from itertools import count


nomeCompleto = "Weslley Wallace Castro Soares"
opiniao = f'Serviço excelente aluno {nomeCompleto}, voltarei a comprar!' #

# Contagem de caracteres
num_caracteres = len(opiniao)
print(f"Número de caracteres: {num_caracteres}")

# Contagem de palavras
num_palavras = opiniao.count(" ") + 1  # +1 para contar a última palavra
print(f"Número de palavras: {num_palavras}")

print(f"fim do programa")

# Fim do programa