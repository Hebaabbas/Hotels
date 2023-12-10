    // Google Maps Initialization
    function initMap() {
        let sweden = { lat: 59.349930, lng: 18.045120 };
        let map = new google.maps.Map(
            document.getElementById('map'), { zoom: 8, center: sweden }
        );
        let marker = new google.maps.Marker({ position: sweden, map: map });}