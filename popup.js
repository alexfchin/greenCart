chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  chrome.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response) {
    document.getElementById('productBrand').textContent=response.productBrand;
    document.getElementById('productName').textContent=response.productName;
    document.getElementById('productImage').src=response.productImage;


    if (GRADE == "A"){
      document.getElementById('ratingIcon').src="images/ratingA.png";
    }else if (GRADE == "B") {
      document.getElementById('ratingIcon').src="images/ratingB.png";
    }else if (GRADE == "C") {
      document.getElementById('ratingIcon').src="images/ratingC.png";
    }else if(GRADE == "D"){
      document.getElementById('ratingIcon').src="images/ratingD.png";
    }else if (GRADE == "F"){
      document.getElementById('ratingIcon').src="images/ratingF.png";
    }
});
