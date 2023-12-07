document.addEventListener('DOMContentLoaded', function () {
    var hotelDropdown = document.getElementById('hotelNameReview');
    var form = document.querySelector('.review-form');

    if (hotelDropdown && form) {
        hotelDropdown.addEventListener('change', function () {
            var selectedHotelId = this.value;
            console.log('Selected Hotel ID:', selectedHotelId);

            if (selectedHotelId) {
                form.action = form.action.replace('hotel_id=0', 'hotel_id=' + selectedHotelId);
            }

            console.log('Form Action After:', form.action);
        });
    }
});
