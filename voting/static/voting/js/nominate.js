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

var warningCartoon = '<div class="alert alert-danger alert-dismissable fade in"\
				style="margin:0;margin-bottom:20px;">\
				<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>\
				<strong>Error:</strong> Ingrese nombre de la caricatura.\
				</div>';

var studentID1;
var studentID2;
var comment;
var cartoon;
var curCategories = {};
var category,category2;


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


$(document).ready(function() {

	// Get information of user to be nominated
	$(".btn-nominate").on('click', function(e) {

		e.preventDefault();

		this_btn    =  $(this);
		category    =  $(this).val();

		if(category !== "") {

			category2   =  $(this).val();
			studentID1  = ($(this).siblings(".nominate-form")).find(".text-input-1").val();
			studentID2  = ($(this).siblings(".nominate-form")).find(".text-input-2").val();
			comment     = ($(this).siblings(".nominate-form")).find(".text-input-3").val();
			cartoon     = ($(this).siblings(".nominate-form")).find(".text-input-4").val();

		} else {

			category    =  $(this).parent().parent().attr('id');
			category2   =  $(this).parent().parent().attr('id');
			studentID1  = ($(this).siblings(".p-nominee")).text();

			if(($(this).siblings(".p-nominee2")).length) {
				studentID2  = ($(this).siblings(".p-nominee2")).text();
			} else {
				studentID2  = undefined;
			}

			comment     = ($(this).siblings(".p-comment")).text();

			if(($(this).siblings(".p-cartoon-outer")).length) {
				cartoon  = ($(this).siblings(".p-cartoon-outer").children(".p-cartoon")).text();
			} else {
				cartoon  = undefined;
			}
		}

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

		if( cartoon === "" ) {
			$(this).parents(".form-nominate").prepend(warningCartoon);
			($(this).siblings(".nominate-form")).find(".text-input-4").select();
			return false;
		}

		if( category === "CompuMaster" || category === "CompuAdoptado" || category === "CompuTeam" ) {
			studentID1 = studentID1.replace(/[^A-Za-z0-9-_:.]/g,"_");
		}

		$.ajax({
			type: 'GET',
			url: '/info/',
			async: false,
			data: {
				'category':category,
				'studentID':studentID1,
				'studentID2':studentID2,
				'comment':comment,
				'cartoon':cartoon,
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

					if( category === "CompuMaster" || category === "CompuAdoptado" || category === "CompuTeam" ) {
						studentID1 = studentID1.replace(/_/g, ' ');
					}

        			$('#modal-body-nominate').html(
        				"<p><span class='text-success'>Nominar</span> a:</p>"
        				+"<p><strong>"+studentID1+"</strong></p>");

					if(data.carnet !== "") {
						$('#modal-body-nominate').append("<p><strong>"+data.carnet+"</strong></p>");
					}

					if(studentID2 !== undefined) {
						$('#modal-body-nominate').append("y</p>"
							+"<p><strong>"+studentID2+"</strong></p>"
							+"<p><strong>"+data.carnet2+"</strong></p>");
					}

					if(cartoon !== undefined) {
						$('#modal-body-nominate').append(
							"<p>como la caricatura:</p>"
							+"<p><strong>"+cartoon+"</strong></p>");
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
					$(".make-nomination-btn").on('click', function(e) {

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

						if( category === "CompuMaster" || category === "CompuAdoptado" || category === "CompuTeam" ) {
							studentID1 = studentID1.replace(/[^A-Za-z0-9-_:.]/g,"_");
						}

						$.ajax({
							type: 'POST',
							url: '/make_nomination/',
							async: false,
							data: {
								'category':category,
								'studentID':studentID1,
								'studentID2':studentID2,
								'comment':comment,
								'cartoon':cartoon,
							},
							success: function (data) {

								data = JSON.parse(data);

								if( category === "CompuMaster" || category === "CompuAdoptado" || category === "CompuTeam" ) {
									studentID1 = studentID1.replace(/_/g, ' ');
								}

								if(data.nomineeOpt_entity === null) {
									data.nomineeOpt_entity = "None";
								}

								if(data.cartoon === null) {
									data.cartoon = "None";
								}

								if($('#'+category+'-nominations-title').length === 0 && !(category in curCategories)) {
									$('#'+category + '> div').append(
										`<button id="${ category }-nominations-title" data-open="${category.name}-nom" class="nominations-title btn btn-info category-nominations cat-item slideanim">
											Mis nominaciones
										</button>`
									);
									curCategories[category] = true;
								}

								$('#'+category).append(
									'<div id="'+category+'-nominations-'+data.nominee_entity+'-'+data.nomineeOpt_entity+'" class="cat-item box-nominate slideanim">'
								);

								$('#'+category+'-nominations-'+data.nominee_entity+'-'+data.nomineeOpt_entity).append(
									'<button type="button" class="close btn-close btn-nominate new-btn-nominate">'
									+'<small><span class="glyphicon glyphicon-edit"></span></small>'
									+'</button>'
								).button();

								$('#'+category+'-nominations-'+data.nominee_entity+'-'+data.nomineeOpt_entity).append(
									'<p class="p-nominee">'+studentID1+'</p>'
								);

								if(data.carnet !== null) {
									$('#'+category+'-nominations-'+data.nominee_entity+'-'+data.nomineeOpt_entity).append(
										'<p>'+data.carnet+'</p>'
									);
								}

								if(data.nomineeOpt_entity !== "None") {
									$('#'+category+'-nominations-'+data.nominee_entity+'-'+data.nomineeOpt_entity).append(
										'<p>y</p>'
										+'<p class="p-nominee2">'+studentID2+'</p>'
									);
								}

								if(data.carnet2 !== null) {
									$('#'+category+'-nominations-'+data.nominee_entity+'-'+data.nomineeOpt_entity).append(
										'<p>'+data.carnet2+'</p>'
									);
								}

								if(data.cartoon !== "None") {
									$('#'+category+'-nominations-'+data.nominee_entity+'-'+data.nomineeOpt_entity).append(
										'<p class="p-cartoon-outer">Carticatura: <span class="p-cartoon">'+data.cartoon+'</span></p>'
									);
								}

								if(data.comment !== "") {
									$('#'+category+'-nominations-'+data.nominee_entity+'-'+data.nomineeOpt_entity).append(
										'<p class="p-comment"><em>'+data.comment+'</em></p>'
									);
								} else {
									$('#'+category+'-nominations-'+data.nominee_entity+'-'+data.nomineeOpt_entity).append(
										'<p class="p-comment">Sin comentarios adicionales.</p>'
									);
								}

								$('#'+category).append(
									'</div>'
								);

								$('#nominateModal').modal('toggle');
								$('#successfulNominationModal').modal('toggle');

							}
						});

						e.stopImmediatePropagation();
						return false;
					});
				}


				else if (data.already_nominated) {

					if( category === "CompuMaster" || category === "CompuAdoptado" || category === "CompuTeam" ) {
						studentID1 = studentID1.replace(/_/g, ' ');
					}

        			$('#modal-body-alreadynominated').html(
        				"<p>Ya has <span class='text-success'><u>Nominado</u></span> a:</p>"
        				+"<p><strong>"+studentID1+"</strong></p>");

					if(data.carnet !== "") {
						$('#modal-body-alreadynominated').append("<p><strong>"+data.carnet+"</strong></p>");
					}

					if(studentID2 !== undefined) {
						$('#modal-body-alreadynominated').append("<p>y</p>"
							+"<p><strong>"+studentID2+"</strong></p>"
							+"<p><strong>"+data.carnet2+"</strong></p>");
					}

					if(cartoon !== undefined) {
						$('#modal-body-alreadynominated').append("<p>como:</p>"
							+"<p><strong>"+data.cartoon+"</strong></p>");
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

						if( category === "CompuMaster" || category === "CompuAdoptado" || category === "CompuTeam" ) {
							studentID1 = studentID1.replace(/[^A-Za-z0-9-_:.]/g,"_");
						}

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

								if(studentID2 == undefined) {
									$('#'+category+'-nominations-'+data.nominee_entity+'-None').remove();
								} else {
									$('#'+category+'-nominations-'+data.nominee_entity+'-'+data.nomineeOpt_entity).remove();
								}

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


});