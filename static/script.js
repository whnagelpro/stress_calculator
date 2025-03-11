async function calculateStress() {
    const force = parseFloat(document.getElementById("force").value);
    const area = parseFloat(document.getElementById("area").value);

    const response = await fetch("/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ force, area })
    });

    const data = await response.json();

    if (response.ok) {
        document.getElementById("result").innerText = `Stress: ${data.stress}`;
    } else {
        document.getElementById("result").innerText = `Error: ${data.error}`;
    }
}
