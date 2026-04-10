const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");

if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => {
        navLinks.classList.toggle("open");
    });
}

const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    },
    { threshold: 0.2 },
);

document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));

const slider = document.querySelector("[data-slider]");
if (slider) {
    const slides = Array.from(slider.querySelectorAll("[data-slide]"));
    const prevButton = slider.querySelector("[data-slider-prev]");
    const nextButton = slider.querySelector("[data-slider-next]");
    let currentIndex = slides.findIndex((slide) => slide.classList.contains("is-active"));
    if (currentIndex < 0) currentIndex = 0;

    const showSlide = (index) => {
        slides.forEach((slide, i) => {
            slide.classList.toggle("is-active", i === index);
        });
        currentIndex = index;
    };

    const nextSlide = () => {
        const nextIndex = (currentIndex + 1) % slides.length;
        showSlide(nextIndex);
    };

    const prevSlide = () => {
        const prevIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(prevIndex);
    };

    if (nextButton) nextButton.addEventListener("click", nextSlide);
    if (prevButton) prevButton.addEventListener("click", prevSlide);

    setInterval(nextSlide, 3000);
}

/* ===== ADD THIS AT VERY BOTTOM ===== */
window.toggleMenu = function(id) {
    let current = document.getElementById("menu-" + id);

    document.querySelectorAll(".menu-items").forEach(menu => {
        if (menu !== current) {
            menu.style.display = "none";
        }
    });

    current.style.display =
        current.style.display === "block" ? "none" : "block";
}