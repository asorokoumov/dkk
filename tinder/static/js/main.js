/**
 * jTinder initialization
 */
$("#tinderslide").jTinder({
	// dislike callback
    onDislike: function (item) {
	    // set the status text
        if (item.index() == 0)
            window.location.replace("thankyou");
        var car_nr = item.attr('id');
        $.ajax({
			  url: "dislike/"+car_nr,
			});
    },
	// like callback
    onLike: function (item) {
	    // set the status text
        if (item.index() == 0)
            window.location.replace("thankyou");
        var car_nr = item.attr('id');

        $.ajax({
			  url: "like/"+car_nr,
			});

    },
	animationRevertSpeed: 200,
	animationSpeed: 300,
	threshold: 1,
	likeSelector: '.like',
	dislikeSelector: '.dislike'
});

/**
 * Set button action to trigger jTinder like & dislike.
 */
$('.actions .like, .actions .dislike').click(function(e){
	e.preventDefault();
	$("#tinderslide").jTinder($(this).attr('class'));
});