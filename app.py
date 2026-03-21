# --- calculadora de consumo elétrico ---
print("Calculadora de consumo elétrico")
aparelho = input("Nome do aparelho: ")
watts = float(input("Potência do aparelho (em watts): "))
horas_dias = float(input("Quantas horas por dia o aparelho fica ligado: "))

consumo_mensal = (watts * horas_dias * 30) / 1000

gasto_mensal = consumo_mensal * 0.8

print(f"\nAparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Gasto mensal estimado: R${gasto_mensal:.2f}")