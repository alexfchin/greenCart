chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
	chrome.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response) {
		document.getElementById('productBrand').textContent=response.productBrand;
		document.getElementById('productName').textContent=response.productName;
	});
});
