// ==========================
// SIDEBAR TOGGLE
// ==========================
const menuToggle = document.querySelector("#menuToggle");
const sidebar = document.querySelector("#sidebar");

if (menuToggle && sidebar) {
    menuToggle.addEventListener("click", () => {
        sidebar.classList.toggle("collapsed");
    });
}


// ==========================
// FADE-IN COM INTERSECTION OBSERVER
// ==========================
const fadeInObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
            fadeInObserver.unobserve(entry.target); // melhora performance
        }
    });
}, {
    threshold: 0.2
});

document.querySelectorAll(".fade-in").forEach(el => {
    fadeInObserver.observe(el);
});


// ==========================
// DARK MODE (COM LOCAL STORAGE)
// ==========================
const darkModeToggle = document.querySelector("#darkModeToggle");

function applyDarkMode(isDark) {
    document.body.classList.toggle("dark-mode", isDark);
    localStorage.setItem("darkMode", isDark);
}

// carregar preferência salva
const savedDarkMode = localStorage.getItem("darkMode") === "true";
applyDarkMode(savedDarkMode);

if (darkModeToggle) {
    darkModeToggle.addEventListener("click", () => {
        const isDark = !document.body.classList.contains("dark-mode");
        applyDarkMode(isDark);
    });
}


// ==========================
// EFEITO DE BOTÕES (COM CSS MELHOR)
// ==========================
document.querySelectorAll(".btn").forEach(button => {
    button.addEventListener("mouseenter", () => {
        button.style.transform = "scale(1.03)";
    });

    button.addEventListener("mouseleave", () => {
        button.style.transform = "scale(1)";
    });
});


// ==========================
// SCROLL SUAVE
// ==========================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            target.scrollIntoView({
                behavior: "smooth"
            });
        }
    });
});


// ==========================
// FUTURO: INTEGRAÇÃO COM API (DENÚNCIAS)
// ==========================

async function criarDenuncia(dados) {
    try {
        const response = await fetch("http://127.0.0.1:5000/denuncias/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        });

        const result = await response.json();
        console.log("Denúncia criada:", result);

    } catch (error) {
        console.error("Erro ao criar denúncia:", error);
    }
}