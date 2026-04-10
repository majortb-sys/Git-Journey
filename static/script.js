let display = document.getElementById('display');

function appendToDisplay(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = '';
}

async function calculate() {
    const expression = display.value;
    if (!expression) return;

    try {
        const response = await fetch('/api/calc', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ expression })
        });
        const data = await response.json();
        display.value = data.result;
    } catch (error) {
        display.value = 'Error';
    }
}