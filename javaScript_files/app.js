
$('#SignUpButton').on('click', function(){
	console.log('ya se dio cuenta que quiero hacer sign up')
	var first_name = $('#first_name').val()
	var last_name = $('#last_name').val()
	var email = $('#email').val()
	var confirm_email = $('#confirm_email').val()
	var password = $('#password').val()
	$('#success_message').addClass('hidden');

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
			'is_administrator':$('#is_administrator').is(':checked'),
			'password':password		
		})
	})
	.done(function(data){
		var next_step = data['next_step'];
		console.log(next_step);


		if (next_step == 'TryAgain'){
			$('#input_error').text(data['input_error'])							
		};

		if (next_step == 'UserCreated'){
			$('#input_error').text('');
			$('#success_message').removeClass('hidden');
			$('#first_name').val('')
			$('#last_name').val('')
			$('#email').val('')
			$('#confirm_email').val('')
			$('#password').val('')
			$('#is_administrator').prop('checked', false)
		};
	})		
});

$('#LogInButton').on('click', function(){
	var email = $('#login_email').val();
	var password = $('#login_password').val();

	$.ajax({
		type: "POST",
		url: "/CrearUsuario",
		dataType: 'json',
		data: JSON.stringify({
			'user_action': 'LogIn',
			'email':email,
			'password':password		
		})
	})
	.done(function(data){
		var next_step = data['next_step'];
		console.log(next_step);

		if (next_step == 'SuccesfulLogIn'){
			window.location.href = '/VisualizadorCNBV'
		};

		if (next_step == 'TryAgain'){
			$('#InvalidEmailOrPasswordError').removeClass('hidden');			
			
		};
	})		
});