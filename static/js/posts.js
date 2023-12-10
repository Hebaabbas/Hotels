document.addEventListener('DOMContentLoaded', function () {
    // Get the dropdown element for hotel selection in the review form
    var hotelDropdown = document.getElementById('hotelNameReview');
    // Get the review form element
    var form = document.querySelector('.review-form');

    if (hotelDropdown && form) {
        hotelDropdown.addEventListener('change', function () {
            var selectedHotelId = this.value;
            console.log('Selected Hotel ID:', selectedHotelId);
            // Update the form's action attribute to include the selected hotel ID
            if (selectedHotelId) {
                form.action = form.action.replace('hotel_id=0', 'hotel_id=' + selectedHotelId);
            }

            console.log('Form Action After:', form.action);
        });
    }
});


// Function to update the action attribute of the review form based on the selected hotel ID
function updateAction(hotelId) {
    // Get the review form element by its ID
    var form = document.getElementById('reviewForm');
    form.action = '/todo/add_review/' + hotelId + '/';
}
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('hotelNameReview').addEventListener('change', function() {
        // Get the selected hotel's ID
        var hotelId = this.value;
        var form = document.getElementById('reviewForm');
        // Update the form's action attribute to include the selected hotel ID using Django's URL template tag
        form.action = "{% url 'add_review' 0 %}".replace('/0/', '/' + hotelId + '/');
    });
});



