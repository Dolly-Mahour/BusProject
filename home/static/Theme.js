// FIRST function for calling the theme and setting it to the local storage
function setTheme() {
  const checkBox = document.getElementById("themeSwitch");
  if (checkBox?.checked) {
    localStorage.setItem("theme", "dark");
    dark_theme();
  } else {
    localStorage.setItem("theme", "light");
    light_theme();
  }
}

// SECOND function for showing the modal on the search button if not logged in
function show_modal() {
  var IsExist = document.getElementById("toggle_button_with_token_value").value;

  if (IsExist == "True") {
    console.log("Yay ! logged in");
    document.getElementById("Search_form").submit();
    localStorage.setItem("showLoginToast", "true");
  } else {
    console.log("please login");
    var modal = new bootstrap.Modal(document.getElementById("loginModal"));

    modal.show();
  }
}

// THIRD  function for showing the signup success toast if the httpcoderesponse is 201
function singup_taost() {
  let IsSignedIn = document.getElementById("signup_form_submit_button").value;
  console.log(
    IsSignedIn,
    "This is the type of the success code we are getting from the signup api"
  );
  if (IsSignedIn == "201") {
    console.log("Yay ! signup");
    const toastElement = document.getElementById("signupToast");
    const toast = new bootstrap.Toast(toastElement);
    toast.show();
    return IsSignedIn;
  }
}

// FOURTH function for showing the login success toast if the user is logged in
function show_login_taost() {
  console.log(
    "this is the local storage item we are checking in the toast fucn",
    localStorage.getItem("showLoginToast")
  );
  if (localStorage.getItem("showLoginToast") != null) {
    console.log("Yay ! logged in");
    const toastElement = document.getElementById("loginToast");
    const toast = new bootstrap.Toast(toastElement);
    toast.show();
    localStorage.removeItem("showLoginToast");
  }
}

//FIFTH to set the images of the toggle wallet logout and anothers according to the theme
function set_images() {
  let current_theme = localStorage.getItem("theme");
  console.log("this is the current theme", current_theme);
  if (current_theme == "dark") {
    document.getElementById("tickets-img").src =
      "../home/static/tickets-white.png";
    document.getElementById("wallet-img").src =
      "../home/static/wallet-white.png";
    document.getElementById("reffer-img").src =
      "../home/static/exchange-white.png";
  } else {
    document.getElementById("tickets-img").src = "../home/static/tickets.png";
    document.getElementById("wallet-img").src = "../home/static/wallet.png";
    document.getElementById("reffer-img").src = "../home/static/exchange.png";
  }
}

// -------------------------THE MAIN EVENT LITSENER-----------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function () {
  let code_ = document.getElementById("signup_button_with_http_response").value;
  console.log("calling the load function ", code_, typeof code_);

  var IsExist = document.getElementById("toggle_button_with_token_value").value;
  // if (IsExist == "True") {
  //   localStorage.setItem("logged_in", "True");
  // }
  singup_taost();
  let profile = document.getElementById("div_of_profile_btn");
  let signup = document.getElementById("div_of_singup_btn");
  let login = document.getElementById("div_of_login_btn");
  let logout = document.getElementById("logout");
  let reffer = document.getElementById("reffer");
  let tickets = document.getElementById("tickets");
  let wallet = document.getElementById("wallet");
  let hr = document.getElementById("hr-logout");

  console.log("This is to check that the token IsExist or not", IsExist);
  if (IsExist == "True") {
    profile.style.display = "flex";
    signup.style.display = "none";
    login.style.display = "none";
    reffer.style.display = "flex";
    logout.style.display = "flex";
    wallet.style.display = "flex";
    tickets.style.display = "flex";
    hr.style.display = "flex";
    set_images();
  } else {
    profile.style.display = "none";
    signup.style.display = "flex";
    login.style.display = "flex";
    reffer.style.display = "none";
    logout.style.display = "none";
    wallet.style.display = "none";
    tickets.style.display = "none";
    hr.style.display = "none";
    set_images();
  }

  if (localStorage.getItem("theme") === "dark") {
    document.getElementById("themeSwitch").checked = true;
    dark_theme();
    console.log(
      "Entering the theme at dark-------------------------------------------------------------------------------------"
    );
  } else {
    document.getElementById("themeSwitch").checked = false;
    light_theme();
    console.log(
      "Entering the theme at light-------------------------------------------------------------------------------------"
    );
  }

  if (IsExist == "True") {
    show_login_taost();
  }

  const emailInput = document.getElementById("email");
  const numberInput = document.getElementById("number");
  const passwordInput = document.getElementById("password");
  const nameInput = document.getElementById("name");

  const numberInputLogin = document.getElementById("number-login");
  const passwordInputLogin = document.getElementById("password-login");

  nameInput.addEventListener("input", function () {
    const nameError = document.getElementById("nameError");
    if (nameInput.value.length < 3) {
      nameError.textContent = "Name must be at least 3 characters long.";
      nameInput.classList.add("input-error");
    } else {
      nameError.textContent = "";
      nameInput.classList.remove("input-error");
    }
  });

  emailInput.addEventListener("input", function () {
    const emailError = document.getElementById("emailError");
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(emailInput.value)) {
      emailError.textContent = "Please enter a valid email address.";
      emailInput.classList.add("input-error");
    } else {
      emailError.textContent = "";
      emailInput.classList.remove("input-error");
    }
  });

  numberInput.addEventListener("input", function () {
    const numberError = document.getElementById("numberError");
    const numberValue = numberInput.value;
    // const mobilePattern = /^[0-9]{10}$/;
    if (numberValue.length != 10) {
      numberError.textContent = "Mobile number must be exactly 10 digits.";
      numberInput.classList.add("input-error");
    } else {
      numberError.textContent = "";
      numberInput.classList.remove("input-error");
    }
  });

  passwordInput.addEventListener("input", function () {
    const passwordError = document.getElementById("passwordError");
    const passwordValue = passwordInput.value;
    if (passwordValue.length != 8) {
      passwordError.textContent = "Password must be at least of 8 characters";
      passwordInput.classList.add("input-error");
    } else {
      passwordError.textContent = "";
      passwordInput.classList.remove("input-error");
    }
  });

  numberInputLogin.addEventListener("input", function () {
    const numberError = document.getElementById("numberError-login");
    const numberValue = numberInputLogin.value;
    if (numberValue.length != 10) {
      numberError.textContent = "Mobile number must be exactly 10 digits.";
      numberInput.classList.add("input-error");
    } else {
      numberError.textContent = "";
      numberInput.classList.remove("input-error");
    }
  });

  passwordInputLogin.addEventListener("input", function () {
    const passwordError = document.getElementById("passwordError-login");
    const passwordValue = passwordInputLogin.value;
    // const passwordPattern = /^[0-7]{8}$/;
    if (passwordValue.length != 8) {
      passwordError.textContent = "Password must be at least of 8 characters";
      passwordInputLogin.classList.add("input-error");
    } else {
      passwordError.textContent = "";
      passwordInputLogin.classList.remove("input-error");
    }
  });

  document
    .getElementById("signup_form")
    .addEventListener("submit", function (event) {
      if (
        nameInput.classList.contains("input-error") ||
        numberInput.classList.contains("input-error") ||
        emailInput.classList.contains("input-error") ||
        passwordInput.classList.contains("input-error")
      ) {
        event.preventDefault();
        alert("Please fix the errors before submitting.");
      }
    });
});

