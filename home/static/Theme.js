
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

    let exists = document.getElementById("search_button_of_card").value;
    console.log("calling pop up",exists);
    if (exists == "True"){
        console.log("Yay ! logged in");
    }
    else{
        console.log("please login");
        var modal = new bootstrap.Modal(document.getElementById('loginModal'));
        modal.show();
    }
}


// function bottom_border(){
//     console.log("hello");
// }


function load(){
        // console.log('script loaded');
        if (localStorage.getItem('theme') === 'dark')
        {
            document.getElementById('themeSwitch').checked = true;
            dark_theme();

        }
        else{
            
            document.getElementById('themeSwitch').checked = false;
            light_theme();
        }
    }
load();








function light_theme(){

    document.documentElement.setAttribute('data-theme', 'light');

    document.getElementById('download-img').src = "../home/static/download.png";
    document.getElementById('globe-image').src = "../home/static/planet-earth.png";
    document.getElementById('toggle-btn-img').src = "../home/static/hamburger.png";

    document.getElementById('email-img').src = "../home/static/email.png";
    document.getElementById('call-img').src = "../home/static/phone.png";
    document.getElementById('location-img').src = "../home/static/location.png";
}
function dark_theme(){

    document.documentElement.setAttribute('data-theme', 'dark');

    document.getElementById('download-img').src = "../home/static/download-white.png";
    document.getElementById('globe-image').src = "../home/static/earth-white.png";
    document.getElementById('toggle-btn-img').src = "../home/static/toggle-white.png";


    document.getElementById('email-img').src = "../home/static/email-dark-theme.png";
    document.getElementById('call-img').src = "../home/static/call-dark-theme.png";
    document.getElementById('location-img').src = "../home/static/location-dark-theme.png";
}