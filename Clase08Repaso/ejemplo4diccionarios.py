# EJ4: Crear un diccionario que represente una cuenta de usuario con:
# ● usuario
# ● email
# ● activo
# Luego:
# 1. Mostrar el email del usuario.
# 2. Cambiar el estado activo a False.
# 3. Agregar una nueva clave llamada ultimo_login.
# 4. Mostrar el diccionario completo.

cuenta = {
    "usuario": "richard",
    "email": "monitofutbolero@gmail.com",
    "activo": True
}
print(cuenta["email"])
cuenta["activo"] = False
cuenta["ultimo_login"] = "hoy"
print(cuenta)