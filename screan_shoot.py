import tkinter as tk
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
print(pytesseract.get_tesseract_version())

from PIL import ImageGrab

# Ruta de Tesseract (ajústala según tu instalación)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def start_capture():
    root.withdraw()
    screen = tk.Toplevel()
    screen.attributes("-fullscreen", True)
    screen.attributes("-alpha", 0.3)
    screen.config(bg="gray")

    start = {}

    def on_click(event):
        start["x"] = event.x
        start["y"] = event.y

    def on_release(event):
        x1, y1 = start["x"], start["y"]
        x2, y2 = event.x, event.y
        screen.destroy()

        # Captura del área seleccionada
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save("captura.png")

        # OCR
        texto = pytesseract.image_to_string(img, lang="spa+eng")
        print("\n=== TEXTO DETECTADO ===\n")
        print(texto)

        root.deiconify()

    screen.bind("<ButtonPress-1>", on_click)
    screen.bind("<ButtonRelease-1>", on_release)

root = tk.Tk()
root.geometry("200x100")
tk.Button(root, text="Capturar y extraer texto", command=start_capture).pack()
root.mainloop()