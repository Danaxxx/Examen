$(function()
{
    $("#btnGrabar").click(function()
    {

        let nombre = $(".txtNombre").val();
        let apellido = $(".txtApellido").val();  
        let donacion = $('.txtMonto').val();
        let tipo = $(".ctMedioPago").val();
        
        
   	    if(!nombre){
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

   	    else if(!donacion){
            alert("Debe registrar su donacion");
            $(".txtMonto").focus();
            return false;
        }

        else if (tipo == '0'){
            alert("Debe especificar medio de pago")
            $(".ctMedioPago").focus();
            return false;
        }

        else{
            alert("Donacion registrada con éxito")
        }
    });
    let numeros = '1234567890';
    $(".txtMonto").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    letras = "qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ1234567890'._@";
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




});
