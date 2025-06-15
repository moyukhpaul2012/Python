'''
Create your own virtual environment and execute the program inside your .venv folder
'''

import qrcode # pip install qrcode inside your .venv

data= input("Enter the text or URL: ").strip()
fileName= input("Enter the file name: ").strip()

qr= qrcode.QRCode(box_size= 10, border= 4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(fileName)
print(f"QR code saved as: {fileName}")