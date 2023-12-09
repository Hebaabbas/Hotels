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



function updateAction(hotelId) {
    var form = document.getElementById('reviewForm');
    form.action = '/todo/add_review/' + hotelId + '/';
}
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('hotelNameReview').addEventListener('change', function() {
        var hotelId = this.value;
        var form = document.getElementById('reviewForm');
        form.action = "{% url 'add_review' 0 %}".replace('/0/', '/' + hotelId + '/');
    });
});