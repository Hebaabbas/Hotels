document.addEventListener('DOMContentLoaded', function () {
    // Function to validate duration input
    function validateDuration() {
        const durationInput = document.getElementById('durationStay');
        const duration = parseInt(durationInput.value, 10);
        if (duration < 1) {
            durationInput.setCustomValidity("Duration must be 1 day or more.");
        } else {
            durationInput.setCustomValidity("");
        }
    }

    // Add change event listener to the duration input
    const durationInput = document.getElementById('durationStay');
    if (durationInput) {
        durationInput.addEventListener('change', validateDuration);
        durationInput.addEventListener('input', validateDuration); 
    }

    // Add submit event listener to the form
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        validateDuration();
        if (!this.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
    });
});
