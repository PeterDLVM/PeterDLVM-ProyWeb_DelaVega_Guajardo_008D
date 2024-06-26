// static/Js/script-api-mapbox.js

mapboxgl.accessToken = 'pk.eyJ1IjoicGV0ZXJkbHZtIiwiYSI6ImNseHUzbzB3djIzdWwybG9kaWMyYjllOXIifQ.Ur7-q8_LfePRfXNEu66BdA'; // Tu token de acceso
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-70.64827, -33.45694], // Coordenadas de Santiago, Chile
    zoom: 11 // Zoom inicial
});

// Agrega los controles de zoom
map.addControl(new mapboxgl.NavigationControl());

// Personalización de los botones de zoom
document.querySelector(".mapboxgl-ctrl-zoom-in").innerHTML = '<img src="{% static "Img/zoom-in.png" %}" alt="Zoom In">';
document.querySelector(".mapboxgl-ctrl-zoom-out").innerHTML = '<img src="{% static "Img/zoom-out.png" %}" alt="Zoom Out">';

function buscarLugaresCercanos(coordenadas) {
    const buscarParques = fetch(`https://api.mapbox.com/geocoding/v5/mapbox.places/parque.json?proximity=${coordenadas[0]},${coordenadas[1]}&access_token=${mapboxgl.accessToken}`);
    const buscarVeterinarias = fetch(`https://api.mapbox.com/geocoding/v5/mapbox.places/veterinaria.json?proximity=${coordenadas[0]},${coordenadas[1]}&access_token=${mapboxgl.accessToken}`);

    // Realizar ambas búsquedas en paralelo
    Promise.all([buscarParques, buscarVeterinarias])
        .then(responses => Promise.all(responses.map(response => response.json())))
        .then(data => {
            // Combinar los resultados de ambas búsquedas
            const lugaresCercanos = data.flatMap(result => result.features);

            // Muestra los resultados en la consola
            console.log("Datos obtenidos:", lugaresCercanos);

            // Verificar si hay resultados
            if (lugaresCercanos.length > 0) {
                // Iterar sobre cada lugar encontrado
                lugaresCercanos.forEach(place => {
                    // Verificar si hay coordenadas disponibles
                    if (place.geometry && place.geometry.coordinates) {
                        // Agregar marcador para el lugar
                        new mapboxgl.Marker()
                            .setLngLat(place.geometry.coordinates)
                            .setPopup(new mapboxgl.Popup().setHTML(`<h3>${place.text}</h3>`))
                            .addTo(map);
                    } else {
                        console.warn(`Lugar sin coordenadas: ${place.text}`);
                    }
                });
            } else {
                console.log("No se encontraron lugares cercanos.");
            }
        })
        .catch(error => {
            console.error('Error al buscar lugares cercanos:', error);
        });
}

// Función para obtener la ubicación actual del usuario
function obtenerUbicacionActual() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var latitud = position.coords.latitude;
            var longitud = position.coords.longitude;
            new mapboxgl.Marker({ color: 'blue' })
                .setLngLat([longitud, latitud])
                .setPopup(new mapboxgl.Popup().setHTML('<h3>Tu ubicación actual</h3>'))
                .addTo(map);
            // Centrar mapa en la ubicación del usuario
            map.flyTo({ center: [longitud, latitud], zoom: 15 });
            buscarLugaresCercanos([longitud, latitud]);
        }, function(error) {
            console.error('Error al obtener la ubicación:', error);
        });
    } else {
        alert('Geolocalización no es soportada por este navegador.');
    }
}

document.addEventListener("DOMContentLoaded", function() {
    var botonUbicacionActual = document.getElementById("botonUbicacionActual");

    if (botonUbicacionActual) {
        botonUbicacionActual.addEventListener("click", function() {
            obtenerUbicacionActual();
        });
    } else {
        console.error("El botón de ubicación actual no se encontró en el DOM.");
    }
});

