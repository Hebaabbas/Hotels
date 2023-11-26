document.getElementById('hotelNameReview').addEventListener('change', function() {
    var selectedHotelId = this.value;
    var form = document.querySelector('.review-form'); // Add a class 'review-form' to your review form
    if (selectedHotelId) {
        form.action = '{% url 'add_review' hotel_id=0 %}'.replace('/0/', '/' + selectedHotelId + '/');
    }
});