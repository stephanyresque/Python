qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <=  qtd_colunas:
        print(f'{linha, coluna}')
        coluna = coluna + 1

    linha = linha + 1

print('Fim')

# Vimos, acima, um exemplo clássico de while dentro de while.