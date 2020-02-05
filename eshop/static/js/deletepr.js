function hz(id) {
    // body...

    $.ajax({

        type: "DELETE",
        url: "/order/?id=" + id,

        beforeSend: function(xhr) {
            
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
          
        },
       	success: function(data){
				       		Swal.fire({
				  title: 'Are you sure?',
				  text: "You won't be able to revert this!",
				  icon: 'warning',
				  showCancelButton: false,
				  confirmButtonColor: '#3085d6',
				  cancelButtonColor: '#d33',
				  confirmButtonText: 'OK!'
				}).then((result) => {
				  	document.location.reload(true);
				    
				  
				})
			
       	}
    })
    };
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