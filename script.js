const BASE_URL = "http://127.0.0.1:5000";
let token = "";

// Show backend response
function showOutput(data) {
    document.getElementById("output").textContent = JSON.stringify(data, null, 2);
}

// Screen switching
function showLogin() {
    document.getElementById("login-screen").style.display = "block";
    document.getElementById("register-screen").style.display = "none";
    document.getElementById("secret-screen").style.display = "none";
}

function showRegister() {
    document.getElementById("login-screen").style.display = "none";
    document.getElementById("register-screen").style.display = "block";
    document.getElementById("secret-screen").style.display = "none";
}

function showSecretScreen() {
    document.getElementById("login-screen").style.display = "none";
    document.getElementById("register-screen").style.display = "none";
    document.getElementById("secret-screen").style.display = "block";
}

// Logout
function logout() {
    token = "";
    showLogin();
}

// REGISTER
async function register() {
    const username = document.getElementById("reg-username").value;
    const password = document.getElementById("reg-password").value;

    const res = await fetch(`${BASE_URL}/register`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    showOutput(data);

    // Optional: send them back to login after success
    if (data.success === true) {
        showLogin();
    }
}

// LOGIN
async function login() {
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;

    const errorBox = document.getElementById("login-error");
    errorBox.textContent = ""; // clear old errors

    const res = await fetch(`${BASE_URL}/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    showOutput(data);

    if (data.success === true) {
        token = data.token || "";
        showSecretScreen();
    } else {
        errorBox.textContent = "❌ Incorrect username or password";
    }
}