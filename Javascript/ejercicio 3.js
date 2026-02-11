function calcularRaizEntera(n) {
    // Casos base para números negativos y cero
    if (n < 0) return "No existe raíz real";
    if (n === 0 || n === 1) return n;

    let i = 1;
    let resultado = 1;

    // Buscamos el número que al elevarlo al cuadrado no supere a n
    while (resultado <= n) {
        i++;
        resultado = i * i;
    }

    // Retornamos i - 1 porque el bucle se detiene cuando ya se pasó de n
    return i - 1;
}

// Ejemplo de uso:
const numero = 27;
console.log("La parte entera de la raíz de " + numero + " es: " + calcularRaizEntera(numero));