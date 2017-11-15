////////////////////////////////////////////////////////
//                                                    //
//       CompuSoft - The Compushow 2017 Software      //
//                                                    //
////////////////////////////////////////////////////////
//                                                    //
//  - Voting page javascript						  //
//                                                    //
////////////////////////////////////////////////////////

var studentID;
var studentName;
var studentIDOpt;
var studentNameOpt;
var extra;
var cartoon;
var category;

$(document).ready(function(){
	category = $(".category-title").text()
});

$(document).on('click', '.custom-a', function() {
	
	studentName    = ($(this).children(".nominee-name")).text();
	studentID      = ($(this).children(".nominee-carnet")).text();
	studentNameOpt = ($(this).children(".nominee-nameOpt")).text();
	studentIDOpt   = ($(this).children(".nominee-carnetOpt")).text();
	extra        = ($(this).children(".nominee-extra")).text().replace(/[^A-Za-z0-9-_:.]/g,"_");
	cartoon      = ($(this).children(".nominee-cartoon")).text().replace(/[^A-Za-z0-9-_:.]/g,"_");

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
        		
	data = JSON.parse(data)

	$('#modal-header-vote').html(
		"<p class='h2 text-center' style='color:white;'>"+category+"</p>"
	);

	// Clean modal
	$('#modal-body-vote-info').html("");

	if(studentName !== "") {        			
		$('#modal-body-vote-info').append("<p><strong>"+studentName+"</strong></p>");
	}

	if(studentID !== "") {        			
		$('#modal-body-vote-info').append("<p><strong>"+studentID+"</strong></p>");
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

	$('#voteModal').modal('toggle');
}
