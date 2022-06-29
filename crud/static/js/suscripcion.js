$(function()
{
    $("#btnGrabar").click(function()
    {
        let run = $(".txtRun").val();
        let dv = $(".txtDv").val();
        let nombre = $(".txtNombre").val();
        let apellido = $(".txtApellido").val();
        let email = $(".txtEmail").val();   
        let celular = $('.txtCelular').val();
        let donacion = $('.txtDonacion').val();
        let activo = $(".chkActivo").val();
        
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
   	    else if(!nombre){
            alert("Debe especificar su nombre");
            $(".txtNombre").focus();
            return false;
        }
        else if(nombre.length<1){
            alert("El nombre de usuario debe tener como minimo 1 caracter")
            $(".txtNombre").focus();
            return false;
        }
   	    else if(!apellido){
            alert("Debe especificar su apellido");
            $(".txtApellido").focus();
            return false;
        }
        else if(apellido.length<1){
            alert("El apellido debe tener como minimo 1 caracter")
            $(".txtApellido").focus();
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

   	    else if(!celular){
            alert("Debe especificar su celular");
            $(".txtCelular").focus();
            return false;
        }
        else if(celular.length<11){
            alert("El numero debe cumplir el formato 56912345678 (11 dígitos)")
            $(".txtCelular").focus();
            return false;
        }

        else{
            alert("Suscripcion registrada con éxito")
        }
    });
    let numeros = '1234567890';
    $(".txtRun").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    $(".txtDonacion").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    $(".txtCelular").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    let letras = "qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ1234567890'._@";
    $(".txtNombre").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })
    $(".txtApellido").keypress(function(e)
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
