def calc_desc(precio):
    if precio>10000:
        return f" se aplica descuento, el valor es: {precio-precio*0.1}"
    else:
        return f"no se aplica descuento, el valor es {precio}"

print(calc_desc(30000))


print("---Version de Gemini---")
def calcular_descuento(precio):
    # Verificamos si el precio supera el límite para el descuento
    if precio > 10000:
        # Calculamos el 10% de descuento restándoselo al precio original
        return precio - (precio * 0.1)
    else:
        # Si no supera los 10000, devolvemos el precio intacto
        return precio

# --- Pruebas y visualización ---

# Caso 1: Supera los 10000 (aplica descuento)
precio_original_1 = 30000
precio_final_1 = calcular_descuento(precio_original_1)
print(f"Precio original: ${precio_original_1} -> Precio final con descuento: ${precio_final_1}")

# Caso 2: No supera los 10000 (mantiene el precio)
precio_original_2 = 5000
precio_final_2 = calcular_descuento(precio_original_2)
print(f"Precio original: ${precio_original_2} -> Precio final sin descuento: ${precio_final_2}")
