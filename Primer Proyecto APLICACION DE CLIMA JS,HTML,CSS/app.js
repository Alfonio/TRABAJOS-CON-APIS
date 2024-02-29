// Utilizo una API geolocalizador https://developer.mozilla.org/es/docs/Web/API/Geolocation_API
//Utilizo una API de Clima https://home.openweathermap.org/
window.addEventListener('load', () => {

    let latitud;
    let longitud;

    let temperaturaValor = document.getElementById('temperatura-valor');
    let temperaturaDescripcion = document.getElementById('temperatura-descripcion');
    let ubicacion = document.getElementById('ubicacion');

    let vientoVelocidad = document.getElementById('viento-velocidad');
    let iconoAnimado = document.getElementById('icono-animado');

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(posicion => {
            const longitud = posicion.coords.longitude;
            const latitud = posicion.coords.latitude;
            const AppyKey = 'c4fb57ed47efc3f944df24c167b74b08';
            const url = `https://api.openweathermap.org/data/2.5/weather?lat=${latitud}&lon=${longitud}&appid=${AppyKey}&units=metric&lang=es`;

            fetch(url)
                .then(response => { return response.json() })
                .then(data => {
                    let temp = Math.round(data.main.temp);
                    temperaturaValor.textContent = `${temp} °C`;

                    let desc = traducirDescripcionClima(data.weather[0].description);
                    temperaturaDescripcion.textContent = desc.toUpperCase();
                    ubicacion.textContent = data.name;

                    vientoVelocidad.textContent = `${data.wind.speed} m/s`;

                    switch (data.weather[0].main) {
                        case 'Thunderstorm':
                            iconoAnimado.src = 'animated/thunder.svg';
                            break;
                        case 'Drizzle':
                            iconoAnimado.src = 'animated/rainy-2.svg';
                            break;
                        case 'Rain':
                            iconoAnimado.src = 'animated/rainy-7.svg';
                            break;
                        case 'Snow':
                            iconoAnimado.src = 'animated/snowy-6.svg';
                            break;
                        case 'Clear':
                            iconoAnimado.src = 'animated/day.svg';
                            break;
                        case 'Atmosphere':
                            iconoAnimado.src = 'animated/weather.svg';
                            break;
                        case 'Clouds':
                            iconoAnimado.src = 'animated/cloudy-day-1.svg';
                            break;
                        default:
                            iconoAnimado.src = 'animated/cloudy-day-1.svg';
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        });
    }
});

function traducirDescripcionClima(englishDescription) {
    // Función para traducir las descripciones del clima de inglés a español
    switch (englishDescription) {
        case 'Thunderstorm':
            return 'Tormenta';
        case 'Drizzle':
            return 'Llovizna';
        case 'Rain':
            return 'Lluvia';
        case 'Snow':
            return 'Nieve';
        case 'Clear':
            return 'Despejado';
        case 'Atmosphere':
            return 'Atmósfera';
        case 'Clouds':
            return 'Nublado';
        default:
            return englishDescription;
    }
}


    //modo sin ecmascript 6 
    // const options = {
    //     enableHighAccuracy: true,
    //     timeout: 5000,
    //     maximumAge: 0,
    //   };
      
    //   function success(pos) {
    //     const crd = pos.coords;
      
    //     console.log("Your current position is:");
    //     console.log(`Latitude : ${crd.latitude}`);
    //     console.log(`Longitude: ${crd.longitude}`);
    //     console.log(`More or less ${crd.accuracy} meters.`);
    //   }
      
    //   function error(err) {
    //     console.warn(`ERROR(${err.code}): ${err.message}`);
    //   }
      
    //   navigator.geolocation.getCurrentPosition(success, error, options);
      