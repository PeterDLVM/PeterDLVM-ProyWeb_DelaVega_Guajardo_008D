$(document).ready(function() {
    // Validación de inicio de sesión
    function validateLoginForm() {
        var username = $("#username").val().trim();
        var password = $("#password").val().trim();

        if (username === "") {
            alert("Por favor, ingrese su nombre de usuario.");
            return false;
        }
        if (password === "") {
            alert("Por favor, ingrese su contraseña.");
            return false;
        }

        return true;
    }

    // Validación de suscripción
    function validateSubscribeForm(form) {
        var username = $(form).find("input[name='username']").val().trim();
        var email = $(form).find("input[name='email']").val().trim();
        var password = $(form).find("input[name='password']").val().trim();
        var birthDate = $(form).find("input[name='fecha_nacimiento']").val();

        if (username === "") {
            alert("Por favor, ingrese su nombre de usuario.");
            return false;
        }
        if (email === "") {
            alert("Por favor, ingrese su correo electrónico.");
            return false;
        }
        if (password === "") {
            alert("Por favor, ingrese su contraseña.");
            return false;
        }
        if (!validateEmail(email)) {
            alert("Por favor, ingrese un correo electrónico válido.");
            return false;
        }
        if (birthDate !== "" && !validateBirthDate(birthDate)) {
            alert("Por favor, ingrese una fecha de nacimiento válida.");
            return false;
        }

        return true;
    }

    // Función para validar el formato del correo electrónico
    function validateEmail(email) {
        var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Función para validar la fecha de nacimiento
    function validateBirthDate(birthDate) {
        var today = new Date();
        var selectedDate = new Date(birthDate);
        return selectedDate <= today;
    }

    // Asignar validaciones a los formularios
    $("#login-form").on("submit", function(event) {
        if (!validateLoginForm()) {
            event.preventDefault();
        }
    });

    $("form[action='#']").on("submit", function(event) {
        event.preventDefault(); // Para evitar el envío del formulario antes de las validaciones

        if (validateSubscribeForm(this)) {
            mostrarAlerta(); // Llamar a mostrarAlerta() solo si las validaciones pasan
            this.submit(); // Envía el formulario después de mostrar la alerta
        }
    });
});