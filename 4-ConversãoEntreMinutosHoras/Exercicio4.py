# Conversão de Minutos para Horas
ano_2_digitos = 25
tempo_minutos = 150 + ano_2_digitos
tempo_horas = 2.25


print("Conversão de Tempo")
print("-----------------")      
total_horas = tempo_minutos / 60  # Convertendo minutos para horas
print(f"tempo em minutos convertido para horas: {total_horas:.2f} horas")

total_em_minutos = tempo_horas * 60  # Convertendo horas de volta para minutos
print(f"tempo em horas convertido de volta para minutos: {total_em_minutos:.0f} minutos")
print("-----------------")
print("Conversão realizada com sucesso!")