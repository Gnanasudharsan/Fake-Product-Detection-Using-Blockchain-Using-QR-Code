import cv2

def scan_qr(image_path):
    """
    Scans a QR code from the given image and extracts the data.
    
    :param image_path: Path to the QR code image file.
    :return: The extracted QR code data or an error message.
    """
    detector = cv2.QRCodeDetector()
    img = cv2.imread(image_path)

    if img is None:
        return "Error: Could not read image. Check file path."

    data, _, _ = detector.detectAndDecode(img)
    
    if data:
        return f" QR Code Data: {data}"
    else:
        return " No QR code detected."

# Example usage
if __name__ == "__main__":
    image_file = "qr_codes/12345ABC.png"  # Example QR code file
    result = scan_qr(image_file)
    print(result)
