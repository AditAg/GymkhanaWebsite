   var position = [25.2623,  82.9893];
function myMap() {
var latLng = new google.maps.LatLng(position[0], position[1]);
  var mapCanvas = document.getElementById("contact");
  var mapOptions = {
    center:latLng,
    zoom: 16
  }
  var map = new google.maps.Map(mapCanvas, mapOptions);
  marker = new google.maps.Marker({
        position: latLng,
        map: map,
        animation: google.maps.Animation.DROP
    });
}
