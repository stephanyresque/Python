tipo = input('Digite algo: ')


print('O tipo primitivo é ', type(tipo))
print('É composto apenas por espaço?', tipo.isspace()) 
print('É um número?', tipo.isnumeric())
print('É alfabético?', tipo.isalpha())
print('É alfanumérico?', tipo.isalnum())
print('Está em maiúsculas?', tipo.isupper())
print('Está em minúsculas?', tipo.islower())
print('Está capitalizada?', tipo.istitle())



