# importante:
Si no carga a la primera, recargar.

# core Carlos Freire:
Módulo bancario de prestamos (método alemán) en flask

# Descripción:
* Estilos con bootstrap flask
* Index: botón iniciar sesión y registrarse
* Autenticación de usuarios con flask-login
* Token de seguridad, clave secreta cifrada, contraseñas hasheadas
* Cerrar sesión correctamente.
* base de datos en MySQL (usuario) (prestamo) relación un usuario puede tener muchos préstamos
* Administración (crud) ir a: https://core_f-codefreire.pythonanywhere.com/admin
* Usuarios de prueba (no eliminar): (usuario: caja, contraseña: 789789) (usuario: user, contraseña: 123123) (usuario: user2, contraseña: 456456)
* 2 roles de usuario: 1 para banco y 2 para cliente (asignar en la administración)
* El usuario con rol banco ingresa un nuevo préstamo al usuario
* El usuario con rol cliente si no tiene préstamos se le muestra un mensaje de que no los tiene.
* Si el usuario con rol cliente tiene uno o más préstamos, se muestra un selector para seleccionar el
préstamo y una ves seleccionado clic en Aceptar y se le despliega la tabla (método alemán) con sus respectivos periodos
* En el navbar clic en la palabra bienvenido para ir a la página del usuario.
* En el navbar si tiene el usuario préstamos, aparece a lado de cerrar sesión, el apartado de reporte
clic para ir a la sección de reporte
* El reporte filtra los periodos cuya cuota está entre los valores ingresados.
* En reporte ingresar los valores y presionar generar reporte para ver el resultado.

# Repositorio github:
https://github.com/codefreire/core_f

# URL despliegue:
https://core_f-codefreire.pythonanywhere.com/

# Flask documentación
https://flask.palletsprojects.com/en/1.1.x/

# Base de datos relacional con flask
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

# hosting gratuito para python
https://www.pythonanywhere.com/

# Contacto:
Nombre: Carlos Freire
email: carlos.freire.yanez@udla.edu.ec
