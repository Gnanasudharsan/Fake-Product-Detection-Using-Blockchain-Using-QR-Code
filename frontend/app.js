// Function to scan QR code and extract data
async function scanQRCode() {
    let fileInput = document.getElementById("qrInput").files[0];

    if (!fileInput) {
        alert("Please upload a QR code image.");
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput);

    try {
        let response = await fetch("http://127.0.0.1:5000/scan_qr", {
            method: "POST",
            body: formData
        });

        let data = await response.json();
        document.getElementById("qrResult").innerText = `Scanned Data: ${data.data}`;

    } catch (error) {
        console.error("Error scanning QR code:", error);
        alert("Failed to scan QR code.");
    }
}

// Function to verify product authenticity
async function verifyProduct() {
    let serialNumber = document.getElementById("serialInput").value;

    if (!serialNumber) {
        alert("Please enter a product serial number.");
        return;
    }

    try {
        let response = await fetch("http://127.0.0.1:5000/verify_product", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ serial: serialNumber })
        });

        let data = await response.json();
        document.getElementById("verificationResult").innerText = `Product Status: ${data.status}`;

    } catch (error) {
        console.error("Error verifying product:", error);
        alert("Failed to verify product.");
    }
}
