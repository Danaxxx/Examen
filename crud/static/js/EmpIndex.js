
//EmpIndex
$(function() 
{
	$(".btnEnviar").click(function()
	{
	let email = $("#email").val();
	let contraseña = $("#password").val();
	if(!email)
	{
		alert("Debe rellenar este campo");
		$("#email").focus();
		return false;
	}
	else if(email.length<13){
		alert("El correo electronico debe tener un minimo de 13 caracteres");
	}
	else if($("#email").val().indexOf('@', 0) == -1 || $("#email").val().indexOf('.', 0) == -1){
	alert('El correo electrónico introducido no es correcto.');
	$("#email").focus();
	return false;
	}
	
	else if(!contraseña)
	{
		alert("Debe especificar la contraseña");
		$("#password").focus();
		return false;
	}  
	});
	let correo = 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ@.1234567890_-';
	$("#email").keypress(function(e)
	{
		let caracter = String.fromCharCode(e.which);
		if(correo.indexOf(caracter) < 0)
			return false;
	})
}); 

   