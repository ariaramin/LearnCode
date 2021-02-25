let eye = document.getElementById("eye");
let password = document.getElementById("password");

eye.addEventListener("click", (toggle) => {
  if (eye.className == "fas fa-eye-slash") {
    eye.className = "fas fa-eye";
    password.setAttribute("type", "text");
  } else {
    eye.className = "fas fa-eye-slash";
    password.setAttribute("type", "password");
  }
});
