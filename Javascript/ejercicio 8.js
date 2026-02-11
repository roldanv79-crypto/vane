function calcularDiaDelAño(dia, mes, año) {
    // 1. Validar si el año es bisiesto
    // Un año es bisiesto si es divisible por 4 Y (no es divisible por 100 O es divisible por 400)
    let esBisiesto = false;
    if ((año % 4 === 0 && año % 100 !== 0) || (año % 400 === 0)) {
        esBisiesto = true;
    }

    let diaDelAño = 0;

    // 2. Sumar los días de los meses anteriores usando un switch con "fallthrough"
    // Al no poner 'break', el caso 12 sumará todos los meses anteriores, el 11 sumará hasta octubre, etc.
    switch (mes - 1) {
        case 11: diaDelAño += 30; // Noviembre
        case 10: diaDelAño += 31; // Octubre
        case 9:  diaDelAño += 30; // Septiembre
        case 8:  diaDelAño += 31; // Agosto
        case 7:  diaDelAño += 31; // Julio
        case 6:  diaDelAño += 30; // Junio
        case 5:  diaDelAño += 31; // Mayo
        case 4:  diaDelAño += 30; // Abril
        case 3:  diaDelAño += 31; // Marzo
        case 2:  diaDelAño += (esBisiesto ? 29 : 28); // Febrero
        case 1:  diaDelAño += 31; // Enero
    }

    // 3. Sumar los días del mes actual
    diaDelAño += dia;

    return diaDelAño;
}

// Ejemplos de prueba:
console.log(calcularDiaDelAño(1, 2, 2024));   // Resultado: 32 (Bisiesto)
console.log(calcularDiaDelAño(31, 12, 2023)); // Resultado: 365
console.log(calcularDiaDelAño(31, 12, 2024)); // Resultado: 366