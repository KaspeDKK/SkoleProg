document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("prediction-form");
    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        fetch("/id/", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Update your page with the prediction
            const predictionOutput = document.getElementById("prediction-output");
            predictionOutput.textContent = "Prediction: " + data.prediction;
        })        
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
