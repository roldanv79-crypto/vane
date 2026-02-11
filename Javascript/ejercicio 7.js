let n = 5; // Tamaño del reloj
let resultado = "";

// --- Parte Superior (Incluyendo la cintura) ---
for (let i = 0; i < n; i++) {
    // 1. Agregar espacios iniciales
    for (let j = 0; j < i; j++) {
        resultado += " ";
    }
    // 2. Agregar números (cantidad decreciente: 2*(n-i)-1)
    for (let k = 0; k < (n - i) * 2 - 1; k++) {
        resultado += (n - i);
    }
    resultado += "\n";
}

// --- Parte Inferior (Creciente) ---
for (let i = 2; i <= n; i++) {
    // 1. Agregar espacios iniciales
    for (let j = 0; j < n - i; j++) {
        resultado += " ";
    }
    // 2. Agregar números (cantidad creciente: 2*i - 1)
    for (let k = 0; k < 2 * i - 1; k++) {
        resultado += i;
    }
    resultado += "\n";
}

console.log(resultado);