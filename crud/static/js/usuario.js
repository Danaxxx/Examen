$(function()
{
    $("#btnGrabar").click(function()
    {
        let run = $(".txtRun").val();
        let dv = $(".txtDv").val();
        let nombreusuario = $(".txtNombreUsuario").val();
        let email = $(".txtEmail").val();
        let password = $('.txtPassword').val();
        let tipousuario = $(".ctTipoDeUsuario").val();
        
        if(!run)
        {
            alert("Debe especificar el run");
            $(".run").focus();
            return false;   
        }
        else if(run.length<7){
            alert("El run debe tener como minimo 7 caracteres")
            $(".run").focus();
            return false;
        }
        else if(!dv)
        {
            alert("Debe especificar el digito verificador");
            $(".dv").focus();
            return false;  
        }  
   	    else if(!nombreusuario){
            alert("Debe especificar el nombre del producto");
            $(".txtNombreUsuario").focus();
            return false;
        }
        else if(nombreusuario.length<5){
            alert("El nombre de usuario debe tener como minimo 5 caracteres")
            $(".txtNombreUsuario").focus();
            return false;
        }

   	    else if(!email){
            alert("Debe especificar el e-mail");
            $(".txtEmail").focus();
            return false;
        }

        else if(email.length<8){
            alert("El correo debe tener como minimo 8 caracteres")
            $(".txtEmail").focus();
            return false;
        }
        else if(email.indexOf('@', 0) == -1 || email.indexOf('.', 0) == -1) {
            alert('El correo electrónico introducido no es correcto.');
            return false;
        }

   	    else if(!password){
            alert("Debe especificar la contraseña");
            $(".txtPassword").focus();
            return false;
        }
        else if(password.length<8){
            alert("La contraseña debe tener como minimo 8 caracteres")
            $(".password").focus();
            return false;
        }
        
        else if(tipousuario==0) {
            alert("Debe especificar el tipo de usuario");
            $(".ctTipoDeUsuario").focus();
            return false;
        }

        else{
            alert("Registro existoso!");
        }
    });
    let numeros = '1234567890';
    $(".txtRun").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    let letras = "qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ1234567890'._@";
    $(".txtNombreUsuario").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })
    let dv = '1234567890Kk';
    $(".txtDv").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(dv.indexOf(caracter) < 0)
            return false;
    })

    $(".txtEmail").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;
    })

    $(".txtPassword").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;
    })


});
