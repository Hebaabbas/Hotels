document.addEventListener('DOMContentLoaded', function () {
    // Function to validate duration input
    function validateDuration() {
        const durationInput = document.getElementById('durationStay');
        if (durationInput) {
            const duration = Number(durationInput.value);
            if (duration < 1) {
                durationInput.setCustomValidity("Duration must be 1 day or more.");
            } else {
                durationInput.setCustomValidity("");
            }
        }
    }

    // Event listener for duration input change
    const durationInput = document.getElementById('durationStay');
    if (durationInput) {
        durationInput.addEventListener('input', validateDuration);
    }

    // Form submission event listener
    const reviewForm = document.querySelector('form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', function (event) {
            validateDuration();
            if (!this.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
        });
    }
});
