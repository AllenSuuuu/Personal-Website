window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('.fade-in');
    const scrollPos = window.pageYOffset + window.innerHeight - 50;

    for (let sec of sections) {
        if (sec.offsetTop < scrollPos) {
            sec.style.opacity = 1;
        }
    }
});
