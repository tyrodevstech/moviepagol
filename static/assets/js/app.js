//  // Force to scroll top 
 history.scrollRestoration = "auto"

 //  Back to top 
 let btpbutton = document.getElementById('btpbutton')
 window.addEventListener('scroll', (function () {
     if ($(window).scrollTop() > 300) {
         btpbutton.classList.add('show');
     } else {
         btpbutton.classList.remove('show');
     }
 }))

 btpbutton.addEventListener('click', function (e) {
     window.scrollTo(0, 0);
 });

 //  Sub menu collapse
 const expandBtn = document.querySelectorAll(".expand-btn");
 expandBtn.forEach((btn) => {
     btn.addEventListener("click", () => {
         btn.classList.toggle("open");
     });
 });

 //  Download collapse 
 $(".downloadbtn").click(function (e) {
     $(this).children('.expand-icon').toggleClass('active');
     $(this).next(".dropdown").slideToggle('fast');
     e.stopPropagation();
 });

 $(document).ready(function () {
     $(".dropdown .toogle-dropdown-sub").click(function (e) {
         $(this).children('.expand-icon').toggleClass('active');
         dropSub = $(this).next('.dropdown-sub')
         dropSub.slideToggle('fast')
         dropSub.closest('li').siblings('li').children('.dropdown-sub').slideUp('fast')
         dropSub.closest('li').siblings('li').children('.toogle-dropdown-sub').children('.expand-icon').removeClass('active')
         e.stopPropagation();
     });
 });


 $('.news-ticker').AcmeTicker({
    controls: {
      prev: $('.acme-news-ticker-prev'),
      next: $('.acme-news-ticker-next')
    },
    type:'horizontal',
    autoplay: 3000,
    speed: 500,
    pauseOnHover:true,
    pauseOnFocus:true,
  });