function cajeroAutomatico(monto) {
    let montoRestante = monto;
    let cantidad;

    // --- Billetes de 100 ---
    cantidad = (montoRestante - (montoRestante % 100)) / 100;
    if (cantidad > 0) {
        console.log(cantidad + " billetes de 100");
    }
    montoRestante %= 100;

    // --- Billetes de 50 ---
    cantidad = (montoRestante - (montoRestante % 50)) / 50;
    if (cantidad > 0) {
        console.log(cantidad + " billetes de 50");
    }
    montoRestante %= 50;

    // --- Billetes de 20 ---
    cantidad = (montoRestante - (montoRestante % 20)) / 20;
    if (cantidad > 0) {
        console.log(cantidad + " billetes de 20");
    }
    montoRestante %= 20;

    // --- Billetes de 10 ---
    cantidad = (montoRestante - (montoRestante % 10)) / 10;
    if (cantidad > 0) {
        console.log(cantidad + " billetes de 10");
    }
    montoRestante %= 10;

    // --- Billetes de 5 ---
    cantidad = (montoRestante - (montoRestante % 5)) / 5;
    if (cantidad > 0) {
        console.log(cantidad + " billetes de 5");
    }
    montoRestante %= 5;

    // --- Billetes de 1 ---
    cantidad = montoRestante; // Lo que queda son billetes de 1
    if (cantidad > 0) {
        console.log(cantidad + " billetes de 1");
    }
}

// Ejemplo de prueba:
console.log("Retiro de 388:");
cajeroAutomatico(388);