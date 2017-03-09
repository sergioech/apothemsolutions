var seconds = 0, minutes = 0, hours = 0,
    start_time,
    t,
    chart_array,
    chart_type;

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


// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

$(document).on('click', '.UpdateChartButton', function(){  
  var variable = $('#variable option:selected').val();
  var show_value_as = $('input:radio[name=show_value_as]:checked').val();

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
      'perspectiva_institucion':$('input:radio[name=perspectiva_institucion]:checked').val(),
      'show_value_as': show_value_as,
      'renglones':renglones,
      'columnas':columnas,
      'filtros':filtros
    })
  })
  .done(function(raw_data){
        
    $('#chart_lead').text(raw_data['title']);

    chart_array = raw_data['chart_array'];
    chart_type = $('input:radio[name=chart_type]:checked').val();
    draw_chart(chart_array, chart_type)

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

// function draw_chart(chart_data, chart_type, chart_options, chart_details){
function draw_chart(chart_array, chart_type){
  
  var chart_data = google.visualization.arrayToDataTable(chart_array),
    options,
    axis_format,
    chart_subtitle, 
    chart;

  if ($('input:radio[name=show_value_as]:checked').val() == 'percentage'){
    axis_format = 'percent'
    chart_subtitle = '%'
  } else {
    axis_format = 'short'
    chart_subtitle = 'Pesos (MXN)'
  }

  if ( chart_type == 'bar_chart'){
    options = {
      chartArea:{height: 350},
      chart: {
        title: 'Company Performance',
        subtitle: 'Sales, Expenses, and Profit: 2014-2017',
        isStacked: true,
        explorer:{}
      },
    bars: 'horizontal', // Required for Material Bar Charts.
    isStacked: true
    };

    chart = new google.charts.Bar(document.getElementById('chart_div'));
    chart.draw(chart_data,  google.charts.Bar.convertOptions(options));

  } else if (chart_type == 'line_chart'){

    options = {
      subtitle: 'in millions of dollars (USD)',
      chart:{ title: 'Box Office Earnings in First Two Weeks of Opening', subtitle: 'in millions of dollars (USD)'},
      chartArea:{height: '75%', width: '87%'},
      // title: 'Company Performance',
      curveType: 'function',
      legend: { position: 'top', maxLines:2},      
      vAxis: { format: axis_format}
    };
    chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(chart_data, options);
  };
};


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


function transpose_matrix(matrix){
  var newArray = [],
    origArrayLength = matrix.length,
    arrayLength = matrix[0].length,
    i;
  
  for(i = 0; i < arrayLength; i++){
      newArray.push([]);
  };

  for(i = 0; i < origArrayLength; i++){
      for(var j = 0; j < arrayLength; j++){
          newArray[j].push(matrix[i][j]);
      };
  };
  return newArray  
};


$('input[type=radio][name=chart_type]').on('change',function(){
  if(chart_array != undefined){
    chart_type = $('input:radio[name=chart_type]:checked').val();
    draw_chart(chart_array, chart_type);
  }
});  

$('#transpose_button').on('click',function(){
  // console.log('Si detecto que quiero transponer los datos')
  if(chart_array != undefined){
    chart_type = $('input:radio[name=chart_type]:checked').val();
    chart_array = transpose_matrix(chart_array);
    draw_chart(chart_array, chart_type);
    // console.log('Si dibujo el chart sin tener que hacer el AJAX request')
  }  
});


$(document).on('change', '.select_all_checkbox', function(){
  
  var checked_option = $(this).is(':checked')
  var target_section = $(this).attr('target_section');
  var opciones = $(target_section).find('.opcion');  

  opciones.each(function(){
    $(this).prop('checked', checked_option);
  });

});


$('input.opcion').on('change', function() {
  var nombre_corte = $(this).closest('#Corte').attr("value"),
    opciones_seleccionadas = $(this).closest('#Corte').find('.opcion').filter(':checked').length,
    limit;

  if (nombre_corte == 'institucion'){
    limit = 7
  } else if(nombre_corte == 'periodo') {
    limit = 20
  } else {
    limit = 50
  }
  
   if(opciones_seleccionadas > limit) {
       this.checked = false;
   }
});


var grupo_totalBancaMultiple = [
  '#institucion_00'
]

var grupo_top7 = [
  '#institucion_16', //Banamex
  '#institucion_31', //Banorte/Ixe
  '#institucion_34', //BBVA Bancomer
  '#institucion_40', //HSBC
  '#institucion_42', //Inbursa
  '#institucion_53', //Santande
  '#institucion_55', //Scotiabank
]


var grupo_ultimoPeriodo = [
  '#periodo_201612'
]


var grupo_anos = [
  '#periodo_201612',
  '#periodo_201512',
  '#periodo_201412',
  '#periodo_201312',
  '#periodo_201212',
]



function select_group(lista_ids){
  
  var opciones = $(lista_ids[0]).closest('#Corte').find('.opcion');
  
  opciones.each(function(){
    $(this).prop('checked', false);
  });

  for( miembro in lista_ids){
    $(lista_ids[miembro]).prop('checked', true)
  }
};


function limpiar_corte(id_corte){
  var opciones = $(id_corte).find('.opcion');  
  opciones.each(function(){
    $(this).prop('checked', false);
  });
}


$('input[type=radio][name=perspectiva_institucion]').on('change',function(){
  var perspectiva = $('input:radio[name=perspectiva_institucion]:checked').val()

  if(perspectiva == 'varios_bancos'){
    select_group(grupo_ultimoPeriodo);
    select_group(grupo_top7);
  
  } else if(perspectiva == 'varios_periodos'){
    select_group(grupo_anos);
    select_group(grupo_totalBancaMultiple);
  }
});


var menus_visibles = {
  'concentracion_cartera':['#boton_graficar', '#vista','#perspectiva_institucion', '#show_value_as', '[value=periodo]', '[value=institucion]']
}


var seleccion_default = {
  'concentracion_cartera':[select_group(grupo_ultimoPeriodo), select_group(grupo_top7)]
}


function unhide_group(lista_ids){
  for( miembro in lista_ids){
    $(lista_ids[miembro]).removeClass('hidden') 
  }
};


function seleccionar_default(variable){
  var lista_funciones = seleccion_default[variable]

  for( miembro in lista_funciones){
    lista_funciones[miembro]
  };
};  


$('#variable').on('change', function(){
  console.log('Si detecto que esta cambiando la variable');  
  
  var variable = $(this).val();  
  unhide_group(menus_visibles[variable]);
  seleccionar_default(variable);
});

