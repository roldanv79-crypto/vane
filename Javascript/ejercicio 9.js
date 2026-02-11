function validarTarjeta(numero) {
    let sumaTotal = 0;
    let posicion = 1; // Para rastrear si la posición es par o impar (de derecha a izquierda)
    let numeroTemporal = numero;

    // Recorremos el número matemáticamente hasta que no queden dígitos
    while (numeroTemporal > 0) {
        // Extraemos el último dígito
        let digito = numeroTemporal % 10;

        // Según Luhn, se duplican los dígitos en posiciones pares (contando desde la derecha)
        // Nota: En un número de 8 dígitos, las posiciones pares desde la derecha son 2, 4, 6, 8.
        if (posicion % 2 === 0) {
            digito *= 2;
            
            // Si el resultado es > 9, restamos 9 (equivalente a sumar sus dígitos)
            if (digito > 9) {
                digito -= 9;
            }
        }

        sumaTotal += digito;

        // Eliminamos el último dígito del número (división entera)
        numeroTemporal = (numeroTemporal - (numeroTemporal % 10)) / 10;
        posicion++;
    }

    // Es válida si la suma total es múltiplo de 10
    return sumaTotal % 10 === 0;
}

// Pruebas:
console.log(validarTarjeta(49927398)); // Ejemplo de número que cumple la lógica