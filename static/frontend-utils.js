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
  console.log("showing modal -", IsExist);
  if (IsExist == "True") {
    console.log("Yay ! logged in");
  } else {
    console.log("please login");
    var modal = new bootstrap.Modal(document.getElementById("loginModal"));
    modal.show();
  }
}

// THIRD  function for showing the signup success toast if the httpcoderesponse is 201
function singup_taost() {
  let IsSignedIn = document.getElementById("signup_form_submit_button").value;
  if (IsSignedIn == "201") {
    console.log("Yay ! signup");
    const toastElement = document.getElementById("signupToast");
    const toast = new bootstrap.Toast(toastElement);
    toast.show();
  }
  if (IsSignedIn == "400") {
    const toastElement = document.getElementById("SignupErrorToast");
    const toast = new bootstrap.Toast(toastElement);
    toast.show();
  }
}

// FOURTH function for showing the login success toast if the user is logged in
function show_login_taost() {
  let isLoggedIn = document.getElementById("navbar_login_btn").value;
  console.log("Yay ! logged in");
  if (isLoggedIn == "200") {
    const toastElement = document.getElementById("loginToast");
    const toast = new bootstrap.Toast(toastElement);
    toast.show();
  }
  if (isLoggedIn == "401") {
    const toastElement = document.getElementById("LoginErrorToast");
    const toast = new bootstrap.Toast(toastElement);
    toast.show();
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

// SIXTH FUNCTION FOR THE TEXT COPY IN REFFER AND EARN
function copyText() {
  const text = document.getElementById("textToCopy").innerText;
  navigator.clipboard
    .writeText(text)
    .then(() => {
      alert("Text copied to clipboard!");
    })
    .catch((err) => {
      console.error("Failed to copy text: ", err);
      alert("Failed to copy text. Please try again.");
    });
}

// Seventh function for sharing options on reffer page
function sharePage() {
  if (navigator.share) {
    navigator
      .share({
        title: "Busify - Book Bus Tickets",
        // text: 'Check out Busify to book your bus tickets online!',
        text: "🚍 Hey! I’ve been using Busify to book my bus tickets online — it’s super easy and reliable ! Use my referral code 550607 when you sign up to get ₹200 off your first booking! Book your next trip with Busify now-Link✨",
      })
      .then(() => console.log("Thanks for sharing!"))
      .catch(console.error);
  } else {
    alert("Sharing is not supported on this device/browser.");
  }
}
// -------------------------THE MAIN EVENT LITSENER-----------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function () {
  // CHECK THE THEME EITHER DARK OR LIGHT
  if (localStorage.getItem("theme") === "dark") {
    document.getElementById("themeSwitch").checked = true;
    dark_theme();
    console.log("WE ARE IN THE DARK THEME ..!");
  } else {
    document.getElementById("themeSwitch").checked = false;
    light_theme();
    console.log("WE ARE IN THE LIGHT THEME..!");
  }
  let SignupResponseCode = document.getElementById(
    "signup_button_with_http_response"
  ).value;
  console.log(
    "DEFAULT PAGE LOAD METHOD--! SUCCESS CODE OF SIGNUP-->",
    SignupResponseCode,
    typeof SignupResponseCode
  );
  var IsExist = document.getElementById("toggle_button_with_token_value").value;
  const SearchBusForm = document.getElementById("Search_form");
  if (SearchBusForm != null) {
    SearchBusForm.addEventListener("submit", function (event) {
      event.preventDefault();
      if (IsExist == "True") {
        SearchBusForm.submit();
      }
    });
  }
  // CALLING THE TOAST METHOD SUCCESS OR WARNING
  singup_taost();
  show_login_taost();

  // getting the variables of the items in toggle need to hide and show
  let profile = document.getElementById("div_of_profile_btn");
  let signup = document.getElementById("div_of_singup_btn");
  let login = document.getElementById("div_of_login_btn");
  let logout = document.getElementById("logout");
  let reffer = document.getElementById("reffer");
  let tickets = document.getElementById("tickets");
  let wallet = document.getElementById("wallet");
  let hr = document.getElementById("hr-logout");

  console.log("IS TOKEN EXIST OR NOT-->", IsExist, typeof IsExist);

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

  // signup form inputs check for error display
  const emailInput = document.getElementById("email");
  const numberInput = document.getElementById("number");
  const passwordInput = document.getElementById("password");
  // login form inputs for error display
  const numberInputLogin = document.getElementById("number-login");
  const passwordInputLogin = document.getElementById("password-login");

  // checking if the email contains @gmail.com  or email regex
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
  // checking if the mobile number is less that 10 digits
  numberInput.addEventListener("input", function () {
    const numberError = document.getElementById("numberError");
    const numberValue = numberInput.value;
    if (numberValue.length != 10) {
      numberError.textContent = "Mobile number must be exactly 10 digits.";
      numberInput.classList.add("input-error");
    } else {
      numberError.textContent = "";
      numberInput.classList.remove("input-error");
    }
  });
  // checking if the password is less that 8 digits
  passwordInput.addEventListener("input", function () {
    const passwordError = document.getElementById("passwordError");
    const passwordValue = passwordInput.value;
    if (passwordValue.length < 8) {
      passwordError.textContent = "Password must be at least of 8 characters";
      passwordInput.classList.add("input-error");
    } else {
      passwordError.textContent = "";
      passwordInput.classList.remove("input-error");
    }
  });

  // checking if the mobile number is less that 10 digits
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

  // checking if the password is less that 8 digits
  passwordInputLogin.addEventListener("input", function () {
    const passwordError = document.getElementById("passwordError-login");
    const passwordValue = passwordInputLogin.value;
    // const passwordPattern = /^[0-7]{8}$/;
    if (passwordValue.length < 8) {
      passwordError.textContent = "Password must be at least of 8 characters";
      passwordInputLogin.classList.add("input-error");
    } else {
      passwordError.textContent = "";
      passwordInputLogin.classList.remove("input-error");
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

  if (document.getElementById("card_calendar") != null) {
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
  if (document.getElementById("card_calendar") != null) {
    document.getElementById("card_calendar").src =
      "../home/static/white-calendar.png";
  }
}
