function mostrarRanking() {
    fetch('http://localhost:3000/productos')
        .then(response => response.json())
        .then(data => mostrarProductos(data))
        .catch(error => console.error('Error al cargar el ranking:', error));
}

function buscarTipo() {
    const tipo = document.getElementById('tipo').value.toLowerCase();
    console.log("Tipo seleccionado:", tipo);

    // Ocultar todas las filas
    document.querySelectorAll('#mascotas tr').forEach(fila => fila.style.display = 'none');

    let contador = 0; // contador de filar, mayormente es para ver si filtraba 

    // visualizar las filas que coinciden con el tipo seleccionado
    document.querySelectorAll('#mascotas tr').forEach(fila => {
        const mascota = fila.querySelector('td:nth-child(5)').textContent.toLowerCase();
        console.log("Mascota de la fila:", mascota);

        if (tipo === '' || mascota.includes(tipo)) {
            fila.style.display = ''; // visualizar la fila si coincide con el tipo seleccionado o si no se seleccionó ningún tipo
            contador++; // incrementar el contador
        }
    });
    //mostrar contador
    document.getElementById('contador').innerText = contador;
}

function mostrarProductos(data) {
    const tbody = document.getElementById('mascotas');
    tbody.innerHTML = ''; // limpiar la tabla antes de agregar nuevos productos

    // generar valores aleatorios en formato estrellas
    data.forEach(producto => {
        producto.estrellas = Math.floor(Math.random() * (producto.estrellas.max - producto.estrellas.min + 1)) + producto.estrellas.min;
    });

    // ordenar los productos según el ranking de estrellas
    data.sort((a, b) => b.estrellas - a.estrellas);

    // mostrar los productos ordenados en la tabla
    data.forEach(producto => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${producto.id}</td>
            <td>${producto.nombre}</td>
            <td>${producto.precio}</td>
            <td>${producto.observacion}</td>
            <td>${Array.isArray(producto.mascota) ? producto.mascota.join(', ') : producto.mascota}</td>
            <td>${producto.estrellas} <span>&#9733;</span></td> <!-- Agregamos un icono de estrella al lado del número de estrellas -->
        `;
        tbody.appendChild(tr);
    });
}

document.getElementById('tipo').addEventListener('change', buscarTipo);