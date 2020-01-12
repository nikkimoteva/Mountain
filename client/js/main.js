const countryInputForm = document.getElementById("countrySelect");


function updateMap(e) {
  console.log(e);

  const countryInput = e.target.elements[0].value.toUpperCase();
  const countryPromise = getSentiments(countryInput);

  countryPromise
    .then(countries => {
      const updateMapObj = {}
      countries.forEach(country => {
        updateMapObj[country["target"]] = { "sentiment": country["sentiment"] * 100 }
      })
      return updateMapObj
    })
    .then(updateMapObj => {
      // updateMap(updateMapObj) 
      console.log(updateMapObj);
    })
    .catch(err => { console.error(err) }
    )

  e.preventDefault();
}

countryInputForm.onsubmit = updateMap;


