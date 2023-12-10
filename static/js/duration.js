// Function to validate duration input
function validateDuration(input) {
    const durationValue = input.value;
    const durationError = document.getElementById("durationError");
    // Check if the duration is less than or equal to zero
    if (durationValue <= 0) {
        durationError.textContent = "Duration must be greater than zero.";
        input.setCustomValidity("Duration must be greater than zero.");
    } else {
        durationError.textContent = "";
        input.setCustomValidity("");
    }
}