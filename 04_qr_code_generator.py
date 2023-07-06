import qrcode

# Define the data you want to encode
data = "rajkumar"

# Generate the QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image file
qr_image.save("qrcode.png")
