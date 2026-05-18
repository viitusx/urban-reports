// SIDEBAR TOGGLE

const menuToggle = document.getElementById("menuToggle");
const sidebar = document.getElementById("sidebar");

menuToggle.addEventListener("click", () => {
    sidebar.classList.toggle("collapsed");
});

// FADE IN ANIMATION

const fadeElements = document.querySelectorAll(".fade-in");

const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if(entry.isIntersecting){
            entry.target.classList.add("show");
        }

    });

});

fadeElements.forEach(element => {
    observer.observe(element);
});

// FUTURE DARK MODE STRUCTURE

function enableDarkMode(){
    document.body.classList.toggle("dark-mode");
}

// BUTTON EFFECTS

const buttons = document.querySelectorAll(".btn");

buttons.forEach(button => {

    button.addEventListener("mouseenter", () => {
        button.style.opacity = "0.9";
    });

    button.addEventListener("mouseleave", () => {
        button.style.opacity = "1";
    });

});