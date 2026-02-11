function dibujarDiamanteHueco(n) {
    if (n % 2 === 0) return;

    let centro = Math.floor(n / 2);

    // Bucle para las FILAS (i)
    for (let i = 0; i < n; i++) {
        let linea = "";
        
        // Calculamos la distancia desde el centro para manejar la simetría
        // distVertical nos dice qué tan lejos estamos de la fila media
        let distVertical = i <= centro ? i : (n - 1) - i;

        // Bucle para las COLUMNAS (j)
        // Recorremos hasta el último asterisco necesario en esa fila
        let limiteColumnas = centro + distVertical;

        for (let j = 0; j <= limiteColumnas; j++) {
            // Lógica de impresión:
            // 1. Espacio exterior izquierdo: centro - distVertical
            // 2. Espacio interior: entre los dos puntos de asterisco
            if (j === centro - distVertical || j === centro + distVertical) {
                linea += "*";
            } else {
                linea += " ";
            }
        }
        console.log(linea);
    }
}

// Ejemplo con n = 7
dibujarDiamanteHueco(7);