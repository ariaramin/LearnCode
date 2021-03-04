//mobile menu show
let nav = document.querySelector('.nav');
let mobile = document.querySelector('.mobile-menu');

function OpenMenu(){
    nav.classList.toggle("change");
    mobile.classList.toggle("open");
    document.body.classList.toggle("disable");
}

nav.addEventListener('click', OpenMenu);