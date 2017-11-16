////////////////////////////////////////////////////////
//                                                    //
//       CompuSoft - The Compushow 2017 Software      //
//                                                    //
////////////////////////////////////////////////////////
//                                                    //
//  - Voting page javascript						  //
//                                                    //
////////////////////////////////////////////////////////

var nomineeID;
var studentID;
var studentName;
var studentIDOpt;
var studentNameOpt;
var extra;
var cartoon;
var parentDIV;
var category;
var voted;

$(document).ready(function(){
	category = $(".category-title").text()
	voted = ($('input#voted').val() === "True");
});

$(document).on('click', '.custom-a', function() {

	nomineeID      = ($(this).children(".nominee-id")).val();
	studentName    = ($(this).children(".nominee-name")).text();
	studentID      = ($(this).children(".nominee-carnet")).text();
	studentNameOpt = ($(this).children(".nominee-nameOpt")).text();
	studentIDOpt   = ($(this).children(".nominee-carnetOpt")).text();
	extra          = ($(this).children(".nominee-extra")).text();
	cartoon        = ($(this).children(".nominee-cartoon")).text();
	parentDIV      = $(this).parent();

	$.ajax({
		type: 'GET',
		url: '/voteinfo/',
		async: false,
		data: {
			'category':category,
			'studentID':studentID,
			'studentIDOpt':studentIDOpt,
			'extra':extra,
		},
		success: function(data) {
			displayVote(data);
		}
	});	
	
});

function displayVote(data) {
        		
	data = JSON.parse(data);

	// Clean modal
	$('#modal-body-vote-info').html("");

	$('#modal-body-vote-info').append(
		"<img class='big-image' src='/static/voting/images/NominationImages/"+category+"/"+nomineeID+".jpg'/>"
	);

	if(studentName !== "") {        			
		$('#modal-body-vote-info').append("<p><strong>"+studentName+"</strong></p>");
	}

	if(studentID !== "") {        			
		$('#modal-body-vote-info').append("<p>"+studentID+"</p>");
	}

	if(studentIDOpt !== "") {
		$('#modal-body-vote-info').append("y</p>"
			+"<p><strong>"+studentNameOpt+"</strong></p>"
			+"<p><strong>"+studentIDOpt+"</strong></p>");
	}

	if(cartoon !== "") {
		$('#modal-body-vote-info').append(
			"<p>como la caricatura:</p>"
			+"<p><strong>"+cartoon+"</strong></p>");
	}

	if(extra !== "") {        			
		$('#modal-body-vote-info').append("<p><strong>"+extra+"</strong></p>");
	}

	$('#carousel-inner-modal').html("");

	var N = data.comments.length;
	if(N === 0) {
		$('#carousel-inner-modal').append(
			"<div class='carousel-comment item active'><p class='comment-text'><em>No hay comentarios adicionales.</em></p></div>"
		);
	} else {
		$('#carousel-inner-modal').append(
			"<div class='carousel-comment item active'><p class='comment-text'><em>"+data.comments[0]+"</em></p></div>"
		);
	}

	for(var i = 1; i < N; i++) {
		$('#carousel-inner-modal').append(
			"<div class='carousel-comment item'><p class='comment-text'><em>"+data.comments[i]+"</em></p></div>"
		);
	}

	if(voted) {
		$("#modal-vote-footer").hide();
	} else {
		$("#modal-vote-footer").show();
	}

	$('#voteModal').modal('toggle');
}

// Process voting
$(document).on('click', '.vote-btn', function() {

	// Safe post method
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
		url: '/voting/',
		async: false,
		data: {
			'category':category,
			'studentID':studentID,
			'studentIDOpt':studentIDOpt,
			'extra':extra,
		},
		success: function(data) {
			voted = true;
			parentDIV.append("<span class='label label-success voted text-center slide'>Voto</span>");
			$('#successfulVotingModal').modal('toggle');
		}
	});	
});