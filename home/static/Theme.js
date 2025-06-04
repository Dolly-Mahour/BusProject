
function setTheme() 
    {
        const checkBox = document.getElementById('themeSwitch');
       if (checkBox?.checked)
        {
            localStorage.setItem('theme', 'dark')
            dark_theme();
        } 
        else
        {
            localStorage.setItem('theme', 'light')
            light_theme();
        }
    }




function show_modal(){

    let exists = "{{token}}";


    if (exists == "True"){
        console.log("Yay ! logged in");
        document.getElementById("Search_form").submit();
    }
    else{
        console.log("please login");
        var modal = new bootstrap.Modal(document.getElementById('loginModal'));
        localStorage.setItem("showLoginToast", "true");
        modal.show();
    }
}



function singup_taost(){
    let exists = "{{http_code_of_singup_api}}";
    console.log(typeof exists,"This is the type of the success code we are getting from the signup api")
    if (exists == "201"){
        console.log("Yay ! signup");
        const toastElement = document.getElementById('signupToast');
        const toast = new bootstrap.Toast(toastElement);
        toast.show();
        return exists;
    }
}
function show_login_taost(){
    let exists = "{{token}}";
    if (exists == "True"){
        console.log("Yay ! logged in");
        const toastElement = document.getElementById('loginToast');
        const toast = new bootstrap.Toast(toastElement);
        toast.show();
        return true;
    }
        return false;
}

// -------------------------THE MAIN EVENT LITSENER-----------------------------------------------------------------------------------------------------

document.addEventListener('DOMContentLoaded', function() {
let code_ = "{{http_code_of_singup_api}}"
console.log("calling the load function ",typeof(code_));

let exists = "{{token}}";

let profile = document.getElementById('div_of_profile_btn');
let signup = document.getElementById('div_of_singup_btn');
let login = document.getElementById('div_of_login_btn');


console.log("This is to check that the token exists or not",exists);
if (exists == "True"){
    
    profile.style.display = "flex";
    signup.style.display = "none";
    login.style.display = "none";
}
else{
    profile.style.display = "none";
    signup.style.display = "flex";
    login.style.display = "flex";
}

    if (localStorage.getItem('theme') === 'dark')
        {
            document.getElementById('themeSwitch').checked = true;
            dark_theme();
            console.log("Entering the theme at dark-------------------------------------------------------------------------------------")

        }
        else{
            
            document.getElementById('themeSwitch').checked = false;
            light_theme();
            console.log("Entering the theme at light-------------------------------------------------------------------------------------")
        }

        const shouldShowToast = localStorage.getItem("showLoginToast");
        if (shouldShowToast === "true") {
          localStorage.removeItem("showLoginToast"); 

        show_login_taost();
        }

        let code = 400
        code = singup_taost();
        console.log("This is all about the code response of the success code of signup api",code);
    
    const emailInput = document.getElementById('email');
    const numberInput = document.getElementById('number');
    const passwordInput = document.getElementById('password');
    const nameInput = document.getElementById('name');

    const numberInputLogin = document.getElementById('number-login');
    const passwordInputLogin = document.getElementById('password-login');


    nameInput.addEventListener('input', function() {
        const nameError = document.getElementById('nameError');
        if (nameInput.value.length < 3) {
            nameError.textContent = 'Name must be at least 3 characters long.';
            nameInput.classList.add('input-error');
        } else {
            nameError.textContent = '';
            nameInput.classList.remove('input-error');
        }
    });

    emailInput.addEventListener('input', function() {
        const emailError = document.getElementById('emailError');
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; 
        if (!emailPattern.test(emailInput.value)) {
            emailError.textContent = 'Please enter a valid email address.';
            emailInput.classList.add('input-error');
        } else {
            emailError.textContent = '';
            emailInput.classList.remove('input-error');
        }
    });


    numberInput.addEventListener('input', function() {
        const numberError = document.getElementById('numberError');
        const numberValue = numberInput.value;
        // const mobilePattern = /^[0-9]{10}$/;
        if (numberValue.length != 10) {
            numberError.textContent = 'Mobile number must be exactly 10 digits.';
            numberInput.classList.add('input-error');
        } else {
            numberError.textContent = '';
            numberInput.classList.remove('input-error');
        }
    });

    
    passwordInput.addEventListener('input', function() {
        const passwordError = document.getElementById('passwordError');
        const passwordValue = passwordInput.value;
        if (passwordValue.length != 8) {
            passwordError.textContent = 'Password must be at least of 8 characters';
            passwordInput.classList.add('input-error');
        } else {
            passwordError.textContent = '';
            passwordInput.classList.remove('input-error');
        }
    });

    numberInputLogin.addEventListener('input', function() {
        const numberError = document.getElementById('numberError-login');
        const numberValue = numberInputLogin.value;
        if (numberValue.length != 10) {
            numberError.textContent = 'Mobile number must be exactly 10 digits.';
            numberInput.classList.add('input-error');
        } else {
            numberError.textContent = '';
            numberInput.classList.remove('input-error');
        }
    });

    
    passwordInputLogin.addEventListener('input', function() {
        const passwordError = document.getElementById('passwordError-login');
        const passwordValue = passwordInputLogin.value;
        // const passwordPattern = /^[0-7]{8}$/;
        if (passwordValue.length != 8) {
            passwordError.textContent = 'Password must be at least of 8 characters';
            passwordInputLogin.classList.add('input-error');
        } else {
            passwordError.textContent = '';
            passwordInputLogin.classList.remove('input-error');
        }
    });


    document.getElementById('signup_form').addEventListener('submit', function(event) {
        if (nameInput.classList.contains('input-error') ||
            numberInput.classList.contains('input-error') ||
            emailInput.classList.contains('input-error') ||
            passwordInput.classList.contains('input-error')) {
            event.preventDefault();
            alert('Please fix the errors before submitting.');
        }
    });
});












