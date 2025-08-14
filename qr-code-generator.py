import qrcode

website_link = input("Enter the website link to generate a QR code: ")

qr = qrcode.QRCode(version=1 , box_size=5, border=5)

qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'")