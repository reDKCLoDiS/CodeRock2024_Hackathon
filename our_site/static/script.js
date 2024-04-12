const setListener = (element, type, handler) => {
  if (!element) {
    return;
  }
  element.addEventListener(type, handler);
  return () => {
    element.removeEventListener(type, handler);
  };
};

document.addEventListener("DOMContentLoaded", function () {
  var toggleStocks = document.getElementById("toggleStocks");
  var stockList = document.querySelector(".manufacturerStockSelector ul");

  var isOpen = false;
  if (toggleStocks) {
    toggleStocks.addEventListener("click", function (event) {
      if (!isOpen === true) {
        stockList.style.display = "block";
        isOpen = true;
      } else {
        stockList.style.display = "none";
        isOpen = false;
      }
    });
  }

  document.addEventListener("click", function (event) {
    if (!event.target.closest(".manufacturerStockSelector")) {
      if (isOpen) {
        stockList.style.display = "none";
        isOpen = false;
      }
    }
  });
});

document.addEventListener("DOMContentLoaded", (event) => {
  const userMailInput = document.getElementById("userMailInput");
  const entryOpenBtn = document.getElementById("entryButton");

  entryOpenBtn.addEventListener("click", function (event) {
    const userMailValue = userMailInput.value;

    fetch("/check-email", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email: userMailValue }),
    })
    .then(response => response.json())
    .then(data => {
      if (data.exists) {
        window.location.href = "/login-page.html";
      } else {
        window.location.href = "/reg-page.html";
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });
});

window.addEventListener("DOMContentLoaded", () => {
    const products = document.querySelectorAll(".product");
    const filterListBtn = document.querySelector(".productFiltersImg");
    const toggleFilters = document.getElementById("productFiltersToggle");
    const filterList = document.querySelector(".сategoryfilter ul");
    const searchBar = document.getElementById("searchBar");
  
    function updateProductVisibility() {
      const searchTerm = searchBar.value.trim().toLowerCase();
  
      // Сначала скрываем все элементы
      products.forEach((product) => {
        product.classList.add("hide");
      });
  
      // Показываем только те элементы, которые соответствуют критериям поиска
      let visibleProductsOrder = 0;
      products.forEach((product) => {
        const productTitle = product.querySelector(".title").innerText.trim().toLowerCase();
        const isVisible = searchTerm === "" || productTitle.includes(searchTerm);
  
        if (isVisible) {
          product.classList.remove("hide");
          product.style.order = visibleProductsOrder;
          visibleProductsOrder++;
        }
      });
    }
  
    searchBar.addEventListener("input", updateProductVisibility);
  
    if (toggleFilters) {
      toggleFilters.addEventListener("click", () => {
        const isOpen = !filterList.style.display || filterList.style.display === "none";
        filterList.style.display = isOpen ? "block" : "none";
        filterListBtn.classList.toggle("open", isOpen);
      });
    }
  
    document.addEventListener("click", (event) => {
      if (!event.target.closest(".сategoryfilter")) {
        filterList.style.display = "none";
        filterListBtn.classList.remove("open");
      }
    });
  });
  

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