import cv2
import numpy as np
import pyautogui
import easyocr
from PIL import ImageGrab
import tkinter as tk
from tkinter import simpledialog

# Inisialisasi easyocr reader
reader = easyocr.Reader(['en', 'id'])  # Bahasa Inggris dan Indonesia

# Fungsi untuk memilih area layar dengan tkinter
def select_area():
    root = tk.Tk()
    root.withdraw()  # Sembunyikan window utama
    root.attributes('-topmost', True)  # Pastikan window di atas
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = simpledialog.askinteger("Input", "X (koordinat mulai)")
    y = simpledialog.askinteger("Input", "Y (koordinat mulai)")
    w = simpledialog.askinteger("Input", "Lebar area")
    h = simpledialog.askinteger("Input", "Tinggi area")
    
    if x is None or y is None or w is None or h is None:
        print("Seleksi area dibatalkan.")
        exit()
        
    return (x, y, w, h)

# Fungsi untuk menangkap layar berdasarkan area yang dipilih
def capture_screen(region):
    x, y, w, h = region
    screenshot = ImageGrab.grab(bbox=(x, y, x+w, y+h))
    return np.array(screenshot)

# Fungsi untuk mendeteksi teks dari gambar
def detect_text(img):
    results = reader.readtext(img)
    text = "\n".join([result[1] for result in results])
    return text

if __name__ == "__main__":
    print("Pilih area untuk mendeteksi teks...")
    region = select_area()
    print("Area terpilih: ", region)
    
    while True:
        screen = capture_screen(region)
        cv2.imshow("Area terpilih", screen)
        text = detect_text(screen)
        print("Teks terdeteksi:\n", text)
        
        # Tekan 'q' untuk keluar dari loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