function light_theme() {
  var IsExist = document.getElementById("toggle_button_with_token_value").value;

  document.documentElement.setAttribute("data-theme", "light");

  document.getElementById("download-img").src = "../home/static/download.png";
  document.getElementById("download-img-sm").src =
    "../home/static/download.png";
  document.getElementById("globe-image").src =
    "../home/static/planet-earth.png";
  document.getElementById("toggle-btn-img").src =
    "../home/static/hamburger.png";

  if (
    document.getElementById("tickets-img") != null &&
    document.getElementById("wallet-img") != null &&
    document.getElementById("reffer-img")
  ) {
    document.getElementById("tickets-img").src = "../home/static/tickets.png";
    document.getElementById("wallet-img").src = "../home/static/wallet.png";
    document.getElementById("reffer-img").src = "../home/static/exchange.png";
  }
  // document.getElementById('tickets-img').src = "../home/static/tickets.png";
  // document.getElementById('wallet-img').src = "../home/static/wallet.png";
  // document.getElementById('reffer-img').src = "../home/static/exchange.png";

  document.getElementById("email-img").src = "../home/static/email.png";
  document.getElementById("call-img").src = "../home/static/phone.png";
  document.getElementById("location-img").src = "../home/static/location.png";
  document.getElementById("earth-img-sm").src =
    "../home/static/planet-earth.png";

  document.getElementById("moonImage").src = "../home/static/moon.png";
  document.getElementById("docImage1").src = "../home/static/google-docs.png";
  document.getElementById("docImage2").src = "../home/static/google-docs.png";
  document.getElementById("docImage3").src = "../home/static/google-docs.png";
  document.getElementById("docImage4").src = "../home/static/google-docs.png";


  if(document.getElementById("card_calendar")!=null){
document.getElementById("card_calendar").src =
    "../home/static/calendar (2).png";
  }
  
}
function dark_theme() {
  var IsExist = document.getElementById("toggle_button_with_token_value").value;

  document.documentElement.setAttribute("data-theme", "dark");

  document.getElementById("download-img").src =
    "../home/static/download-white.png";
  document.getElementById("download-img-sm").src =
    "../home/static/download-white.png";
  document.getElementById("globe-image").src = "../home/static/earth-white.png";
  document.getElementById("toggle-btn-img").src =
    "../home/static/toggle-white.png";
  document.getElementById("earth-img-sm").src =
    "../home/static/earth-white.png";
  if (
    document.getElementById("tickets-img") != null &&
    document.getElementById("wallet-img") != null &&
    document.getElementById("reffer-img")
  ) {
    document.getElementById("tickets-img").src =
      "../home/static/tickets-white.png";
    document.getElementById("wallet-img").src =
      "../home/static/wallet-white.png";
    document.getElementById("reffer-img").src =
      "../home/static/exchange-white.png";
  }
  

  document.getElementById("email-img").src =
    "../home/static/email-dark-theme.png";
  document.getElementById("call-img").src =
    "../home/static/call-dark-theme.png";
  document.getElementById("location-img").src =
    "../home/static/location-dark-theme.png";

  document.getElementById("moonImage").src = "../home/static/moon-white.png";
  document.getElementById("docImage1").src =
    "../home/static/google-doc-white.png";
  document.getElementById("docImage2").src =
    "../home/static/google-doc-white.png";
  document.getElementById("docImage3").src =
    "../home/static/google-doc-white.png";
  document.getElementById("docImage4").src =
    "../home/static/google-doc-white.png";
  if(document.getElementById("card_calendar")!=null){
  document.getElementById("card_calendar").src =
    "../home/static/white-calendar.png";
  }

}
