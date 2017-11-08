////////////////////////////////////////////////////////
//                                                    //
//       CompuSoft - The Compushow 2017 Software      //
//                                                    //
////////////////////////////////////////////////////////
//                                                    //
//  		    Base Javascript of header.  		  //
//                                                    //
////////////////////////////////////////////////////////

$(function() {
	
	$("body").on('keyup', "#ch-pswd-1", function() {
		if ($('#ch-pswd-1').val() == $('#ch-pswd-2').val()) {
			$('#pswd-group-2').removeClass('has-error');
			$('#pswd-group-2').addClass('has-success');
		} else { 
			$('#pswd-group-2').removeClass('has-success');
			$('#pswd-group-2').addClass('has-error');
		}
	});

	$("body").on('keyup', "#ch-pswd-2", function() {
		if ($('#ch-pswd-1').val() == $('#ch-pswd-2').val()) {
			$('#pswd-group-2').removeClass('has-error');
			$('#pswd-group-2').addClass('has-success');
		} else { 
			$('#pswd-group-2').removeClass('has-success');
			$('#pswd-group-2').addClass('has-error');
		}
	});

	$("body").on('click', "#ch-pswd-btn", function(e) {

		e.preventDefault();

		if ($('#ch-pswd-1').val() != $('#ch-pswd-2').val()) {
			return false;
		}
		
		// POST csrf token
		var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
		$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});

		$.ajax({
			type: 'POST',
			url: '/pswd/',
			async: false,
			data: {
				'new_pswd':$('#ch-pswd-1').val(),
			},
			success: function (data) {		
				$('#ch-pswd-1').val("");
				$('#ch-pswd-2').val("");
				$('#pswdModal').modal('toggle');
				$('#successfulUpdPswdModal').modal('toggle');
			}
		});

		e.stopImmediatePropagation();
		return false;
	});

});