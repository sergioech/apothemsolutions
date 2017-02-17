var seconds = 0, minutes = 0, hours = 0,
    t;

var start_time;

function add() {
    seconds++;
    if (seconds >= 60) {
        seconds = 0;
        minutes++;
        if (minutes >= 60) {
            minutes = 0;
            hours++;
        }
    }
    
    console.log((hours ? (hours > 9 ? hours : "0" + hours) : "00") + ":" + (minutes ? (minutes > 9 ? minutes : "0" + minutes) : "00") + ":" + (seconds > 9 ? seconds : "0" + seconds));
    timer();
}

function timer() {
    t = setTimeout(add, 1000);
}

// timer();


/* Start button */
// start.onclick = timer;

/* Stop button */
// stop.onclick = function() {
//     clearTimeout(t);
// }

// /* Clear button */
// clear.onclick = function() {
//     h1.textContent = "00:00:00";
//     seconds = 0; minutes = 0; hours = 0;
// }




// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

$(document).on('click', '.UpdateChartButton', function(){  
  var variable = $('#variable option:selected').val();
  var renglones = $('#CorteRenglones').val();
  var columnas = $('#CorteColumnas').val();

  var cortes = jQuery('.corte');
  var filtros = determinar_filtros(cortes);

  start_time = new Date()
  timer()

  $.ajax({
    type: "POST",
    url: "/CNBVQueries",
    dataType: 'json',
    data: JSON.stringify({
      'data_requested': 'TestDataCNBV', 
      'variable': variable,
      'renglones':renglones,
      'columnas':columnas,
      'filtros':filtros
    })
  })
  .done(function(raw_data){
    var chart_array = raw_data['chart_array'];

    var chart_data = google.visualization.arrayToDataTable(chart_array)

    $('#chart_lead').text(raw_data['title']);

    var options = {
      chartArea:{height: 350},
      chart: {
        title: 'Company Performance',
        subtitle: 'Sales, Expenses, and Profit: 2014-2017',
        isStacked: true
      },
      bars: 'horizontal', // Required for Material Bar Charts.
      isStacked: true
    };

    var chart = new google.charts.Bar(document.getElementById('chart_div'));
    chart.draw(chart_data,  google.charts.Bar.convertOptions(options));
    
    clearTimeout(t);
    seconds = 0; minutes = 0; hours = 0;

    var milliseconds_since_start = new Date().valueOf() - start_time
    var m  = new Date(milliseconds_since_start)
    
    console.log('    ')
    console.log('Chart generado')
    console.log('A Echeverría le gusta dar beso negro')
    console.log('Total de data points en query: ' + raw_data['total_dps'])
    console.log('Total de tiempo requerido para generar chart: '+m.getMinutes()+":"+m.getSeconds())
    console.log('    ')

  })
});

function determinar_filtros(cortes){
  
  var filtros = {}; 
  var opciones_validas = [];

  cortes.each(function(){
    opciones = $(this).find('.opcion')
    
    opciones_validas = []

    opciones.each(function(){
      if ($(this).is(':checked')){
        opciones_validas.push($(this).val())
      };
    });
    filtros[$(this).attr("value")] = opciones_validas
  });
  return filtros;
}








