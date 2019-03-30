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


var bruh = document.getElementsByClassName("a-button-stack");

for (var i = 0; i < bruh.length; i++) {
  setAlert(bruh, i);
}

function setAlert(bruh, i) {
  var element = bruh.item(i);

  element.addEventListener("mouseover", function() {
    if (!element.hasAttribute("warned")) {
      setModal();
      element.setAttribute("warned", true);
    }
  });
}

function setModal() {
  var newestDiv = document.createElement("div");

  newestDiv.setAttribute("id", "greenBasketCover");
  newestDiv.setAttribute("style", "width: 100%; height: 100%; background-color: rgb(0,0,0); opacity: 0.6; z-index: 10000; position: absolute; top: 0;");

  var newDiv = document.createElement("div");

  newDiv.setAttribute("id", "greenBasket");
  newDiv.setAttribute("style", "width:40%; height:40%; background-color:rgb(211,211,211); z-index:1000000; position: absolute; top: 30%; left:30%; border-radius:10px");


  var newerDiv = document.createElement("img");

  newerDiv.setAttribute("id", "greenBasketExit");
  newerDiv.setAttribute("src", "https://image.flaticon.com/icons/svg/32/32178.svg");

  newerDiv.addEventListener("mouseover", function() {
    newerDiv.setAttribute('src', 'https://image.flaticon.com/icons/svg/579/579006.svg');
  });
  newerDiv.addEventListener("mouseout", function() {
    newerDiv.setAttribute('src', 'https://image.flaticon.com/icons/svg/32/32178.svg');
  });
  newerDiv.addEventListener("click", function() {
    document.getElementById('greenBasketCover').remove();
    document.getElementById('greenBasket').remove();
    document.getElementById('greenBasketExit').remove();
  });

  newerDiv.setAttribute("style", "width:2.5%; height:5%; z-index:1000000; position: absolute; top: 0; right:0;");

  document.body.appendChild(newestDiv);
  document.body.appendChild(newDiv);
  document.body.appendChild(newerDiv);
}
