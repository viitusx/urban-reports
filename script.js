/* ============================================================
   script.js — SDU | Funções compartilhadas entre todas as páginas
   ============================================================ */

const API = "http://127.0.0.1:5000";


// ── SIDEBAR ──────────────────────────────────────────────────
const sidebar    = document.getElementById("sidebar");
const menuToggle = document.getElementById("menuToggle");

if (sidebar) {
    if (menuToggle) {
        menuToggle.addEventListener("click", (e) => {
            e.stopPropagation();
            sidebar.classList.add("collapsed");
        });
    }

    sidebar.addEventListener("click", () => {
        if (sidebar.classList.contains("collapsed")) {
            sidebar.classList.remove("collapsed");
        }
    });

    sidebar.querySelectorAll(".menu-item").forEach(item => {
        item.addEventListener("click", e => e.stopPropagation());
    });
}


// ── AUTENTICAÇÃO ─────────────────────────────────────────────
/**
 * Verifica se o usuário está logado consultando a sessão no servidor.
 * Se não estiver, redireciona para login.html.
 * Retorna os dados do usuário para uso na página.
 */
async function verificarAuth() {
    try {
        const resp = await fetch(`${API}/auth/me`, { credentials: "include" });

        if (resp.status === 401) {
            window.location.href = "login.html";
            return null;
        }

        const usuario = await resp.json();

        // Exibe o nome do usuário na topbar, se o elemento existir
        const elNome = document.getElementById("nome-usuario");
        if (elNome) elNome.textContent = usuario.nome;

        return usuario;
    } catch {
        window.location.href = "login.html";
        return null;
    }
}

async function sair() {
    await fetch(`${API}/auth/logout`, { method: "POST", credentials: "include" });
    window.location.href = "login.html";
}


// ── TOAST (notificação rápida) ───────────────────────────────
function mostrarToast(msg, duracao = 3000) {
    let toast = document.getElementById("toast");
    if (!toast) {
        toast = document.createElement("div");
        toast.id = "toast";
        toast.className = "toast";
        document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.classList.add("mostrar");
    setTimeout(() => toast.classList.remove("mostrar"), duracao);
}


// ── UTILITÁRIOS DE API ───────────────────────────────────────
async function buscarDenuncias() {
    const resp = await fetch(`${API}/denuncias`, { credentials: "include" });
    if (!resp.ok) throw new Error("Erro ao buscar denúncias.");
    return resp.json();
}

async function criarDenuncia(dados) {
    const resp = await fetch(`${API}/denuncias`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(dados),
    });
    if (!resp.ok) {
        const erro = await resp.json();
        throw new Error(erro.erro || "Erro ao criar denúncia.");
    }
    return resp.json();
}

async function atualizarDenuncia(id, dados) {
    const resp = await fetch(`${API}/denuncias/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(dados),
    });
    if (!resp.ok) throw new Error("Erro ao atualizar denúncia.");
    return resp.json();
}

async function excluirDenuncia(id) {
    const resp = await fetch(`${API}/denuncias/${id}`, {
        method: "DELETE",
        credentials: "include",
    });
    if (!resp.ok) throw new Error("Erro ao excluir denúncia.");
    return resp.json();
}
