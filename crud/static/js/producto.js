$(function()
{
    $("#btnGrabar").click(function()
    {
        let nombreproducto = $(".txtNombre").val();
        let precioproducto = $(".txtPrecioProducto").val();
        let costoproducto = $('.txtPrecioCosto').val();
        let stockproducto = $(".txtStockProducto").val();
        let descripcionproduc = $(".txtDescripcion").val();
        let categoria = $('.ctProducto').val();
        let marca = $('.ctMarca').val();
   	    if(!nombreproducto){
            alert("Debe especificar el nombre del producto");
            $(".txtNombre").focus();
            return false;
        }
        else if(nombreproducto.length < 5){
            alert("El nombre del producto debe tener como minimo 5 caracteres");
            $(".txtNombre").focus();
            return false;
        }
         
        else if(!precioproducto){
            alert("Debe especificar el precio del producto");
            $(".txtPrecioProducto").focus();
            return false;
        }
        else if(precioproducto<500){
            alert("El precio minimo debe ser de 500 pesos");
            $(".txtPrecioProducto").focus();
            return false;
        }
        else if(!costoproducto){
            alert("Debe especificar el costo del producto");
            $(".txtPrecioCosto").focus();
            return false;
        }
        else if(costoproducto<500){
            alert("El precio minimo del costo deber ser de 500 pesos");
            $(".txtPrecioCosto").focus();
            return false;
        }
        else if(!stockproducto){
            alert("Debe especificar el stock del producto");
            $(".txtStockProducto").focus();
            return false;
        }
        else if(stockproducto<1){
            alert("El numero de stock debe ser mayor que 0");
            $(".txtStockProducto").focus();
            return false;
        }

        else if(!descripcionproduc){
            alert("Debe especificar la descripción del producto");
            $(".txtDescripcion").focus();
            return false;
        }
        else if(descripcionproduc.length < 10){
            alert("La descripción del producto debe tener como minimo 10 caracteres");
            $(".txtDescripcion").focus();
            return false;
       
        }
        else if (categoria == '0'){
            alert("Debe especificar la categoria del producto")
            $(".ctProducto").focus();
            return false;
        }
        else if (marca == '0'){
            alert("Debe especificar la marca del producto")
            $(".ctMarca").focus();
            return false;
        }
        else{
            alert("Producto registrado correctamente")
        }
    });
    let numeros = '1234567890';
    $(".txtPrecioProducto").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    let letras = "qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ1234567890'";
    $(".txtNombre").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })
    $(".txtDescripcion").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })
    $(".txtPrecioProducto").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;

    })
    $(".txtPrecioCosto").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;

    })
    $(".txtStockProducto").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;

    })
});
