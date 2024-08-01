const x = document.querySelector('#x');
const y = document.querySelector('#languageSelect');
const form = document.querySelector('form');
const result = document.querySelector('#result');
const url = 'http://127.0.0.1:5000/add'; 

form.addEventListener('submit', (event) => {
    const x_value = x.value;
    const y_value = y.value;
    
    const request_options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ x: x_value, languageSelect: y_value }) 
    };

    fetch(url, request_options)
        .then(response => response.json())
        .then(data => {
            result.innerHTML = data.output; 
        })
        .catch(err => console.log(err));
    
    event.preventDefault();
});
