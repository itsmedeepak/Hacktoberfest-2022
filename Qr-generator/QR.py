import pyqrcode
import png
from pyqrcode import QRCode

s = input("Enter Url Of Website, To create QR Code")
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 6)
