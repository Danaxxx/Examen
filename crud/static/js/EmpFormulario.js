
//EmpFormulario
$(function() // public static void main (JAVa)
{
    $("#btnEnviar").click(function()
    {
    let idProducto = $("#idProducto").val();
    let nombre = $("#txtNombre").val();
    let txtCantidad = $("#txtCantidad").val();
    let descripcion = $("#descripcion").val();
    let precioNeto = $("#precioNeto").val();
    let precioTotal = $("#precioTotal").val();
    
    if(!idProducto)
    {
        alert("Debe especificar el id del producto");
        $("#idProducto").focus();
        return false;
        
    }
    
    else if(!nombre)
    {
        alert("Debe especificar el nombre del producto");
        $("#txtNombre").focus();
        return false;
        
    }
    
    else if(!txtCantidad)
    {
        alert("Debe especificar la cantidad del producto");
        $("#txtCantidad").focus();
        return false;
        }
    else if(!descripcion)
    {
        alert("Debe especificar la descripcion del producto");
        $("#txtCantidad").focus();
        return false;
        
    }
    else if(!precioNeto)
    {
        alert("Debe especificar el precio neto");
        $("#precioNeto").focus();
        return false;
        
    }
    
    else if(!precioTotal)
    {
        alert("Debe especificar el precio total ");
        $("#precioTotal").focus();
        return false;
        
    }
    });


    function resetform() {
    $("form select").each(function() { this.selectedIndex = 0 });
    $("form input[type=text] , form textarea").each(function() { this.value = '' });
    }



    let numeros = '0123456789';
    //ID PRODUCTOR
    $(".idProducto").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    //CANTIDAD
    $(".txtCantidad").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    //DESCRIPCION
    $(".descripcion").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(descripcion.indexOf(caracter) < 0)
            return false;

    })
    //PRECIO NETO
    $(".precioNeto").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    //PRECIO TOTAL
    $(".precioTotal").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    let letras = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM ÁÉÍÓÚáéíóú';
    let descripcion = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM ÁÉÍÓÚáéíóú1234567890,-';
    $(".txtNombre").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })

}); // cierre
  