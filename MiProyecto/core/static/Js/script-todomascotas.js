function agregarAlCarrito() {
    let cantidadCarrito = parseInt(document.getElementById("cantidad-carrito").textContent);
    cantidadCarrito++;
    document.getElementById("cantidad-carrito").textContent = cantidadCarrito;
}
function quitarDelCarrito() {
    let cantidadCarrito = parseInt(document.getElementById("cantidad-carrito").textContent);
    if (cantidadCarrito > 0) {
        cantidadCarrito--;
        document.getElementById("cantidad-carrito").textContent = cantidadCarrito;
    }
}

document.addEventListener("DOMContentLoaded", function() {
  var usuarioIcono = document.getElementById("usuario-icono");
  var modal = document.getElementById("modal");

  // Cuando se haga clic en el icono de usuario, mostrar la ventana emergente
  usuarioIcono.onclick = function () {
    modal.style.display = "block";
  }

  // Obtener el elemento de cierre de la ventana emergente
  var closeButton = document.getElementsByClassName("close")[0];

  // Cuando se haga clic en el botón de cierre, ocultar la ventana emergente
  closeButton.onclick = function () {
    modal.style.display = "none";
  }

  // Cuando el usuario haga clic fuera de la ventana emergente, ocultarla
  window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
      }
  }
});

// Función que se ejecuta al hacer clic en el botón de registrarse
function registrarseycerrarmodal() {
  // Almacenar una bandera en el almacenamiento local para indicar que queremos desplazarnos a 'suscribete'
  localStorage.setItem('scrollToSuscribete', 'true');
  
  // Redirigir a la página principal (index)
  window.location.href = "/";
}

// Escuchar el evento de carga de la página para desplazarse si es necesario
document.addEventListener('DOMContentLoaded', function () {
  // Verificar si la bandera está configurada en el almacenamiento local
  if (localStorage.getItem('scrollToSuscribete') === 'true') {
      // Desplazarse a la sección 'suscribete'
      var suscribeteSection = document.getElementById('suscribete');
      if (suscribeteSection) {
          suscribeteSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      } else {
          console.log("La sección 'suscribete' no fue encontrada en la página.");
      }
      
      // Limpiar la bandera del almacenamiento local
      localStorage.removeItem('scrollToSuscribete');
  }
});
function mostrarAlerta() {
  alert("¡Muchas gracias por suscribirte!");
}
function iniciarSesion() {
  console.log("Iniciando sesión...");

  var nombreUsuario = document.getElementById("username").value;
  var contrasena = document.getElementById("password").value;

  if (nombreUsuario !== "" && contrasena !== "") {
    localStorage.setItem('username', nombreUsuario);
    document.getElementById("nombre-usuario").innerText = nombreUsuario;
    document.getElementById("usuario-info").style.display = "inline";
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";

    cerrarModal(); 
    //funcion dentro de iniciar sesion para determinar el saludo dia,tarde, noche..
    var fecha = new Date();
    var hora = fecha.getHours();
    var mensaje;

    if (hora >= 5 && hora <= 12) {
      mensaje = "¡Buenos días, " + nombreUsuario + "! Que tengas un excelente día.";
    } else if (hora > 12 && hora <= 18) {
      mensaje = "¡Buenas tardes, " + nombreUsuario + "! Espero que estés teniendo una buena tarde.";
    } else {
      mensaje = "¡Buenas noches, " + nombreUsuario + "! Que tengas una buena noche.";
    }

    alert(mensaje);
  } else {
    alert("Por favor, ingrese su nombre de usuario y contraseña.");
  }
}

function cerrarModal() {
  console.log("Cerrando modal...");
  document.getElementById("modal").style.display = "none";
}
function cerrarSesion() {
  window.location.href = "{% url 'logout' %}";
  alert("¡Gracias por preferirnos! Esperamos verte pronto de nuevo.");
}
function actualizarReloj() {
  const ahora = new Date();
  const hora = ahora.getHours().toString().padStart(2, '0');
  const minutos = ahora.getMinutes().toString().padStart(2, '0');
  const segundos = ahora.getSeconds().toString().padStart(2, '0');
  const tiempo = `${hora}:${minutos}:${segundos}`;
  document.getElementById('reloj').textContent = tiempo;
}

// Llamar a la función para mostrar el reloj inicialmente
actualizarReloj();

// Actualizar el reloj cada segundo
setInterval(actualizarReloj, 1000);
function irA(url) {
  window.location.href = url;
}