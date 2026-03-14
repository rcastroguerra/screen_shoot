import os

SCRIPTS_DIR = "scripts"
OUTPUT_FILE = os.path.join(SCRIPTS_DIR, "scripts_list.txt")

def generar_lista():
    if not os.path.exists(SCRIPTS_DIR):
        print(f"La carpeta '{SCRIPTS_DIR}' no existe.")
        return

    archivos = [
        f for f in os.listdir(SCRIPTS_DIR)
        if f.endswith(".py")
    ]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for archivo in archivos:
            f.write(archivo + "\n")

    print(f"scripts_list.txt generado con {len(archivos)} scripts.")

if __name__ == "__main__":
    generar_lista()