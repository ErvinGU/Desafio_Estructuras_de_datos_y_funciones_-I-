import sys

if len(sys.argv) != 5:
    print("<tasa_sol> <tasa_peso_argentino> <tasa_dolar> <monto_clp>")
    sys.exit(1)


tasa_sol = float(sys.argv[1])
tasa_peso_argentino = float(sys.argv[2])
tasa_dolar = float(sys.argv[3])
monto_clp = float(sys.argv[4])


soles = monto_clp * tasa_sol
pesos_argentinos = monto_clp * tasa_peso_argentino
dolares = monto_clp * tasa_dolar


print(f"Los {monto_clp:.0f} pesos equivalen a:")
print(f"{soles:.1f} Soles")
print(f"{pesos_argentinos:.1f} Pesos Argentinos")
print(f"{dolares:.1f} Dólares")
