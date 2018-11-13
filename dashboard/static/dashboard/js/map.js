loadGoogleMapsApi().then(function (googleMaps) {
  new googleMaps.Map(document.querySelector('.map'), {
    center: {
      lat: 40.7484405,
      lng: -73.9944191
    },
    zoom: 12
  })
}).catch(function (error) {
  console.error(error)
})