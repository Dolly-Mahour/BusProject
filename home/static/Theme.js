
function setTheme() 
    {
    //   document.body.setAttribute("data-theme", "dark");
    //   console.log("theme set");
    const checkBox = document.getElementById('themeSwitch');

       if (checkBox?.checked)
        {
            console.log('checked')
            document.documentElement.setAttribute('data-theme', 'dark');
            document.getElementById('busifyLogo').src = "../home/static/peach-logo.png";
            document.getElementById('download-img').src = "../home/static/download-peach.png";
            document.getElementById('globe-image').src = "../home/static/globe-peach.png";
            document.getElementById('toggle-btn-img').src = "../home/static/toggle-peach.png";

            document.getElementById('email-img').src = "../home/static/email-dark-theme.png";
            document.getElementById('call-img').src = "../home/static/call-dark-theme.png";
            document.getElementById('location-img').src = "../home/static/location-dark-theme.png";

            window.localStorage.setItem('data-theme', 'dark');
        } 
        else
        {
          console.log("unchecked")

            document.getElementById('busifyLogo').src = "../home/static/logo.png";
            document.getElementById('download-img').src = "../home/static/download.png";
            document.getElementById('globe-image').src = "../home/static/planet-earth.png";
            document.getElementById('toggle-btn-img').src = "../home/static/hamburger.png";

            document.getElementById('email-img').src = "../home/static/email.png";
            document.getElementById('call-img').src = "../home/static/phone.png";
            document.getElementById('location-img').src = "../home/static/location.png";

            document.documentElement.setAttribute('data-theme', 'light');
            window.localStorage.setItem('data-theme', 'light');
          
        }
    }

    // function load(){
    //     console.log('script loaded');
    // }
    // load();