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

document.addEventListener("DOMContentLoaded", function () {
  var toggleFilters = document.getElementById("productFiltersToggle");
  var filterList = document.querySelector(".сategoryfilter ul");

  var isOpen = false;
  if (toggleFilters) {
    toggleFilters.addEventListener("click", function (event) {
      if (!isOpen === true) {
        filterList.style.display = "block";
        isOpen = true;
      } else {
        filterList.style.display = "none";
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
  const loginModal = document.getElementById("loginModal");
  const regModal = document.getElementById("regModal");
  const openBtn = document.getElementById("entryButton");
  const loginModalContainer = document.getElementById("loginModal-container");
  const regModalContiner = document.getElementById("regModal-container");
  const userMailInput = document.getElementById("userMailInput");

  var isOpen = false;
  openBtn.addEventListener("click", function (event) {
    var userMailValue = userMailInput.value;
    if (userMailValue === "123") {
      if (!isOpen === true) {
        loginModal.classList.add("is-open");
        loginModalContainer.classList.add("is-open");
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
      if (!isOpen === true) {
        regModal.classList.add("is-open");
        regModalContiner.classList.add("is-open");
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

window.addEventListener("DOMContentLoaded", (event) => {
  const modal = document.getElementById("entryModal");
  const openBtn = document.getElementById("loginBtn");
  const modalContainer = document.getElementById("entryModal-container");

  var isOpen = false;

  if (openBtn) {
    openBtn.addEventListener("click", function (event) {
      if (!isOpen === true) {
        modal.classList.add("is-open");
        modalContainer.classList.add("is-open");
        isOpen = true;
      } else {
        modal.classList.remove("is-open");
        modalContainer.classList.remove("is-open");
        isOpen = false;
      }
    });
  }

  const handleClickClose = function (event) {
    if (event.target == modal) {
      modal.classList.remove("is-open");
      modalContainer.classList.remove("is-open");
      isOpen = false;
    }
  };

  window.onclick = handleClickClose;
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
