document.addEventListener('scroll', (event) => {
  let height = document.body.offsetHeight;
  let scrollTop = window.scrollY;
  let winHeight = window.innerHeight;
  let opacity = ((scrollTop / (height / winHeight) * 0.8) / 100);
  if (opacity <= 0.8) {
    document.getElementById('nav').style.background = `rgba(0,0,0,${opacity})`;
  }
});