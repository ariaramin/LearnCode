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

let cover = document.querySelector(".cover");
let title = document.querySelector(".cover-title");
let text = document.querySelector(".cover-text");
let text2 = document.querySelector(".cover-text2");
let btn = document.querySelector(".cover-btn");
let color = document.getElementsByClassName('color');

btn.addEventListener("click", (move) => {
  cover.classList.toggle("right");
  if (title.innerHTML === "Welcome") {
    title.innerHTML = "Welcome back!";
    text.innerHTML = "Log in to the account";
    text2.innerHTML = "with your personal info to continue";
    btn.innerHTML = "Sign in";
  } else {
    title.innerHTML = "Welcome";
    text.innerHTML = "Create account with";
    text2.innerHTML = "your personal info to continue";
    btn.innerHTML = "Log in";
  }

  if (screen.width < 768) {
    cover.classList.toggle("down");
  }
});
