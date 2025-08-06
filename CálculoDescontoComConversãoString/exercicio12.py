PI = 3.14
desconto_txt = "31"
desconto_num = int(desconto_txt) / PI
preco_original = 599.99
preco_com_desconto = preco_original - (preco_original * desconto_num / 100)

print(f"O preço original era {preco_original:.2f} e com desconto de {desconto_num:.2f}% fica {preco_com_desconto:.2f}")
print(f"valor a ser pago: {preco_com_desconto:.2f}")
print(f"Fim do programa")
