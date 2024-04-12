document.addEventListener("DOMContentLoaded", function () {
  var chooseDelivery = document.getElementById("chooseDelivery");
  var deliveryTypes = document.querySelector(".deliveryTypes ul");
  var deliveryImg = document.querySelector(".chooseDeliveryImg");

  var isOpen = false;
  if (chooseDelivery) {
    chooseDelivery.addEventListener("click", function (event) {
      if (!isOpen === true) {
        deliveryTypes.style.display = "block";
        deliveryImg.classList.add("open")
        isOpen = true;
      } else {
        deliveryTypes.style.display = "none";
        deliveryImg.classList.remove("open")
        isOpen = false;
      }
    });
  }


  document.addEventListener("click", function (event) {
    if (!event.target.closest(".chooseDelivery")) {
      if (isOpen) {
        deliveryTypes.style.display = "none";
        deliveryImg.classList.remove("open")
        isOpen = false;
      }
    }
  });
});
