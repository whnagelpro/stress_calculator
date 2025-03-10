function calculateStress() {
    let force = document.getElementById("force").value;
    let area = document.getElementById("area").value;

    fetch("/calculate", {
        method: "POST",
        body: JSON.stringify({ force: force, area: area }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById("result").innerText = `Stress: ${data.stress} N/m²`;
        }
    })
    .catch(error => console.log("Error:", error));
}
