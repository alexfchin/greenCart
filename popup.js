let endpoint = "127.0.0.1:5000/company"

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  chrome.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response) {
    document.getElementById('productBrand').textContent=response.productBrand;
    document.getElementById('productName').textContent=response.productName;
    document.getElementById('productImage').src=response.productImage;

    let data = {company: response.productBrand};
    
    fetch(endpoint, {
      method: 'GET',
      body: data,
    }).then(res => {
      resJSON = res.json();
      document.getElementById('ratingGrade').textContent = resJSON.Grade;
      
      if (resJSON.Grade == "A"){
        document.getElementById('ratingIcon').src="images/ratingA.png";
      } else if (resJSON.Grade == "B") {
        document.getElementById('ratingIcon').src="images/ratingB.png";
      } else if (resJSON.Grade == "C") {
        document.getElementById('ratingIcon').src="images/ratingC.png";
      } else if (resJSON.Grade == "D"){
        document.getElementById('ratingIcon').src="images/ratingD.png";
      } else if (resJSON.Grade == "F"){
        document.getElementById('ratingIcon').src="images/ratingF.png";
      }
    }).catch(error => {
      document.getElementById('ratingGrade').textContent = 'n/a';
    });

});
