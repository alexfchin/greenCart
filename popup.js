document.addEventListener('DOMContentLoaded', function() {
		var link = document.getElementById('button');
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
