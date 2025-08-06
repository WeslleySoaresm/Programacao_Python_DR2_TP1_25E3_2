#Simulação de Cliente com Tipos de Dados Primitivos
# Este programa coleta informações de um cliente e exibe os dados formatados.
NOME_CLIENTE = "João da Silva"
IDADE_CLIENTE = 30
CODIGO_CLIENTE = 12345
SCORE_CREDITO = 772.4
STATUS_CLIENTE = True

print("Cadastro de Cliente")
print("-------------------")
print(f"Nome: {NOME_CLIENTE}, {type(NOME_CLIENTE)}")
print(f"Idade: {IDADE_CLIENTE}, {type(IDADE_CLIENTE)}")
print(f"Código: {CODIGO_CLIENTE}, {type(CODIGO_CLIENTE)}")
print(f"Score de Crédito: {SCORE_CREDITO}, {type(SCORE_CREDITO)}")
print(f"Status: {STATUS_CLIENTE}, {type(STATUS_CLIENTE)}")
print("-------------------")