
$(function() 
{			
	$(".btnEnviar").click(function()
	{
	let contraseña = $("#password").val();
	let contraseñaN = $("#password-confirm").val();
	if(!contraseña)
		{
			alert("Debe especificar la contraseña");
			$("#password").focus();
		}       
	else if(!contraseñaN)
		{
			alert("Debe especificar nueva contraseña");
			$("#password").focus();
		}       
	})
	});
