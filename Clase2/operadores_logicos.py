monto=900
cliente_vip=False
cupon=True

if (monto>1000 and cliente_vip) or cupon: #el parentesis cambia la jerarquia en que se aplican las operaciones
    print("se aplica descuento")
else:
    print("no hay descuento ñao ñao")