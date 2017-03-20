var seconds = 0, minutes = 0, hours = 0, limite_periodos = 1, limite_instituciones = 7,        
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


$('.ExpandColapseSection').on('click', function(){
  var target_section = $(this).attr("targetsection")
  $(target_section).toggleClass('hidden');

  var GlaphiconDiv = $(this).find('#PlusMinusGlyphicon');
  GlaphiconDiv.toggleClass('glyphicon-minus');
  GlaphiconDiv.toggleClass('glyphicon-plus'); 
});

$('.SeleccionarCorte').on('click', function(){
  var CorteSeleccionado = $(this)
  var CortesActivos = parseInt($('#NumeroCortesSeleccionados').val());
  var CorteRenglones = $('#CorteRenglones');
  var CorteColumnas = $('#CorteColumnas');

  if (CorteSeleccionado.attr("corte_activo") == "Si") {
    $('#NumeroCortesSeleccionados').val(CortesActivos - 1);
    CorteRenglones.val(CorteColumnas.val())
    CorteColumnas.val('')
  
  } else {

    if ( CortesActivos == 0){
      CorteRenglones.val(CorteSeleccionado.val());
      $('#NumeroCortesSeleccionados').val(1);

    } else if (CortesActivos == 1) {    
      CorteColumnas.val(CorteSeleccionado.val());
      $('#NumeroCortesSeleccionados').val(2);   

    } else {
      flipear_boton_corte($('#boton_' + CorteRenglones.val()));
      flipear_boton_corte($('#boton_' + CorteColumnas.val()));

      CorteRenglones.val(CorteSeleccionado.val())   
      CorteColumnas.val('');
      $('#NumeroCortesSeleccionados').val(1);
    }

  }

  flipear_boton_corte(CorteSeleccionado);

});


function flipear_boton_corte(boton_corte) {
  boton_corte.find('#OkGlyphicon').toggleClass('hidden'); 
  boton_corte.toggleClass('btn-primary');
  boton_corte.toggleClass('btn-default');

  if (boton_corte.attr("corte_activo") == "Si") {
    boton_corte.attr("corte_activo", "No"); 
  } else {
    boton_corte.attr("corte_activo", "Si");
  }

};




// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart', 'bar']});

$(document).on('click', '.UpdateChartButton', function(){  

  $('#chart_lead').addClass('hidden');
  $('#chart_units').addClass('hidden');
  $('#chart_div').addClass('hidden');
  $('#chart_loader').removeClass('hidden');

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
    $('#chart_loader').addClass('hidden');
    $('#chart_lead').removeClass('hidden');
    $('#chart_units').removeClass('hidden');
    $('#chart_div').removeClass('hidden');
    $('#boton_transponer').removeClass('hidden');
    
    $('#chart_lead').text(raw_data['title']);
    $('#chart_units').text(raw_data['chart_units']);

    chart_array = raw_data['chart_array'];
    chart_type = $('input:radio[name=chart_type]:checked').val();
    draw_chart(chart_array, chart_type)

    clearTimeout(t);
    seconds = 0; minutes = 0; hours = 0;  
    var milliseconds_since_start = new Date().valueOf() - start_time
    var m  = new Date(milliseconds_since_start)
    
    console.log('    ')
    console.log('Chart generado')
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

  var is_stacked = $('#is_stacked').is(':checked');
  
  if ($('input:radio[name=show_value_as]:checked').val() == 'percentage'){
    axis_format = 'percent'
  } else {
    axis_format = 'short'
  }

  if ( chart_type == 'bar_chart'){
    options = {
      bar: { groupWidth: '80%'}, 
      // chartArea:{height: '80%', width: '80%'},
      chartArea:{height: '85%', width: '65%'},
      // legend: { position: 'top', maxLines:3}, 
      hAxis: {title:'', format: axis_format},
      isStacked: is_stacked
    };

    chart = new google.visualization.BarChart(document.getElementById('chart_div'));
    chart.draw(chart_data, options);


  } else if (chart_type == 'line_chart'){

    options = {      
      chartArea:{height: '75%', width: '87%'},
      legend: { position: 'top', maxLines:2},      
      vAxis: { format: axis_format}
      // curveType: 'function',
    };
    chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(chart_data, options);
  
  } else if(chart_type == 'column_chart') {
    options = {
      chartArea:{height: '75%', width: '87%'},
      legend: { position: 'top', maxLines:2},
      vAxis: { format: axis_format},
      isStacked: is_stacked
    };
    var view = new google.visualization.DataView(chart_data);
    // view.setColumns()
    chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
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
    limit = limite_instituciones
  
  } else if(nombre_corte == 'periodo') {
    limit = limite_periodos
  
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
    limite_periodos = 1;
    limite_instituciones = 7;
  
  } else if(perspectiva == 'varios_periodos'){
    select_group(grupo_anos);
    select_group(grupo_totalBancaMultiple);
    limite_periodos = 30;
    limite_instituciones = 1;
  
  } else if(perspectiva == 'varias_varios'){
    select_group(grupo_anos);
    select_group(grupo_top7);
    limite_periodos = 15;
    limite_instituciones = 7;

  }
});


