function calculateStress() {
    let force = parseFloat(document.getElementById("force").value);
    let area = parseFloat(document.getElementById("area").value);

    // Validate input
    if (isNaN(force) || isNaN(area)) {
        alert("Please enter valid numbers for force and area.");
        return;
    }
    if (area === 0) {
        alert("Area cannot be zero. Division by zero is not allowed.");
        return;
    }

    fetch("/calculate", {
        method: "POST",
        body: JSON.stringify({ force: force, area: area }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Server error. Please try again.");
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById("result").innerText = `Stress: ${data.stress} N/m²`;
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while calculating stress.");
    });
}
