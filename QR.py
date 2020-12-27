#in this we are going to create a QR Code Generator
#we are going to import a library called py qr code

import pyqrcode
import png

def qrcode():
    q = pyqrcode.create(input())
    q.png('qrcode.png', scale=5)
    print("QR Code Generated")


if __name__ == '__main__':
    qrcode()
