modelos = ["SkyLine", "Gtr", "X6", "Lambo", "Opala"]
consumo_km_litro = [7.0, 10.0, 12.5, 9.0, 14.5]
preco_gasolina = 4.10

print("Comparativo de Consumo de Combustível:")
print("------------------------------------------------")

for i in range(len(modelos)):
    print(f"Veiculo {i + 1}")
    print(f"Nome: {modelos[i]}")
    print(f"Km por litro: {consumo_km_litro[i]:.1f}")
    
    litros_para_1000_km = 1000 / consumo_km_litro[i]
    custo_para_1000_km = litros_para_1000_km * preco_gasolina
    
    print(f"Litros para percorrer 1000 km: {litros_para_1000_km:.1f} litros")
    print(f"Custo para percorrer 1000 km: R$ {custo_para_1000_km:.2f}")
    print("------------------------------------------------")

indice_mais_economico = consumo_km_litro.index(max(consumo_km_litro))
print(f"O veículo mais econômico e o {modelos[indice_mais_economico]}")