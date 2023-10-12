const login = async () => {
    var username = document.querySelector('#username').value
    var password = document.querySelector('#password').value
    let alert;

    const search_url = `/api-login/?username1=${username}&password1=${password}`;

    try {
        const response = await fetch(search_url)
        const data = await response.json();

        if (response.status === 200) {
            console.log('Login Successful');
            // You can redirect the user to the dashboard page if login is successful.
            window.location.assign("/dashboard/");
        } else if (response.status === 400) {
            const data = await response.json();
            document.querySelector('#alert').innerHTML =  data.detail;
            document.querySelector('#alert').classList.remove('alert-success');
            document.querySelector('#alert').classList.add('alert-danger');
        }
    } catch (error) {
       
        document.querySelector('#alert').innerHTML = `No "${username}" username in the Database or Password is inCorrect`;
        document.querySelector('#alert').classList.remove('alert-success');
        document.querySelector('#alert').classList.add('alert-danger');
    }
};

var loginCredential = document.querySelector('#BtnLogin');
loginCredential.addEventListener("click", function() {
    login();
});
