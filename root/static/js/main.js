document.addEventListener("scroll", scrolled);
let height = window.outerHeight
function scrolled() {
  document.getElementById("header").style.opacity = '' + (height / (window.scrollY * 1.2) / 10);
  if (window.scrollY >= 290) {
    document.getElementById("nav").classList.add("scrolled");
  } else {
    document.getElementById("nav").classList.remove("scrolled");
    }
}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();

    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});