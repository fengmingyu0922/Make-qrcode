import qrcode
import random
import os

def makeqrcode(data,filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="green", back_color="white")
    img.save(f"./qrcode/{filename}")
