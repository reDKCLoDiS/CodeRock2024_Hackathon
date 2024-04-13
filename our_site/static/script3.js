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

document.addEventListener("DOMContentLoaded", function() {
  var contactUsForm = document.getElementById("contactUsForm");
  contactUsForm.addEventListener("submit", function(event) {
      event.preventDefault();
      
      var csrfTokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
      var csrfValue = csrfTokenInput.value;

      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/contactUs/", true);
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onreadystatechange = function() {
          if (xhr.readyState === XMLHttpRequest.DONE) {
              if (xhr.status === 200) {
                  console.debug(xhr.responseText);
                  console.debug("Successfully sent contact form");
              } else {
                  console.error(xhr.responseText);
                  console.error("Error occurred while sending contact form");
              }
          }
      };
      var formData = {
          userName: document.getElementById("userName").value,
          companyName: document.getElementById("companyName").value,
          emailAddress: document.getElementById("emailAddress").value,
          message: document.getElementById("message").value,
          csrfmiddlewaretoken: csrfValue
      };
      xhr.send(JSON.stringify(formData));
  });
});

document.addEventListener("DOMContentLoaded", (event) => {
  const loginModal = document.getElementById("loginModal");
  const regModal = document.getElementById("regModal");
  const entryOpenBtn = document.getElementById("entryButton");
  const loginModalContainer = document.getElementById("loginModal-container");
  const regModalContiner = document.getElementById("regModal-container");
  const userMailInput = document.getElementById("userMailInput");
  const entryModal = document.getElementById("entryModal");
  const loginOpenBtn = document.getElementById("loginBtn");
  const entryModalContainer = document.getElementById("entryModal-container");

  if (loginOpenBtn) {
    loginOpenBtn.addEventListener("click", function (event) {
      var isOpen = false;

      if (!isOpen === true) {
        entryModal.classList.add("is-open");
        entryModalContainer.classList.add("is-open");
        isOpen = true;
      } else {
        entryModal.classList.remove("is-open");
        entryModalContainer.classList.remove("is-open");
        isOpen = false;
      }

      const handleClickClose = function (event) {
        if (event.target == entryModal) {
          entryModal.classList.remove("is-open");
          entryModalContainer.classList.remove("is-open");
          isOpen = false;
        }
      };

      window.onclick = handleClickClose;
    });
  }

  entryOpenBtn.addEventListener("click", function (event) {
    var userMailValue = userMailInput.value;
    if (userMailValue === "123") {
      var isOpen = false;

      if (!isOpen === true) {
        loginModal.classList.add("is-open");
        loginModalContainer.classList.add("is-open");
        entryModal.classList.remove("is-open");
        entryModalContainer.classList.remove("is-open");
        isOpen = true;
      } else {
        loginModal.classList.remove("is-open");
        loginModalContainer.classList.remove("is-open");
        isOpen = false;
      }
      const handleClickCloseLoginModal = function (event) {
        if (event.target == loginModal) {
          loginModal.classList.remove("is-open");
          loginModalContainer.classList.remove("is-open");
          isOpen = false;
        }
      };
      window.onclick = handleClickCloseLoginModal;
    } else {
      var isOpen = false;

      if (!isOpen === true) {
        regModal.classList.add("is-open");
        regModalContiner.classList.add("is-open");
        entryModal.classList.remove("is-open");
        entryModalContainer.classList.remove("is-open");
        isOpen = true;
      } else {
        regModal.classList.remove("is-open");
        regModalContiner.classList.remove("is-open");
        isOpen = false;
      }
      const handleClickCloseRegModal = function (event) {
        if (event.target == regModal) {
          regModal.classList.remove("is-open");
          regModalContiner.classList.remove("is-open");
          isOpen = false;
        }
      };
      window.onclick = handleClickCloseRegModal;
    }
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
  var userLabel = document.getElementById("userLabel");
  var manufacturerLabel = document.getElementById("manufacturerLabel");
  var underline = document.getElementById("underline");
  var navInputManufacturerStock = document.querySelector(
    ".nav__inputManufacturerStock"
  );

  underline.style.width = userLabel.offsetWidth + "px";
  underline.style.left = userLabel.offsetLeft + "px";

  userLabel.addEventListener("click", function () {
    underline.style.width = userLabel.offsetWidth + "px";
    underline.style.left = userLabel.offsetLeft + "px";
    navInputManufacturerStock.style.visibility = "hidden";
  });

  manufacturerLabel.addEventListener("click", function () {
    underline.style.width = manufacturerLabel.offsetWidth + "px";
    underline.style.left = manufacturerLabel.offsetLeft + "px";
    navInputManufacturerStock.style.visibility = "visible";
  });
});
