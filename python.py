import qrcode
from PIL import Image

# Website URL
url = "https://allensuuuu.github.io/Personal-Website/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save it somewhere, change the path as needed
img.save("website_qr.png")
