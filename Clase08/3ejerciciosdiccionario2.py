cuenta={
    "usuario": "richard",
    "email": "monitofutbolero@gmail.com",
    "activo": True
}
print(cuenta["email"])
print(cuenta)
cuenta["activo"]=False
print(cuenta)
cuenta["ultimo login"] = (6, 5, 2026)
print(cuenta)