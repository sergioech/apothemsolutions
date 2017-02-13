
// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

$(document).on('click', '.UpdateChartButton', function(){  
  var variable = $('#variable option:selected').val();
  var renglones = $('#CorteRenglones').val();
  var columnas = $('#CorteColumnas').val();

  var cortes = jQuery('.corte');
  var filtros = determinar_filtros(cortes);


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
      },
      bars: 'horizontal', // Required for Material Bar Charts.
      
    };

    var chart = new google.charts.Bar(document.getElementById('chart_div'));
    chart.draw(chart_data, options);
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








