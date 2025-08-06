#manipulação de strings com aspas e quebras de linha
NOME_PROPRIO = "Weslley Soares"

msg_aspas_simples = 'Projeto, "{NOME_PROPRIO}" em execução!'
msg_aspas_duplas = "Aluno, '{NOME_PROPRIO}' aprovado no teste !" 
relatorio_triple = """ \nTitulo: Lorem\n 
lorem ipsum dolor sit amet, consectetur adipiscing elit, lorem ipsum
dolor sit amet, consectetur adipiscing elit, lorem ipsum dolor sit amet,
consectetur adipiscing elit, lorem ipsum dolor sit amet, consectetur adipiscing elit,"""

print(msg_aspas_simples.format(NOME_PROPRIO=NOME_PROPRIO))
print(msg_aspas_duplas.format(NOME_PROPRIO=NOME_PROPRIO))
print(relatorio_triple)
print("\nFim do programa")