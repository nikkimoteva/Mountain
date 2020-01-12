// var basic_choropleth = new Datamap({
//     element: document.getElementById("basic_choropleth"),
//     projection: 'mercator',
//     fills: {
//       defaultFill: "#ABDDA4"
//     }
//   });
  
  var colors = d3.scale.category10();
  

  const updateMap = (mapData) => {
    map.updateChoropleth({
      USA: colors(45),
      RUS: colors(48),
      AUS: colors(Math.random() * 100),
      BRA: colors(Math.random() * 50),
      CAN: colors(Math.random() * 50),
      ZAF: colors(Math.random() * 50),
      IND: colors(Math.random() * 50),
    });
  };

  window.onload = updateMap();