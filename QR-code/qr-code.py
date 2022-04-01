import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("You have successfully generated and read a QR Code!")
qr.png("myCode.png", scale=8)

d = decode(Image.open("myCode.png"))
print(d[0].data.decode("ascii"))
