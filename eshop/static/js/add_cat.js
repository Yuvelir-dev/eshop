
function add_cat() {
    // body...

    $.ajax({
        beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));},
        type: "POST",
        url: "/add_cat/",
        data:{categories_title: $( "#categories_title" ).val(),
              id_cat: $( "#id_cat option:selected" ).val(),},

        success: function(data){ Swal.fire('Добавлено!');},
      })
}
  


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');