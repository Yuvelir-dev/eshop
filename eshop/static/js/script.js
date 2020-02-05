function add_card(id) {
    // body...

    $.ajax({

        type: "GET",
        url: "/card/?id=" + id,
        
    })
    }
