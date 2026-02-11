function binarioADecimal(numeroBinario) {
  let decimal = 0;
  let multiplicador = 1; // Representa 2^0, luego 2^1, 2^2, etc.

  // Mientras el número sea mayor a 0, seguimos extrayendo dígitos
  while (numeroBinario > 0) {
    // 1. Extraemos el último dígito (el residuo de dividir entre 10)
    let ultimoDigito = numeroBinario % 10;

    // 2. Si el dígito es 1, sumamos el valor de la potencia actual
    if (ultimoDigito === 1) {
      decimal = decimal + multiplicador;
    }

    // 3. Eliminamos el último dígito del número original
    // Usamos Math.floor para asegurar que la división sea entera
    numeroBinario = Math.floor(numeroBinario / 10);

    // 4. Duplicamos el multiplicador para la siguiente posición (potencia de 2)
    multiplicador = multiplicador * 2;
  }

  return decimal;
}

// Ejemplo de uso:
const binario = 1011;
const resultado = binarioADecimal(binario);
console.log("El decimal de " + binario + " es: " + resultado); 
// Salida: 11
