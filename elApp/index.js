const button = document.getElementById('load-btn');
const resultDiv = document.getElementById('result');

button.addEventListener('click', async () => {
    resultDiv.innerText = 'Loading...';

    try {
        const res = await fetch('http://127.0.0.1:8000/api/CATspirations');

        if (!res.ok) {
            throw new Error('Error: ${res.status}');
        }

            const data = await res.json();

            resultDiv.innerText = JSON.stringify(data, null, 2);
        
        } catch (error) {
            resultDiv.innerText = `Error: ${error.message}`;
            console.error(error);
        }
});
