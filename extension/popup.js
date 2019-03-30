let endpoint = "127.0.0.1:5000/company"

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
	chrome.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response) {
		document.getElementById('productBrand').textContent=response.productBrand;
		document.getElementById('productName').textContent=response.productName;

		let data = {company: response.productBrand};

		fetch(endpoint, {
			method: 'GET',
			body: data,
		}).then(res => {
			document.getElementById('ratingGrade').textContent = res.json().Grade;
		}).catch(error => {
			document.getElementById('ratingGrade').textContent = 'n/a';
		});
	});
});
