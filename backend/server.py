import qrcode
import cv2
import sqlite3
from flask import Flask, request, jsonify
from web3 import Web3

# Initialize Flask app
app = Flask(__name__)

# Connect to Blockchain
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
contract_address = "0xYourContractAddress"  # Replace with deployed contract address
contract_abi = [...]  # Replace with compiled ABI
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Database setup
def init_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, serial TEXT)''')
    conn.commit()
    conn.close()

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json['data']
    img = qrcode.make(data)
    img.save("qr_codes/" + data + ".png")
    return jsonify({"message": "QR Code generated!", "path": "qr_codes/" + data + ".png"})

@app.route('/scan_qr', methods=['POST'])
def scan_qr():
    file = request.files['file']
    file.save("temp_qr.png")
    detector = cv2.QRCodeDetector()
    val, _, _ = detector.detectAndDecode(cv2.imread("temp_qr.png"))
    return jsonify({"message": "Scanned successfully", "data": val})

@app.route('/verify_product', methods=['POST'])
def verify_product():
    serial = request.json['serial']
    stored_product = contract.functions.verifyProduct(serial).call()
    return jsonify({"status": "Genuine" if stored_product else "Fake"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
