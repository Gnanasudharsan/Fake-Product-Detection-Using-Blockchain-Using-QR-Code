# Fake-Product-Detection-Using-Blockchain-Using-QR-Code
This project ensures the authenticity of products using blockchain technology and QR codes. Manufacturers generate a unique QR code linked to a blockchain entry. Consumers can scan the QR code to verify whether a product is genuine or counterfeit. The system consists of a Solidity smart contract, a Flask backend, and a JavaScript-based frontend.

# Fake Product Detection Using Blockchain & QR Code

## Overview
This project ensures **fake product detection** using **blockchain technology**. A **QR code** is generated for each product, and its authenticity is verified by storing and retrieving its details from a **smart contract on Ethereum**.

## Features
-  **Blockchain-based Verification**: Decentralized product authentication.
-  **QR Code Generation & Scanning**: Unique QR codes for each product.
-  **Smart Contract Implementation**: Immutable and tamper-proof data storage.
-  **Web-based Interface**: Simple UI to scan & verify product authenticity.
-  **Flask API**: Backend API to interact with blockchain.

## Tech Stack
- **Frontend**: HTML, JavaScript, CSS
- **Backend**: Python (Flask)
- **Blockchain**: Solidity (Ethereum Smart Contract)
- **Database**: SQLite
- **QR Code**: OpenCV, QR Code library

## Installation Guide
### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Fake-Product-Detection.git
cd Fake-Product-Detection
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Deploy Smart Contract

```bash
python blockchain/deploy.py
```

### Step 4: Start Flask Backend

```bash
python backend/server.py
```

### Step 5: Open the web interface
