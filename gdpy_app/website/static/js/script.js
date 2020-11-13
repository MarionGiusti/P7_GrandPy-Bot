// **** GrandPy page








//function displayUserInput() {
	// Add a new value to the paragraphe with the id="dialog", to display dialog with PyBot
//	.append
//});


$(document).ready(function(){
	$('form').on('submit', function(event) {
		event.preventDefault();
		// Get the input field
		var userInput = $('#adresse');
		// console.log('hello', userInput.val());
		$.ajax({
			data: {
				userInput : $('#adresse').val()
			},
			type : 'POST',
			url : '/process',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		})
		.done(function(data) {
			// $('#result').text(data.result).show();
			$('#result').append('</br>' + data.result).show();
		});

	});
});



// *********************//
// **** Google Maps ****//
// *********************//

var map;

function initMap(latitude, longitude) {
  map = new google.maps.Map(document.getElementById("map"), {
    // center: { lat: -34.397, lng: 150.644 },
    center: { lat: latitude, lng: longitude },
    zoom: 8,
  });
}