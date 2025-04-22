
function setTheme() 
    {
        const checkBox = document.getElementById('themeSwitch');
       if (checkBox?.checked)
        {
            localStorage.setItem('theme', 'dark')
            console.log('checked')
            set_dark_theme_elements();
        } 
        else
        {
          console.log("unchecked")
          localStorage.setItem('theme', 'light')
          set_light_theme_elements();
        }
    }

    function load(){
        console.log('script loaded');
        if (localStorage.getItem('theme') === 'dark')
        {
            document.getElementById('themeSwitch').checked = true;
            set_dark_theme_elements();
        }
        else{
            document.documentElement.setAttribute('data-theme', 'light');
            set_light_theme_elements();
        }
    }
function set_dark_theme_elements(){
    document.documentElement.setAttribute('data-theme', 'dark');
    document.getElementById('download-img').src = "../home/static/download-white.png";
    document.getElementById('globe-image').src = "../home/static/earth-white.png";
    document.getElementById('toggle-btn-img').src = "../home/static/toggle-white.png";

    document.getElementById('email-img').src = "../home/static/email-dark-theme.png";
    document.getElementById('call-img').src = "../home/static/call-dark-theme.png";
    document.getElementById('location-img').src = "../home/static/location-dark-theme.png";

}
function set_light_theme_elements(){
    document.getElementById('themeSwitch').checked = false;
    document.getElementById('download-img').src = "../home/static/download.png";
    document.getElementById('globe-image').src = "../home/static/planet-earth.png";
    document.getElementById('toggle-btn-img').src = "../home/static/hamburger.png";

    document.getElementById('email-img').src = "../home/static/email.png";
    document.getElementById('call-img').src = "../home/static/phone.png";
    document.getElementById('location-img').src = "../home/static/location.png";
}
    load();