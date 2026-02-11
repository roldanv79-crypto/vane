function invertirNumero(n) {
    let acumulador = 0;
    let esNegativo = n < 0;

    // Trabajamos con el valor absoluto para simplificar la lógica del bucle
    if (esNegativo) {
        n = n * -1;
    }

    while (n > 0) {
        // 1. Extraemos el último dígito
        let ultimoDigito = n % 10;

        // 2. Desplazamos lo acumulado a la izquierda y sumamos el dígito
        acumulador = (acumulador * 10) + ultimoDigito;

        // 3. Eliminamos el último dígito del número original
        // Usamos Math.floor para asegurar que la división sea entera
        n = Math.floor(n / 10);
    }

    // Si el original era negativo, devolvemos la inversión también negativa
    return esNegativo ? (acumulador * -1) : acumulador;
}

// Pruebas
console.log(invertirNumero(1234)); // Resultado: 4321
console.log(invertirNumero(987));  // Resultado: 789
console.log(invertirNumero(-561)); // Resultado: -165