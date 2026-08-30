import TP4conversores

mts=3
cm=3
hs=3

conversionmts = TP4conversores.mts_a_cm(mts)
conversioncm = TP4conversores.cm_a_mm(cm)
conversionhs = TP4conversores.hs_a_min(hs)
print(f"{mts} metro/s son {conversionmts} centimetros")
print(f"{cm} centimetro/s son {conversioncm} milimetros")
print(f"{hs} hora/s son {conversionhs} minutos")    