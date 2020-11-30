var map, marker, $lat, $lon;

function initMap(lat, lon, mark_draggable, init_zoom) { // Ta funkcja jest ważna przy odczycie zgłoszeń

    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: init_zoom,
        center: { lat: lat, lng: lon },
    });

     marker = new google.maps.Marker({
        position: { lat: lat, lng: lon },
        map: map,
        draggable: mark_draggable,
    });

    google.maps.event.addListener(map, 'click', function (ev) {
        if(mark_draggable){
            setMarkerPosition(ev.latLng.lat(), ev.latLng.lng());
        }
    });

    setMarkerPosition(lat, lon);
}

function setMarkerPosition(lat, lon) { // Ta funkcja jest ważna dla dodawania zgłoszeń
    marker.setPosition({ lat: lat, lng: lon });
    document.getElementById("lat").value = lat.toFixed(6);
    document.getElementById("lon").value = lon.toFixed(6);
};

