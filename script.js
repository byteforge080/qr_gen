async function generateQR() {
    const data = document.getElementById("text").value;

    const res = await fetch("/generate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({data})
    });

    const out = await res.json();

    document.getElementById("qr").src = out.image;
}

async function scanQR() {
    const fileInput = document.getElementById("file");
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("/scan", {
        method: "POST",
        body: formData
    });

    const out = await res.json();

    document.getElementById("result").innerText = out.result;
}