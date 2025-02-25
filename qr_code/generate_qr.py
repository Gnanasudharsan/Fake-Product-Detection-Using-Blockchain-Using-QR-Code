import qrcode
import os

# Ensure QR code directory exists
QR_CODE_DIR = "qr_codes"
if not os.path.exists(QR_CODE_DIR):
    os.makedirs(QR_CODE_DIR)

def generate_qr(data, filename):
    """
    Generates a QR code with the given data and saves it as an image file.
    
    :param data: The data to encode in the QR code.
    :param filename: The name of the output file (without extension).
    :return: The path of the generated QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    
    file_path = os.path.join(QR_CODE_DIR, f"{filename}.png")
    img.save(file_path)
    
    return file_path

# Example usage
if __name__ == "__main__":
    product_serial = "12345ABC"  # Example product serial number
    qr_path = generate_qr(product_serial, product_serial)
    print(f"QR Code generated: {qr_path}")
