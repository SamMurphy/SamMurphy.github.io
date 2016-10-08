$(document).ready(function(){
	
	var excuses=[
		"I'm ill",
		"I'm tired",
		"I have the plague",
		"I didn't sleep very well",
		"I'm hungover",
		"I'm hungry",
		"I forgot",
		"My alarm didn't go off",
		"I forgot to put down the bathmat, so slipped on the soaking wet floor and broke my neck",
		"I danced to Abba to vigorously and injured my neck",
		"I can't be bothered to go"
	];	

	$('#excuseButton').click(function(evt) {
		//define the containers of the info we target
		var quote = $('#quoteContainer p').text();
		var quoteGenius = $('#quoteGenius').text();
		//prevent browser's default action
		evt.preventDefault();
		//getting a new random number to attach to a quote and setting a limit
		var sourceLength = excuses.length;
		var randomNumber= Math.floor(Math.random()*sourceLength);
		//set a new quote
		var newQuoteText = excuses[randomNumber];
		var name = "Adam Kadowski";
		//console.log(newQuoteText,newQuoteGenius);
   		var timeAnimation = 500;
   		var quoteContainer = $('#quoteContainer');
   		//fade out animation with callback
   		quoteContainer.fadeOut(timeAnimation,
   						       function() {
		   							quoteContainer.html('');
									quoteContainer.append('<p>'+newQuoteText+'</p>'+'<p id="quoteGenius">'+'-								'+name+'</p>');
       								//fadein animation.
       								quoteContainer.fadeIn(timeAnimation);
    							});

	});

});