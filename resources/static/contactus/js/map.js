<script>
    var map;
    function initMap() {
        var myLatLng = {lat: 34.050837, lng: 51.484168};
        map = new google.maps.Map(document.getElementById('map'), {
            zoom: 18,
            scrollwheel: false,
            center: {lat: 34.050837, lng: 51.484168},
            styles: [
                {
                    "featureType": "road.local",
                    "stylers": [
                        {"invert_lightness": true},
                        {"hue": "#909b25"},
                        {"color": "#2980b9"},
                        {"weight": 0.8}
                    ]
                }
            ]
        });
        var image = '/nano-project/static/img/map-marker.png';
        var marker = new google.maps.Marker({
            position: myLatLng,
            animation: google.maps.Animation.BOUNCE,
            map: map,
            title: ' کلینیک علوم و فناوری نانو ',
            icon: image
        });
    }


</script>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB7oBofpoFpFKpWtqsI0EYTv2nQCNNozzc&callback=initMap"
        async defer>
</script>
