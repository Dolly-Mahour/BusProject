
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
            window.localStorage.setItem('data-theme', 'dark');
        } 
        else
        {
          console.log("unchecked")
          document.documentElement.setAttribute('data-theme', 'light');
          window.localStorage.setItem('data-theme', 'light');
        }
    }

    // function load(){
    //     console.log('script loaded');
    // }
    // load();