window.onload = function(){
	updateEvents();
}

function showEvents(content) {
	console.log(content);

	var events_div = document.getElementById('events');
	events_div.innerHTML = '';

	for (let i=0; i<content.length; i++) {
		console.log(content[i]);

		var event_div = document.createElement('div');
		event_div.classList.add('event');

		var type = document.createElement('h1');
		type.innerHTML = content[i].type;
		event_div.appendChild(type);

		var date = document.createElement('h3');
		date.innerHTML = content[i].datetime;
		event_div.appendChild(date);

		var body = document.createElement('p');
		body.innerHTML = content[i].content.type;
		event_div.appendChild(body);

		events_div.appendChild(event_div);
	}
}

function updateEvents(){
	getEvents();
}

function getEvents()
{
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.onreadystatechange = function() { 
		if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
			showEvents(JSON.parse(xmlHttp.responseText));
	}
	xmlHttp.open("GET", "/api/v1/events", true); // true for asynchronous 
	xmlHttp.send(null);
}