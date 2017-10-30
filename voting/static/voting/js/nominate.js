////////////////////////////////////////////////////////
//                                                    //
//       CompuSoft - The Compushow 2017 Software      //
//                                                    //
////////////////////////////////////////////////////////
//                                                    //
//  - Jquery to process nomination forms without	  //
//	  reloading page.  		  						  //
//                                                    //
////////////////////////////////////////////////////////

var warning = 	'<div class="alert alert-danger alert-dismissable fade in"\
				style="margin:0;margin-bottom:20px;">\
				<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>\
				<strong>Error:</strong> Ingrese nombre de la persona.\
				</div>';

var warning2 = 	'<div class="alert alert-danger alert-dismissable fade in"\
				style="margin:0;margin-bottom:20px;">\
				<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>\
				<strong>Error:</strong> Nombre inválido. Escoja nombre de la lista.\
				</div>';

var studentID1;
var studentID2;
var comment;
var category,category2;

$(function() {

	// Remove slide in effect from first category
	$("#CompuCono .cat-item").removeClass("slideanim");	

	// Add smooth scrolling to all links in category navbar
	$(".nav-categories li a").on('click', function(event) {
		// Make sure this.hash has a value before overriding default behavior
		if (this.hash !== "") {
		// Prevent default anchor click behavior
		event.preventDefault();
		// Store hash
		var hash = this.hash;
    	// Using jQuery's animate() method to add smooth page scroll
    	// The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
		$('html, body').animate({
			scrollTop: $(hash).offset().top
		}, 1500, function(){
    		// Add hash (#) to URL when done scrolling (default click behavior)
			window.location.hash = hash;
			});
		} // End if
	});

	// Get information of user to be nominated
	$(".btn-nominate").click(function(e) {

		e.preventDefault();

		this_btn    =  $(this);
		category    =  $(this).val();
		category2   =  $(this).val();
		studentID1  = ($(this).siblings(".nominate-form")).find(".text-input-1").val();
		studentID2  = ($(this).siblings(".nominate-form")).find(".text-input-2").val();
		comment     = ($(this).siblings(".nominate-form")).find(".text-input-3").val();

		// Validate non empty input
		if( studentID1 === "" ) {
			$(this).parents(".form-nominate").prepend(warning);
			($(this).siblings(".nominate-form")).find(".text-input-1").select();
			return false;
		}

		if( studentID2 === "" ) {
			$(this).parents(".form-nominate").prepend(warning);
			($(this).siblings(".nominate-form")).find(".text-input-2").select();
			return false;
		}

		$.ajax({
			type: 'GET',
			url: '/info/',
			async: false,
			data: {
				'category':category,
				'studentID':studentID1,
				'studentID2':studentID2,
				'comment':comment
			},
			success: function (data) {
        		
				data = JSON.parse(data)

				if(data.not_found) {
					this_btn.parents(".form-nominate").prepend(warning2);
					(this_btn.siblings(".nominate-form")).find(".text-input-1").select();
					return false;

				} 
				else if(data.not_found_2) {
					this_btn.parents(".form-nominate").prepend(warning2);
					(this_btn.siblings(".nominate-form")).find(".text-input-2").select();
					return false;

				} 



				else if(data.nominate) {

        			$('#modal-body-nominate').html(
        				"<p><span class='text-success'>Nominar</span> a:</p>"
        				+"<p><strong>"+studentID1+"</strong></p>");

					if(data.carnet !== "") {        			
						$('#modal-body-nominate').append("<p><strong>"+data.carnet+"</strong></p>");
					}

					if(studentID2 !== null) {
						$('#modal-body-nominate').append("y</p>"
							+"<p><strong>"+studentID2+"</strong></p>"
							+"<p><strong>"+data.carnet2+"</strong></p>");
					}

        			$('#modal-body-nominate').append(
        				"<p>para la categoría de:</p>"
        				+"<p><strong>"+data.category+"</strong></p>"
        				+"<p>Comentario:</p>");

        			if(data.comment === "") {
        				$('#modal-body-nominate').append("<p>No tienes comentarios.</p>");
        			} else {
        				$('#modal-body-nominate').append('<p><em>"'+data.comment+'"</em></p>');
        			}

        			$('#nominateModal').modal('toggle');

        			// Make nomination
					$(".make-nomination-btn").click(function(e) {

						e.preventDefault();

						// Safe post method
						var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
						
						function csrfSafeMethod(method) {
						    // these HTTP methods do not require CSRF protection
						    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
						}
						$.ajaxSetup({
						    beforeSend: function(xhr, settings) {
						        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
						            xhr.setRequestHeader("X-CSRFToken", csrftoken);
						        }
						    }
						});

						$.ajax({
							type: 'POST',
							url: '/make_nomination/',
							async: false,
							data: {
								'category':category,
								'studentID':studentID1,
								'studentID2':studentID2,
								'comment':comment,
							},
							success: function (data) {
					        		
								data = JSON.parse(data);
						
								$('#nominateModal').modal('toggle');
								$('#successfulNominationModal').modal('toggle');

							}
						});

						e.stopImmediatePropagation();
						return false;
					});
				}


				else if (data.already_nominated) {
        			$('#modal-body-alreadynominated').html(
        				"<p>Ya has <span class='text-success'><u>Nominado</u></span> a:</p>"
        				+"<p><strong>"+studentID1+"</strong></p>");

					if(data.carnet !== "") {        			
						$('#modal-body-alreadynominated').append("<p><strong>"+data.carnet+"</strong></p>");
					}

					if(studentID2 !== null) {
						$('#modal-body-alreadynominated').append("y</p>"
							+"<p><strong>"+studentID2+"</strong></p>"
							+"<p><strong>"+data.carnet2+"</strong></p>");
					}

					$('#modal-body-alreadynominated').append(
        				 "<p>para la categoría de:</p>"
        				+"<p><strong>"+data.category+"</strong></p>"
        				+"<p>Comentario:</p>")
        			
        			if(data.comment === "") {
        				$('#modal-body-alreadynominated').append("<p>No tienes comentarios.</p>");
        			} else {
        				$('#modal-body-alreadynominated').append('<p><em>"'+data.comment+'"</em></p>');
        			}

        			$('#alreadyNominatedModal').modal('toggle');	

        			// Eliminate nomination
					$(".eliminate-nomination-btn").click(function(e) {
					
						e.preventDefault();

						$.ajax({
							type: 'GET',
							url: '/delete_nomination/',
							async: false,
							data: {
								'category':category,
								'studentID':studentID1,
								'studentID2':studentID2,
							},
							success: function (data) {
					        		
								data = JSON.parse(data);
						
								$('#alreadyNominatedModal').modal('toggle');
								$('#deletedNominationModal').modal('toggle');
							}
						});

						e.stopImmediatePropagation();
						return false;
					});		
				}
			}
		});	
		e.stopImmediatePropagation();
		return false;
	});

	$(".btn-close").click(function(e) {

	});
});