function sonAmigos(a, b) {
    // Un número no puede ser amigo de sí mismo según la definición estándar
    if (a === b) return false;

    let sumaA = 0;
    let sumaB = 0;

    // Calculamos los divisores propios de 'a'
    // Un divisor propio es menor al número mismo, por eso i < a
    for (let i = 1; i < a; i++) {
        if (a % i === 0) {
            sumaA += i;
        }
    }

    // Calculamos los divisores propios de 'b'
    for (let j = 1; j < b; j++) {
        if (b % j === 0) {
            sumaB += j;
        }
    }

    // Verificamos la condición de reciprocidad
    if (sumaA === b && sumaB === a) {
        return true;
    } else {
        return false;
    }
}

// Ejemplo de prueba con el par de números amigos más conocido: 220 y 284
console.log(sonAmigos(220, 284)); // true
console.log(sonAmigos(1184, 1210)); // true
console.log(sonAmigos(10, 20)); // false