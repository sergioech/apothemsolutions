
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
	console.log('Si se dio cuenta de que quiero hacer login')

	var email = $('#login_email').val();
	var password = $('#login_password').val();

	$.ajax({
		type: "POST",
		url: "/LogIn",
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


$('#RequestPasswordReset').on('click', function(){
	var user_email = $('#user_email').val()
	$.ajax({
		type: "POST",
		url: "/Accounts",
		dataType: 'json',
		data: JSON.stringify({
			'user_action': 'RequestPasswordReset',
			'user_email': user_email,			
		})
	})
	.done(function(data){
		var next_step = data['next_step'];
		console.log(next_step);

		if (next_step == 'EnterValidEmail'){
			$('#InvalidEmailError').removeClass('hidden');
		};

		if (next_step == 'CheckYourEmail'){
			$('#request_reset_email').toggleClass('hidden');
			$('#reset_email_sent').toggleClass('hidden');
		};
	})		
});


$('#PasswordResetButton').on('click', function(){
	var usuario_id = $('#usuario_id').val()
	var password_hash = $('#password_hash').val()
	var new_password = $('#NewPassword').val()
	$.ajax({
		type: "POST",
		url: "/Accounts",
		dataType: 'json',
		data: JSON.stringify({
			'user_action': 'SetNewPassword',
			'new_password': new_password,
			'usuario_id':usuario_id,
			'password_hash':password_hash		
		})
	})
	.done(function(data){
		var next_step = data['next_step'];
		console.log(next_step);

		if (next_step == 'EnterValidPassword'){
			$('#InvalidPasswordError').removeClass('hidden');
		};

		if (next_step == 'GoToLandingPage'){
			$('#enter_new_password').toggleClass('hidden');
			$('#password_reseted').toggleClass('hidden');
			
		};
	})		
});


function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#imgInp").change(function(){
    readURL(this);
});

$(document).on('focusin', '.QuickAttributeUpdate', function(){
	
	var attr_value = $(this).val();

	$(this).on('focusout', function(){
		if(attr_value != $(this).val()){
			var attr_key = $(this).attr("name");
			var slide = $(this).closest('#DeckEditorSlide');
			var slide_id = slide.attr("value");
			
			console.log(attr_key);
			console.log(attr_value);

			$.ajax({
				type: "POST",
				url: "/DeckEditor",
				dataType: 'json',
				data: JSON.stringify({
					'slide_id': slide_id,
					'user_action': 'UpdateSlide',
					'attr_key':attr_key,
					'attr_value':$(this).val(),
				})
			}).done(function(data){console.log(data['message'])})
		}
	})
});