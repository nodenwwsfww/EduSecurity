let btn = document.getElementById('btn');
let login = document.getElementById('id_username');
let phone = document.getElementById('id_phone_number');
let mail = document.getElementById('id_email');
let city = document.getElementById('city');
let password = document.getElementById('id_password1');
let repassword = document.getElementById('id_password2');

btn.addEventListener('click', validate);

function validate() {
	login.classList.remove("is-invalid");
	phone.classList.remove("is-invalid");
	mail.classList.remove("is-invalid");
	password.classList.remove("is-invalid");
	repassword.classList.remove("is-invalid");
	
	if(login.value == ""){
		login.classList.add("is-invalid");
	}
	let re = /^[\d\+][\d\(\)\ -]{4,14}\d$/;
	if(!re.test(phone.value)){
		phone.classList.add("is-invalid");
	}
	let reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
	if(reg.test(mail.value) == false) {
	    mail.classList.add("is-invalid");
	}
	if(city.value == ""){
		city.classList.add("is-invalid");
	}
	if(password.value == ""){
		password.classList.add("is-invalid");
	}
	if(repassword.value == ""){
		repassword.classList.add("is-invalid");
	}
	if(!(password.value == repassword.value)){
		repassword.classList.add("is-invalid");
	}
}
