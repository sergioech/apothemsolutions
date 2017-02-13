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

