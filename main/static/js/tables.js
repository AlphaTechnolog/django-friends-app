const hrefeables = document.querySelectorAll('.hrefeable');

hrefeables.forEach((hrefeable) => {
  hrefeable.style.cursor = 'pointer';
  hrefeable.addEventListener('click', () => {
    window.location = hrefeable.dataset.href
  });
});