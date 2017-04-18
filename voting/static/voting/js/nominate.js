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
				<strong>Error:</strong> Carnet requerido.\
				</div>';

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
	$(".btn-nominate").click(function() {

		var studentID1 = ($(this).siblings(".nominate-form")).find(".text-input-1").val();
		var studentID2 = ($(this).siblings(".nominate-form")).find(".text-input-2").val();
		var comment = ($(this).siblings(".nominate-form")).find(".text-input-3").val();
		
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
			data: {
				'category':$(this).val(),
				'studentID':studentID1,
				'studentID2':studentID2,
				'comment':comment
			},
			success: function (data) {
        		
				data = JSON.parse(data)

        		if(data.nominate) {
        			$('#nominateModal').modal('show');
				} 
				else if (data.already_nominated) {
        			$('#alreadyNominatedModal').modal('show');
				}
			}
		});
	});

});