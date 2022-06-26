let btn = document.getElementById('btn');
let login = document.querySelector('.login');
let password = document.querySelector('.password');

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
}
