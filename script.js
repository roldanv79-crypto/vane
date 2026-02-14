let currentOperand = '0';
let previousOperand = '';
let operation = undefined;

const currentText = document.getElementById('current-operand');
const previousText = document.getElementById('previous-operand');
const historyList = document.getElementById('history-list');

function updateDisplay() {
    currentText.innerText = currentOperand;
    if (operation != null) {
        let opDisplay = operation === '**' ? '^' : operation;
        previousText.innerText = `${previousOperand} ${opDisplay}`;
    } else {
        previousText.innerText = previousOperand;
    }
}

function appendNumber(number) {
    if (number === Math.PI) {
        currentOperand = parseFloat(Math.PI.toFixed(8)).toString();
    } else if (number === '.' && currentOperand.includes('.')) {
        return;
    } else if (currentOperand === '0' && number !== '.') {
        currentOperand = number.toString();
    } else {
        currentOperand = currentOperand.toString() + number.toString();
    }
    updateDisplay();
}

function appendOperator(op) {
    if (currentOperand === '') return;
    if (previousOperand !== '') calculate();
    operation = op;
    previousOperand = currentOperand;
    currentOperand = '';
    updateDisplay();
}

function appendScientific(func) {
    let val = parseFloat(currentOperand);
    if (isNaN(val)) return;
    let result;
    switch(func) {
        case 'sin': result = Math.sin(val * Math.PI / 180); break;
        case 'cos': result = Math.cos(val * Math.PI / 180); break;
        case 'tan': result = Math.tan(val * Math.PI / 180); break;
        case 'log': result = Math.log10(val); break;
        case 'sqrt': result = Math.sqrt(val); break;
        case 'exp': result = Math.exp(val); break;
    }
    
    addToHistory(`${func}(${currentOperand}) = ${parseFloat(result.toFixed(8))}`);
    currentOperand = parseFloat(result.toFixed(8)).toString();
    operation = undefined;
    previousOperand = '';
    updateDisplay();
}

function calculate() {
    let result;
    const prev = parseFloat(previousOperand);
    const current = parseFloat(currentOperand);
    if (isNaN(prev) || isNaN(current)) return;

    switch (operation) {
        case '+': result = prev + current; break;
        case '-': result = prev - current; break;
        case '*': result = prev * current; break;
        case '/': result = current === 0 ? "Error" : prev / current; break;
        case '%': result = (prev / 100) * current; break;
        case '**': result = Math.pow(prev, current); break;
        default: return;
    }

    if (result !== "Error") {
        let opLabel = operation === '**' ? '^' : operation;
        addToHistory(`${prev} ${opLabel} ${current} = ${result}`);
    }

    currentOperand = result.toString();
    operation = undefined;
    previousOperand = '';
    updateDisplay();
}

function addToHistory(entry) {
    const li = document.createElement('li');
    li.innerText = entry;
    historyList.prepend(li);
    if (historyList.children.length > 5) historyList.lastChild.remove();
}

function clearDisplay() {
    currentOperand = '0';
    previousOperand = '';
    operation = undefined;
    updateDisplay();
}

function deleteNumber() {
    if (currentOperand === '0') return;
    currentOperand = currentOperand.toString().slice(0, -1) || '0';
    updateDisplay();
}