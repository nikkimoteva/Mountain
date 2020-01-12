const countryInputForm = document.getElementById("countrySelect");

const normalize = (val, max, min) => { return (val - min) / (max - min); }

function updateMap(e) {
  console.log(e);

  const countryInput = e.target.elements[0].value.toUpperCase();

  const countryPromise = getSentiments(countryInput);

  countryPromise
    .then(countries => {
      const updateMapObj = {}
      countries.forEach(country => {
        updateMapObj[country["target"]] = country["sentiment"]
      })
      return updateMapObj
    })
    .then(updateMapObj => { console.log(updateMapObj) })
    .catch(err => { console.error(err) }
    )

  e.preventDefault();
}

countryInputForm.onsubmit = updateMap;


