// Adding & Removing nav bar styles on scroll
document.addEventListener("DOMContentLoaded", () => {
  const navContainer = document.querySelector(".home-nav-container");
  const headerImage = document.querySelector("header img");

  if (navContainer && headerImage) {
    const headerHeight = headerImage.offsetHeight;

    window.addEventListener("scroll", () => {
      if (window.scrollY > headerHeight) {
        navContainer.classList.add("scrolled-nav");
      } else {
        navContainer.classList.remove("scrolled-nav");
      }
    });
  }
});

// INVERTS BOOK SWETHA BTN COLOR WHEN INSIDE FOOTER
document.addEventListener("DOMContentLoaded", function () {
  const bookButton = document.querySelector(".book-swetha");
  const footer = document.querySelector("footer");

  if (!bookButton || !footer) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          bookButton.classList.add("footer-visible");
        } else {
          bookButton.classList.remove("footer-visible");
        }
      });
    },
    {
      root: null, // viewport
      threshold: 0.2, // adjust sensitivity if needed
    }
  );

  observer.observe(footer);
});
