
// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
//google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.

$(document).on('click', '.UpdateChartButton', function(){  
  var variable = $('#variable option:selected').val()
  var renglones = $('#renglones option:selected').val()
  var columnas = $('#columnas option:selected').val()

  $.ajax({
    type: "POST",
    url: "/CNBVQueries",
    dataType: 'json',
    data: JSON.stringify({
      'data_requested': 'TestDataCNBV', 
      'variable': variable,
      'renglones':renglones,
      'columnas':columnas
    })
  })
  .done(function(raw_data){
    // var chart_data = new google.visualization.DataTable();
    // console.log(raw_data);
    // var chart_array = [];
    var chart_array = raw_data['chart_array'];
    console.log(chart_array);

    var chart_data = google.visualization.arrayToDataTable(chart_array)

    // Set chart options
    $('#chart_lead').text(raw_data['title']);

    var options = {
      chartArea:{height: 350},
      chart: {
        title: 'Company Performance',
        subtitle: 'Sales, Expenses, and Profit: 2014-2017',
      },
      bars: 'horizontal', // Required for Material Bar Charts.
      
    };


    // Instantiate and draw our chart, passing in some options.
    //var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
    var chart = new google.charts.Bar(document.getElementById('chart_div'));
    chart.draw(chart_data, options);
  })
});



// function requestChartData(){
//   $.ajax({
//     type: "POST",
//     url: "/CNBVQueries",
//     dataType: 'json',
//     data: JSON.stringify({
//       'data_requested': 'TestDataCNBV', 
//     })
//   })
//   .done(function(data){
//     return data['chartData']
//     });    
// };

// function drawChart() {

//   // Create the data table.
  
  
//   $.ajax({
//     type: "POST",
//     url: "/CNBVQueries",
//     dataType: 'json',
//     data: JSON.stringify({
//       'data_requested': 'TestDataCNBV', 
//     })
//   })
//   .done(function(raw_data){
//     var data = new google.visualization.DataTable();
//     var raw_data = raw_data ['chartData'];
//       console.log(raw_data)

//     for (i in raw_data['columns']){
//       column = raw_data['columns'][i]
//       //console.log(column)
//       data.addColumn(column[0],column[1]);
//     };

//     data.addRows(raw_data['rows'])
//     // for ( i in raw_data['rows'] ){
//     //    row = raw_data['rows'][i]
//     //    console.log(raw_data['rows'])
//     //    console.log(row)
//     //    data.addRows(rows)
//     // };

//     // Set chart options
//     var options = {'title':'Distribucion de numero de acreditados',
//                    'width':400,
//                    'height':300};

//     // Instantiate and draw our chart, passing in some options.
//     //var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
//     var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
//     chart.draw(data, options);
//   }); 
// }


// La funcion original
// function drawChart() {

//   // Create the data table.
//   var data = new google.visualization.DataTable();
//   data.addColumn('string', 'Topping');
//   data.addColumn('number', 'Slices');
//   data.addRows([
//     ['Mushrooms', 3],
//     ['Onions', 1],
//     ['Olives', 1],
//     ['Zucchini', 1],
//     ['Pepperoni', 2]
//   ]);

//   // Set chart options
//   var options = {'title':'How Much Pizza I Ate Last Night',
//                  'width':400,
//                  'height':300};

//   // Instantiate and draw our chart, passing in some options.
//   var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
//   chart.draw(data, options);
// }