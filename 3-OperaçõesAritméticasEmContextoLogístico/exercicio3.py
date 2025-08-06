#operacoes aritmeticas em contexto logístico
# Este programa realiza operações aritméticas básicas e exibe os resultados formatados.
km_por_dia = 30
gasto_diario = 300 
ano_2_digitos = 25

#   Operações Aritméticas
TotalSemana  = km_por_dia * 7 # total de km percorridos em uma semana
DiferencaEntre100EGastoDiario = 100 - gasto_diario #diferença entre 100 e gasto diário
DiasRodando = 500 // gasto_diario # dias rodando com base no gasto diário
PorcentagemGastoDiarioPor100 = 100 * (gasto_diario / 100) # porcentagem do gasto diário em relação a 100
MediaGastoDiarioPorKm =  gasto_diario / km_por_dia # média de gasto diário por km

print("Resultados das Operações Aritméticas")
print("-------------------------------------")
print(f"Total da Semana: {TotalSemana}, {type(TotalSemana)}")
print(f"Diferença entre 100 e Gasto Diário: {DiferencaEntre100EGastoDiario}, {type(DiferencaEntre100EGastoDiario)}")
print(f"Dias Rodando: {DiasRodando}, {type(DiasRodando)}")
print(f"Porcentagem de Gasto Diário por 100: {PorcentagemGastoDiarioPor100}, {type(PorcentagemGastoDiarioPor100)}")
print(f"Média de Gasto Diário por Km: {MediaGastoDiarioPorKm}, {type(MediaGastoDiarioPorKm)}")
print("-------------------------------------")