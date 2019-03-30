var brand = document.getElementById('bylineInfo').innerHTML;
var name = document.getElementById('productTitle').innerHTML;
var image = document.getElementById('landingImage').src;
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    console.log(sender.tab ?
                "from a content script:" + sender.tab.url :
                "from the extension");
    if (request.greeting == "hello")
      sendResponse({productBrand: brand, productName: name, productImage: image});
  });
