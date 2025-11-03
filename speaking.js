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
