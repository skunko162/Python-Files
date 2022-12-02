const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'dec13b3ae0msh8251aeec1c5ef34p1b9aa6jsna8f25f22f6ef',
		'X-RapidAPI-Host': 'barcode-generator4.p.rapidapi.com'
	}
};

fetch('https://barcode-generator4.p.rapidapi.com/?text=123456&barcodeType=C128&imageType=PNG', options)
	.then(response => response.json())
	.then(response => console.log(response))
	.catch(err => console.error(err));