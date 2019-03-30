document.addEventListener('DOMContentLoaded', function() {
	let link = document.getElementById('button');
	// onClick's logic below:
	link.addEventListener('click', function() {
		// Chrome tab stuff
		chrome.tabs.getSelected(null, function(tab) {
			var tabId = tab.id;
			var tabUrl = tab.url;

			document.getElementById('productName').textContent=tabUrl;
		});
	});
});

$(document).ready(function() {
	chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
		chrome.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response) {
			document.getElementById('productBrand').textContent=response.productBrand;
			document.getElementById('productName').textContent=response.productName;
		});
	});
});

