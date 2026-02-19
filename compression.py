import os
import sys  

# Taille minimale en octets (ici 100 Mo)
MIN_SIZE_BYTES = 100 * 1024 * 1024  
def verifier_taille(chemin):
    taille = os.path.getsize(chemin)
    if taille <= MIN_SIZE_BYTES:
        print(f"Fichier trop petit : {taille / (1024*1024):.2f} Mo")
        print(f"La taille minimale requise est strictement supérieure à 100 Mo. Insere autre fichier superieur du 100 Mo")
        sys.exit(1)
    print(f"[OK] Taille du fichier : {taille / (1024*1024):.2f} Mo")
    return taille

def lire_fichier(chemin): 
    with open(chemin, "r", encoding="utf-8") as f: 
        contenu = f.read() 
        return contenu 
        # Exemple d’utilisation 

def lz77_compress(chemin, window_size=20):
    data = lire_fichier(chemin)
    i = 0
    output = []
    while i < len(data):
        match = (-1, -1, "")
        # Chercher la plus longue correspondance dans la fenêtre
        for j in range(max(0, i - window_size), i):
            length = 0
            while (i + length < len(data) and
                   data[j + length] == data[i + length]):
                length += 1
                if j + length >= i:
                    break
            if length > match[1]:
                match = (i - j, length, data[i + length] if i + length < len(data) else "")
        if match[1] > 0:
            output.append((match[0], match[1], match[2]))
            i += match[1] + 1
        else:
            output.append((0, 0, data[i]))
            i += 1
    
    # Calculer la taille compressée (nombre de tuples)
    size_data = len(data)
    compressed_size = len(output)
    print(f"Compressed: {size_data / (1024*1024):.2f} Mo")
    print(f"Compressed size: {compressed_size / (1024*1024):.2f} Mo")
    return output

lz77_compress("autre.txt")