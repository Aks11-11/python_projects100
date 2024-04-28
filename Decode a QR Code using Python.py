from pyzbar.pyzbar import decode
from PIL import Image
decocdeQR = decode(Image.open('instagram.png'))
print(decocdeQR[0].data.decode('ascii'))