function light_theme(){

    document.documentElement.setAttribute('data-theme', 'light');

    document.getElementById('download-img').src = "../home/static/download.png";
    document.getElementById('download-img-sm').src = "../home/static/download.png";
    document.getElementById('globe-image').src = "../home/static/planet-earth.png";
    document.getElementById('toggle-btn-img').src = "../home/static/hamburger.png";

    document.getElementById('email-img').src = "../home/static/email.png";
    document.getElementById('call-img').src = "../home/static/phone.png";
    document.getElementById('location-img').src = "../home/static/location.png";
    document.getElementById('earth-img-sm').src = "../home/static/planet-earth.png";

    document.getElementById('moonImage').src = "../home/static/moon.png";
    document.getElementById('docImage1').src = "../home/static/google-docs.png";
    document.getElementById('docImage2').src = "../home/static/google-docs.png";
    document.getElementById('docImage3').src = "../home/static/google-docs.png";
    document.getElementById('docImage4').src = "../home/static/google-docs.png";


    document.getElementById('card_calendar').src = "../home/static/calendar (2).png";

}
function dark_theme(){

    document.documentElement.setAttribute('data-theme', 'dark');

    document.getElementById('download-img').src = "../home/static/download-white.png";
    document.getElementById('download-img-sm').src = "../home/static/download-white.png";
    document.getElementById('globe-image').src = "../home/static/earth-white.png";
    document.getElementById('toggle-btn-img').src = "../home/static/toggle-white.png";
    document.getElementById('earth-img-sm').src = "../home/static/earth-white.png";


    document.getElementById('email-img').src = "../home/static/email-dark-theme.png";
    document.getElementById('call-img').src = "../home/static/call-dark-theme.png";
    document.getElementById('location-img').src = "../home/static/location-dark-theme.png";



    document.getElementById('moonImage').src = "../home/static/moon-white.png";
    document.getElementById('docImage1').src = "../home/static/google-doc-white.png";
    document.getElementById('docImage2').src = "../home/static/google-doc-white.png";
    document.getElementById('docImage3').src = "../home/static/google-doc-white.png";
    document.getElementById('docImage4').src = "../home/static/google-doc-white.png";

    document.getElementById('card_calendar').src = "../home/static/white-calendar.png";


}
