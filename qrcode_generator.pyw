import qrcode
import tkinter as tk
from tkinter import filedialog

def generate_qr_code():
    # Obtenir l'URL à partir de la zone de texte
    url = url_entry.get()

    # Générer le QR code
    qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr_code.add_data(url)
    qr_code.make(fit=True)

    # Créer une image à partir du QR code
    qr_image = qr_code.make_image(fill_color="black", back_color="white")

    # Enregistrer l'image
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if filename:
        qr_image.save(filename)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Générateur de QR code")

# Créer la zone de texte pour l'URL
url_label = tk.Label(root, text="URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Créer le bouton pour générer le QR code
generate_button = tk.Button(root, text="Générer QR code", command=generate_qr_code)
generate_button.pack()

# Lancer la boucle principale de l'interface
root.mainloop()
