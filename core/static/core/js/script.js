$(document).ready(function(){
	
	// Adds the highlight in the nav
    $('nav ul li a').each(function(index) {
        if(this.href.trim() == window.location)
            $(this).parent().addClass("active");
    });
    $('ul.a-z-list li a').each(function(index) {
        if(this.href.trim() == window.location)
            $(this).parent().addClass("selected");
    });
    $('ul.film-side-bar li a').each(function(index) {
        if(this.className == document.body.id)
            $(this).parent().addClass("selected");
    });
	
	//Opens mailing list modal with URL
  if(window.location.href.indexOf('#mailing-form') != -1) {
    $('#mailing-modal').modal('show');
  }
    	
	// Makes an element square
	var width = $(".square").innerWidth();
	$('.square').css('height', width);
	$(window).resize(function() {
	    var width = $(".square").innerWidth();
	    $('.square').css('height', width);
	});
	
	// Makes an element 16:9
	var width = $(".sixteen-nine").innerWidth()/16;
	$('.sixteen-nine').css('height', width*9);
	$(window).resize(function() {
	    var width = $(".sixteen-nine").innerWidth()/16;
	    $('.sixteen-nine').css('height', width*9);
	});
	
	// Makes bubbles always round
	var width = $(".bubble").innerWidth();
	$('.bubble').css('height', width);
	$(window).resize(function() {
	    var width = $(".bubble").innerWidth();
	    $('.bubble').css('height', width);
	});
	var width = $(".bubble2").innerWidth();
	$('.bubble2').css('height', width);
	$(window).resize(function() {
	    var width = $(".bubble2").innerWidth();
	    $('.bubble2').css('height', width);
	});		
});

$(document).delegate('*[data-toggle="lightbox"]', 'click', function(event) {
    event.preventDefault();
    $(this).ekkoLightbox();
});