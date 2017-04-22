
$('#SignUpButton').on('click', function(){
	console.log('ya se dio cuenta que quiero hacer sign up')
	var first_name = $('#first_name').val()
	var last_name = $('#last_name').val()
	var email = $('#email').val()
	var confirm_email = $('#confirm_email').val()
	var password = $('#password').val()

	$.ajax({
		type: "POST",
		url: "/CrearUsuario",
		dataType: 'json',
		data: JSON.stringify({
			'user_action': 'SignUp',
			'first_name': first_name,
			'last_name':last_name,
			'email':email,
			'confirm_email':confirm_email,
			'password':password		
		})
	})
	.done(function(data){
		var next_step = data['next_step'];
		console.log(next_step);


		if (next_step == 'TryAgain'){
			$('#input_error').text(data['input_error'])						
			
		};
	})		
});