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

	$('#modal-body-vote').html(
		"<p><span class='text-success'>Votar</span> por:</p>"
	);

	if(studentName !== "") {        			
		$('#modal-body-vote').append("<p><strong>"+studentName+"</strong></p>");
	}

	if(studentID !== "") {        			
		$('#modal-body-vote').append("<p><strong>"+studentID+"</strong></p>");
	}

	if(studentIDOpt !== "") {
		$('#modal-body-vote').append("y</p>"
			+"<p><strong>"+studentNameOpt+"</strong></p>"
			+"<p><strong>"+studentIDOpt+"</strong></p>");
	}

	if(cartoon !== "") {
		$('#modal-body-vote').append(
			"<p>como la caricatura:</p>"
			+"<p><strong>"+cartoon+"</strong></p>");
	}

	$('#modal-body-vote').append(
		"<p>para la categoría de:</p>"
		+"<p><strong>"+category+"</strong></p>"
		+"<p>Comentario:</p>");

	if("comments" in data) {
		$('#modal-body-vote').append("<p>No tienes comentarios.</p>");
	} else {
		$('#modal-body-vote').append('<p>No tienes comentarios.</p>');
	}

	$('#voteModal').modal('toggle');
}
