
function setTheme() 
    {
    //   document.body.setAttribute("data-theme", "dark");
    //   console.log("theme set");
    const checkBox = document.getElementById('themeSwitch');

       if (checkBox?.checked)
        {
            console.log('checked')
            document.documentElement.setAttribute('data-theme', 'dark');
            // document.getElementById('busifyLogo').src = "../home/static/peach-logo.png";
            document.getElementById('download-img').src = "../home/static/download-white.png";
            document.getElementById('globe-image').src = "../home/static/earth-white.png";
            document.getElementById('toggle-btn-img').src = "../home/static/toggle-white.png";

            // document.getElementById('destiny-card').style.border= "1px solid blue";
            // document.getElementById('destiny-card').style.boxShadow= "0px 0px 30px 0px blue";

            document.getElementById('email-img').src = "../home/static/email-dark-theme.png";
            document.getElementById('call-img').src = "../home/static/call-dark-theme.png";
            document.getElementById('location-img').src = "../home/static/location-dark-theme.png";

            window.localStorage.setItem('data-theme', 'dark');
        } 
        else
        {
          console.log("unchecked")

            // document.getElementById('busifyLogo').src = "../home/static/logo.png";
            document.getElementById('download-img').src = "../home/static/download.png";
            document.getElementById('globe-image').src = "../home/static/planet-earth.png";
            document.getElementById('toggle-btn-img').src = "../home/static/hamburger.png";

            document.getElementById('email-img').src = "../home/static/email.png";
            document.getElementById('call-img').src = "../home/static/phone.png";
            document.getElementById('location-img').src = "../home/static/location.png";

            // document.getElementById('destiny-card').style.border= "transparent";

            document.documentElement.setAttribute('data-theme', 'light');
            window.localStorage.setItem('data-theme', 'light');
          
        }
    }

    // function load(){
    //     console.log('script loaded');
    // }
    // load();