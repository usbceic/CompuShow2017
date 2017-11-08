////////////////////////////////////////////////////////
//                                                    //
//       CompuSoft - The Compushow 2017 Software      //
//                                                    //
////////////////////////////////////////////////////////
//                                                    //
//  	  - Animation for sliding in elements.  	  //
//                                                    //
////////////////////////////////////////////////////////


$(function() {

	$(window).scroll(function() {
		$(".slideanim").each(function(){
			var pos = $(this).offset().top;

			var winTop = $(window).scrollTop();
			if (pos < winTop + 700) {
				$(this).addClass("slide");
			}
		});
	});

});