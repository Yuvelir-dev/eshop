
function add_order() {
    // body...

    $.ajax({
        type: "POST",
        url: "/order/",
        data:{
            delivery_method: $( "#delivery_method option:selected" ).text(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
    
        },
        success: function(data){
                if (data == 'invalid payment') { Swal.fire(data)}
                else {stripe.redirectToCheckout({
              // Make the id field from the Checkout Session creation API response
              // available to this file, so you can provide it as parameter here
              // instead of the {{CHECKOUT_SESSION_ID}} placeholder.
              sessionId: data
            }).then(function (result) {
              // If `redirectToCheckout` fails due to a browser or network
              // error, display the localized error message to your customer
              // using `result.error.message`.
            });}

            

}
    })
    };



