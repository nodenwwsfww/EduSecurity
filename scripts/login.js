let btn = document.getElementById('btn');
let login = document.getElementById('login');
let password = document.getElementById('password');

btn.addEventListener('click', validate);

function validate() {
	login.classList.remove("is-invalid");
	password.classList.remove("is-invalid");
	if(login.value == ""){
		login.classList.add("is-invalid");
	}
	if(password.value == ""){
		password.classList.add("is-invalid");
	}
	else{
		request(login.value, password.value);
	}
}
