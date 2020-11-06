// **** GrandPy page
// Get the input field
//var userInput = document.getElementById("adresse").value;

// Execute function when the user releases ENTER key on the keyboard
//userInput.addEventListener.on("keyup", function(event) {
	// Number 13 is the "Enter" key on the keyboard
	///if (event.keyCode === 13) {
//		userInput.target.value
	//	document =addDiscussion;
//	}
//
//function addDiscussion(event) {

//}

//userInput.submit();

const input = document.getElementById("adresse");
const log = document.getElementById("values");

input.addEventListener('click', function(e){
	console.log("e.target.value")
});

/*const myForm = document.getElementById("myForm");
myForm.addEventListener("submit", (e) => {
	e.preventDefault();
	console.log("Form submitted");
})*/


//input.addEventListener('input', updateValue);

//input.onkeypress = logKey;
//function logKey(e) {
//	log.textContent += '${e.code}';
//}
//function updateValue(e) {
//	log.textContent = e.target.value;
//}

// **** Google Maps
let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}