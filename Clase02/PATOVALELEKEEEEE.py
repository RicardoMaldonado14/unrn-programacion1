documento=bool(input("trajiste documento? SI/NO ")=="SI")
if documento==True:
    edad=int(input("edad del wachin: "))
    if edad>=18 and documento==True:
        print("pasa pibe")
    else:
        print("no podes pasar")
else:
    print("no podes pasar")