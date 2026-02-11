let numero = 12; // Número a evaluar
let divisor = 2;

// Usamos un bucle para reducir el número hasta que llegue a 1
while (numero > 1) {
    // Requerimiento: Dividir por el divisor tantas veces como sea posible
    while (numero % divisor === 0) {
        console.log(divisor);
        numero = numero / divisor;
    }
    
    // Cuando ya no es divisible, incrementamos el divisor
    divisor++;
}