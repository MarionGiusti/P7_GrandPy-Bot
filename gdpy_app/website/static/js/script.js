// **** GrandPy page

var $map = $('#map');
var $img_pybot = $('#pybot');
$map.hide();


$(document).ready(function(){
	$('form').on('submit', function(event) {
		event.preventDefault();
		// Get the input field
		var userInput = $('#adresse');
		$.ajax({
			data: {
				userInput : $('#adresse').val(),
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
			// Empty the search field of the form
			$('#adresse').val('');
			// Set the message of GrandPy. First one for the address.
			var first_message = data.firstAnswerGdPy + ' ' + data.adress_formatted;
			// and second one for the description.
			var second_message = data.secondAnswerGdPy + ' ' + data.description_wiki;
			var message;

			/* Function to create the message of the user in order to
			have the historic of the discussion between the user and
			GrandPy */
			function new_mess_user(){
				/* Create new elements in the result element.
				Element p to have only "User :" print in a special font-family.
				Element span to have the user input print in a other font-family.
				*/
				var user = document.createElement("p");
				user.setAttribute("id", "user");
				user.appendChild(document.createTextNode('User: '));
				var user_mess = document.createElement("span");
				user_mess.setAttribute("id", "user_mess");
				user_mess.append(data.userQuery);
				user.append(user_mess);
				var result = document.getElementById("result");
				result.append(user);
				// Set the font-family the answer of GrandPy
				$('span#user_mess:last').css({'font-family': 'quicksandlight'});
				$('p#user:last').css({'font-family': 'Black_jackregular'});
				
			};

			function new_mess_gdpy(){
				/* Create new elements in the result element.
				Element p to have only "GrandPy :" print in a special font-family.
				Element span to have the answer of GrandPy print in a other font-family.
				*/
				var gdpy = document.createElement("p");
				gdpy.setAttribute("id", "gdpy");
				gdpy.appendChild(document.createTextNode('GrandPy: '));
				var gdpy_mess = document.createElement("span");
				gdpy_mess.setAttribute("id", "gdpy_mess");
				gdpy_mess.append(message);
				gdpy.append(gdpy_mess);		
				var result = document.getElementById("result");
				result.append(gdpy);
				// Set the font-family the answer of GrandPy
				$('span#gdpy_mess:last').css({'font-family': 'quicksandlight'});
				$('p#gdpy:last').css({'font-family': 'Black_jackregular'});
			};

			new_mess_user();

			// Change the image of GrandPy when user input submitted.
			$img_pybot.attr('src', 'static/img/pybothmm.png');
			$img_pybot.css({'transform': 'rotate(0deg)'});	

			/* Delate the first answer of GrandPy*/
			setTimeout(function(){	
				message = first_message;
				new_mess_gdpy();
				// Show the map from GoogleMaps
				$map.show();
			}, 1000);

			initMap(data.latitude, data.longitude);

			/* Display the second message of GrandPy only if the call of API Googlemaps
			 found a place */
			if (data.found_place = true) {
				setTimeout(function(){
				message = second_message;
				new_mess_gdpy();
				// Add a new element to have the link of the wikipedia url.
				var link_wiki = document.createElement("a");
				link_wiki.setAttribute('href', data.url_wiki);
				link_wiki.append( ' [Jette un oeil sur Wikipédia]');
				$('span#gdpy_mess:last').append(link_wiki);
				$("a").attr('target', '_blank');
				},3000);
			}
						
		});
	});
	
});


// *********************//
// **** Google Maps ****//
// *********************//

function initMap(latitude, longitude) {
	// Location
	const location = {lat: latitude, lng: longitude};
	// Map centered at location
	const map = new google.maps.Map(document.getElementById("map"), {
    center: location,
    zoom: 12,
    });
    // Marker positioned at location
    const marker = new google.maps.Marker({
    	position: location,
    	map: map,
    });
}