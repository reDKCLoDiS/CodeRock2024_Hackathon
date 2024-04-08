document.addEventListener("DOMContentLoaded", function() {
    var toggleStocks = document.getElementById('toggleStocks');
    var stockList = document.querySelector('.manufacturerStockSelector ul');

    var isOpen = false; 
    if(toggleStocks){
        toggleStocks.addEventListener('click', function(event) {
            if (!isOpen===true) { 
                stockList.style.display = 'block';
                isOpen = true; 
            } else {
                stockList.style.display = 'none';
                isOpen = false;
            }
        });
    }
    
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.manufacturerStockSelector')) {
            if (isOpen) { 
                stockList.style.display = 'none';
                isOpen = false; 
            }
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var userLabel = document.getElementById('userLabel');
    var manufacturerLabel = document.getElementById('manufacturerLabel');
    var underline = document.getElementById('underline');
    var navInputManufacturerStock = document.querySelector('.nav__inputManufacturerStock');

    underline.style.width = userLabel.offsetWidth + 'px';
    underline.style.left = userLabel.offsetLeft + 'px';

    userLabel.addEventListener('click', function() {
      underline.style.width = userLabel.offsetWidth + 'px';
      underline.style.left = userLabel.offsetLeft + 'px';
      navInputManufacturerStock.style.visibility="hidden";
    });
  
    manufacturerLabel.addEventListener('click', function() {
      underline.style.width = manufacturerLabel.offsetWidth + 'px';
      underline.style.left = manufacturerLabel.offsetLeft + 'px';
      navInputManufacturerStock.style.visibility="visible";
    });
  });




