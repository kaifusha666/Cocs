const footer = document.querySelector('footer')

window.addEventListener('resize', function(evt){
    const widthWind = document.querySelector('body').offsetWidth;
    if (widthWind <= 820) {
        console.log(1)
        footer.classList.add('fixed-bottom')
    }
    else{
        footer.classList.remove('fixed-bottom')
    }
});