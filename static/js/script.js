document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('clientForm');
    const clientList = document.getElementById('clientList');

    // Function to save client data to localStorage
    function saveClient(name, phone) {
        let clients = JSON.parse(localStorage.getItem('clients')) || [];
        clients.push({ name, phone });
        localStorage.setItem('clients', JSON.stringify(clients));
    }

    // Function to display clients
    function displayClients() {
        let clients = JSON.parse(localStorage.getItem('clients')) || [];
        clientList.innerHTML = '';
        clients.forEach(client => {
            const li = document.createElement('li');
            li.textContent = `Nombre: ${client.name}, Teléfono: ${client.phone}`;
            clientList.appendChild(li);
        });
    }

    // Handle form submission
    if (form) {
        form.addEventListener('submit', event => {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const phone = document.getElementById('phone').value;
            saveClient(name, phone);
            alert('Cliente registrado correctamente.');
            form.reset();
        });
    }

    // Display clients if on clients.html
    if (clientList) {
        displayClients();
    }
});
