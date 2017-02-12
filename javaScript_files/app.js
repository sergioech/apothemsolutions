$('.ExpandColapseSection').on('click', function(){
  var target_section = $(this).attr("targetsection")
  $(target_section).toggleClass('hidden');

  var GlaphiconDiv = $(this).find('#PlusMinusGlyphicon');
  GlaphiconDiv.toggleClass('glyphicon-minus');
  GlaphiconDiv.toggleClass('glyphicon-plus'); 
});

$('.SeleccionarCorte').on('click', function(){
	$(this).toggleClass('btn-primary');
	$(this).toggleClass('btn-default');

	$(this).find('#OkGlyphicon').toggleClass('hidden');


});