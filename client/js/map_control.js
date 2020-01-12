const map = new Datamap({
  element: document.getElementById('choroplethMap'),
  fills: {
    defaultFill: "#ABDDA4"
  },
  // setProjection: "mercator",
  geographyConfig: {
    highlightBorderColor: '#bada55',
    popupTemplate: function (geography, data) {
      return '<div class="hoverinfo">' + geography.properties.name + '</p>Sentiment: ' + data.sentiment + '</p></div>'
    },
    highlightBorderWidth: 3
  },
});

var colors = d3.scale.category10();

const updateMapCanvas = (mapData) => {
  map.
    map.updateChoropleth(mapData);
};

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
      updateMapCanvas(updateMapObj)
      console.log(updateMapObj);
    })
    .catch(err => { console.error(err) }
    )

  e.preventDefault();
}

countryInputForm.onsubmit = updateMap;