var menus_visibles = {
  'saldo_total':['#boton_graficar', '#vista', '#perspectiva_institucion', '[value=periodo]', '[value=institucion]', '#tipo_de_grafica'],
  'concentracion_cartera':['#boton_graficar', '#vista', '#perspectiva_institucion', '#show_value_as', '[value=periodo]', '[value=institucion]', '#tipo_de_grafica'],

  'creditos':['#boton_graficar', '#vista', '#perspectiva_institucion', '[value=periodo]', '[value=institucion]', '#tipo_de_grafica'],
  'acreditados':['#boton_graficar', '#vista', '#perspectiva_institucion', '[value=periodo]', '[value=institucion]', '#tipo_de_grafica'],
  'tasa_i_mn':['#boton_graficar', '#vista', '#perspectiva_institucion', '[value=periodo]', '[value=institucion]', '#tipo_de_grafica'],
  'tasa_i_me':['#boton_graficar', '#vista', '#perspectiva_institucion', '[value=periodo]', '[value=institucion]', '#tipo_de_grafica'],
  'tasa_i_udis':['#boton_graficar', '#vista', '#perspectiva_institucion', '[value=periodo]', '[value=institucion]', '#tipo_de_grafica'],
  'plazo_ponderado':['#boton_graficar', '#vista', '#perspectiva_institucion', '[value=periodo]', '[value=institucion]', '#tipo_de_grafica'],


}


var seleccion_default = {
  'saldo_total':[select_group(grupo_ultimoPeriodo), select_group(grupo_top7), seleccionar_cortes_iniciales('periodo', 'institucion'), seleccionar_grafica_inicial('bar_chart')],
  'concentracion_cartera':[select_group(grupo_ultimoPeriodo), select_group(grupo_top7)],

  'creditos':[select_group(grupo_ultimoPeriodo), select_group(grupo_top7), seleccionar_cortes_iniciales('periodo', 'institucion'), seleccionar_grafica_inicial('bar_chart')],
  'acreditados':[select_group(grupo_ultimoPeriodo), select_group(grupo_top7), seleccionar_cortes_iniciales('periodo', 'institucion'), seleccionar_grafica_inicial('bar_chart')],
  'tasa_i_mn':[select_group(grupo_ultimoPeriodo), select_group(grupo_top7), seleccionar_cortes_iniciales('periodo', 'institucion'), seleccionar_grafica_inicial('bar_chart')],
  'tasa_i_me':[select_group(grupo_ultimoPeriodo), select_group(grupo_top7), seleccionar_cortes_iniciales('periodo', 'institucion'), seleccionar_grafica_inicial('bar_chart')],
  'tasa_i_udis':[select_group(grupo_ultimoPeriodo), select_group(grupo_top7), seleccionar_cortes_iniciales('periodo', 'institucion'), seleccionar_grafica_inicial('bar_chart')],
  'plazo_ponderado':[select_group(grupo_ultimoPeriodo), select_group(grupo_top7), seleccionar_cortes_iniciales('periodo', 'institucion'), seleccionar_grafica_inicial('bar_chart')]
}


function seleccionar_cortes_iniciales(CorteRenglones, CorteColumnas){
  if (CorteRenglones){
    $('#CorteRenglones').val(CorteRenglones)
    flipear_boton_corte($('#boton_' + CorteRenglones));
  }

  if (CorteColumnas){
    $('#CorteColumnas').val(CorteColumnas);
    flipear_boton_corte($('#boton_' + CorteColumnas));
  }
}


function seleccionar_grafica_inicial(chart_type){  
  $('input:radio[name=chart_type]').attr('checked',false)
  // $('#chart_type_bar_chart').prop('checked', true)
  $('input[type=radio][name=chart_type][value=' + chart_type +']' ).prop('checked', true)
};




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

