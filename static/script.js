function calculateStress() {
        let force = parseFloat(document.getElementById("force").value);
        let area = parseFloat(document.getElementById("area").value);
    
        if (isNaN(force) || isNaN(area)) {
            alert("Please enter valid numbers for force and area.");
            return;
        }
        if (area === 0) {
            alert("Area cannot be zero. Division by zero is not allowed.");
            return;
        }
    
        console.log("Sending request to: https://stress_calculator-1.onrender.com/calculate");
    
        fetch("https://stress_calculator-1.onrender.com/calculate", {// Ensure it's pointing to the local Flask server
            method: "POST",
            body: JSON.stringify({ force: force, area: area }),
            headers: { "Content-Type": "application/json" }
        })
        .then(response => {
            console.log("Response received:", response);
            return response.json();
        })
        .then(data => {
            console.log("Data received:", data);
            if (data.error) {
                alert(`Error: ${data.error}`);
            } else {
                document.getElementById("result").innerText = `Stress: ${data.stress} N/m²`;
            }
        })
        .catch(error => {
            console.error("Fetch Error:", error);
            alert("An error occurred while communicating with the server.");
        });
    }