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
	
	// Get information of vote
	$(".custom-a").one('click', function(e) {

		e.preventDefault();

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
			success: function (data) {
        		
				data = JSON.parse(data)

				

			}	
		});	
	});

	
});