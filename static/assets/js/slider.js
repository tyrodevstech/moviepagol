let width = window.innerWidth;
let perLoadCount = 0;
let carousels = document.querySelectorAll(".slider__content");
let heroslider_content = document.getElementById("heroslider_content");
let topslider__content = document.getElementById("topslider__content");
let primaryslider__content = document.getElementById("primary-slider");
let secondaryslider__content = document.getElementById("secondary-slider");
let stillpath__content = document.getElementById("still_path");
let gap = "0.5rem";

let bp_1920 = 8;
let bp_1550 = 7;
let bp_1280 = 6;
let bp_768 = 3;
let bp_480 = 2;

if (width > 768) perLoadCount = 1;

if (typeof heroslider_content != "undefined" && heroslider_content != null) {
  new Splide(heroslider_content, {
    type: "fade",
    perMove: 1,
    preloadPages: perLoadCount,
    interval: 5000,
    rewind: true,
    autoplay: true,
    cover: true,
    lazyLoad: "nearby",
  }).mount();
}

if (typeof topslider__content != "undefined" && topslider__content != null) {
  new Splide(topslider__content, {
    perPage: 5,
    perMove: 1,
    preloadPages: perLoadCount,
    cover: true,
    pagination: false,
    interval: 4000,
    autoplay: false,
    lazyLoad: "nearby",
    breakpoints: {
      1920: {
        perPage: 8,
      },
      1550: {
        perPage: 7,
      },
      1280: {
        perPage: 6,
      },
      768: {
        perPage: 3,
      },
      480: {
        perPage: 2,
      },
    },
  }).mount();
}

// episodes slider must be top of other carosals for fixing offsetTop problem
if (
  typeof secondaryslider__content != "undefined" &&
  secondaryslider__content != null &&
  typeof primaryslider__content != "undefined" &&
  primaryslider__content != null
) {
  let secondarySlider = new Splide(secondaryslider__content, {
    gap: 20,
    cover: true,
    isNavigation: true,
    focus: 1,
    arrows: false,
    pagination: false,
    breakpoints: {
      1920: {
        perPage: 6,
        gap: "1.5rem",
      },

      1312: {
        perPage: 5,
        gap: "1rem",
      },
      992: {
        perPage: 4,
        gap: "1rem",
      },
      688: {
        perPage: 3,
        gap: "1rem",
      },
      480: {
        perPage: 2,
        gap: "1rem",
      },
    },
  }).mount();
  let primarySlider = new Splide(primaryslider__content, {
    type: "slide",
    heightRatio: 0.5,
    pagination: false,
    arrows: false,
    cover: true,
  }); // do not call mount() here.

  primarySlider.sync(secondarySlider).mount();

  //  localStorage.clear()
  let episodeWatchStatus = localStorage.episodeWatchStatus;

  if (episodeWatchStatus) {
    episodeWatchStatus = JSON.parse(episodeWatchStatus);
  } else {
    episodeWatchStatus = {};
  }
  seasonID = document.querySelector(".episode-main").dataset.seasonId;
  primarySlider.go(
    episodeWatchStatus[seasonID] ? episodeWatchStatus[seasonID] : 0
  );

  secondarySlider.on("click", function () {
    episodeWatchStatus[seasonID] = secondarySlider.index;
    localStorage.setItem(
      "episodeWatchStatus",
      JSON.stringify(episodeWatchStatus)
    );
  });
}

if (typeof stillpath__content != "undefined" && stillpath__content != null) {
  new Splide(stillpath__content, {
    perPage: 3,
    perMove: 1,
    gap: "1rem",
    preloadPages: perLoadCount,
    cover: true,
    pagination: false,
    lazyLoad: "nearby",
    breakpoints: {
      1920: {
        perPage: 6,
      },
      1400: {
        perPage: 5,
      },
      1200: {
        perPage: 4,
      },
      768: {
        perPage: 3,
      },
      480: {
        perPage: 2,
      },
    },
  }).mount();
}


const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        let carousel = entry.target;
        splide = new Splide(carousel, {
          perPage: 5,
          perMove: 1,
          preloadPages: perLoadCount,
          cover: true,
          pagination: false,
          lazyLoad: "nearby",
          gap: gap,
          breakpoints: {
            1920: {
              perPage: 7,
            },
            1400: {
              perPage: 6,
            },
            1200: {
              perPage: 5,
            },
            991: {
              perPage: 4,
            },
            768: {
              perPage: 3,
            },
            480: {
              perPage: 2,
            },
          },
        });
        splide.mount();
        carousel.classList.add("animate__fadeIn");
        observer.unobserve(entry.target);
      }
    });
  },
);
carousels.forEach((carousel) => {
  observer.observe(carousel);
});
