//Here starts predefined code for csrf token inclusion in ajax request header
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = $.trim(cookies[i]);
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
function csrfSafeMethod(method) { // these HTTP methods do not require CSRF protection 
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method)); }
$.ajaxSetup({
	beforeSend: function(xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});
//End of the predefined code


$('button').on('click', function(event){
	event.preventDefault();
	var element = $(this);
	$.ajax({
		url : '/access_offer/',
		type : 'POST',
		data : { 'offer_id' : element.attr("data-id")},
		success : function(response){
				
				switch(parseInt(response)) {
				  case 0:
				    $('.hover_bkgr_fricc').show();
				    break;
				  case 4:
				  	alert("Insufficient funds!")
				    break;
				  default:
				    alert("Internal issue, try again later!")
				}

			}
		});
});



$( document ).ready(function() {
    $("#id_type option[value='Undefined']").each(function() {
    	$(this).remove();
	});
	$('.hover_bkgr_fricc').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
    $('.popupCloseButton').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
});