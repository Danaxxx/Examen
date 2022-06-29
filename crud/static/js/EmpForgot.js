
    //EmpForgot
$(function() 
{
    $(".btnEnviar").click(function()
    {
    let email = $("#email").val();        
    if(!email)
    {
        alert("Debe rellenar este campo");
        $("#email").focus();
    }
    else if(email.length<13){
        alert("El correo electronico debe tener un minimo de 13 caracteres");
    }
    else if($("#email").val().indexOf('@', 0) == -1 || $("#email").val().indexOf('.', 0) == -1){
    alert('El correo electrónico introducido no es correcto.');
    $("#email").focus();
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

      