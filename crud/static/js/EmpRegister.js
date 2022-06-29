
//EmpRegister
$(function() 
{
    $("#btnEnviar").click(function()
    {
    let nombre = $("#name").val();
    let run = $("#run").val();
    let dv = $("#dv").val();
    let email = $("#email").val();
    let contraseña = $("#password").val();

    
    if(!nombre)
    {
    alert("Debe especificar el nombre");
            $("#name").focus();
            return false;
    }        
    else if(!run)
    {
        alert("Debe especificar el run");
        $("#run").focus();
        return false;
        
    }

    else if(!dv)
    {
        alert("Debe especificar el digito verificador");
        $("#dv").focus();
        return false;
        
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
    let letras = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM ÁÉÍÓÚáéíóú.-_';
    $("#name").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })

    let numeros = '0123456789';
    $("#run").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;

    })
    
    let dv = '0123456789Kk';
    $("#dv").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(dv.indexOf(caracter) < 0)
            return false;
    })
    
}); 
