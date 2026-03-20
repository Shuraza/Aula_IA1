## [EXERCÍCIOS] 


# # 1) Após importar o módulo math

# # x = cos(pi/2) + sin(pi/2)
# # x = √3
# # x = log2 10


# import math as m

# cos = m.cos
# pi = m.pi
# sin = m.sin

# x = cos(pi/2) + sin (pi/2)
# y = m.sqrt(3)
# z = m.log2(10) 


# print( x, y, z)

# ---------------------------------------------------------------------------

# #  2) Importe o módulo `calendar` e descubra:

# # 2018 é um ano bissexto (leap year)?
# # Dia 22 de Maio de 1992 foi que dia da semana?
# # O mês de Julho de 2000 começou em que dia da semana?

# import calendar 

# x = calendar.isleap(2018)
# y = calendar.weekday(1992, 5, 22)
# z = calendar.monthrange(2000, 7)

# print(x, y, z)

# ---------------------------------------------------------------------------


# 1) Defina as variáveis `x = 1`, `y = 2.3` e `z = x+y`. 
# Qual o tipo de `x`, `y` e `z`?

# x = 1.78
# y = 53
# z = y / x ** 2

# print(z, type(z))

# 2) Defina as variáveis `x = 1`, `y = 4` e `z = x/y`. Qual o valor de `z`?

# x = 1
# y = 4
# z = x/y

# print(z, type(z))

# 3) Defina as variáveis `x = 1.0`, `y = 4` e `z = x/y`. Qual o valor de `z`?


# x = 1
# y = 4
# z = x/y

# print(z, type(z))



# 4) Calcule seu [Índice de Massa Corporal (IMC)](https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal).

# x = 1.78
# y = 53
# z = y / x ** 2

# print(z, type(z))

# 16.72768589824517 <class 'float'>



# ## [EXERCÍCIOS] Operadores e Comparações

# 1) Defina a variável `x = 7`:
# * `x * 2` é maior que `10`?
# * `x / 3` é menor que `5`?
# * `x` ao quadrado é igual a `49`?

# x = 7

# print(x * 2 > 10)  
# print(x / 3 < 5)    
# print(x ** 2 == 49) 


# 2) Defina a variável `y = 3`:
# * `y` é menor que `10` e `x` é maior que `10`?
# * `y` é maior ou igual a `3` ou `x` é igual a `8`?
# * `y` não é igual a `4`?

# y = 3
# x = 7

# print(y < 10 and x > 10)  
# print(y >= 3 or x == 8)    
# print(y != 4)              


# -----------------------------------------------------------------------------------------

# 1) Adicione, de forma programática, o pib da Turquia na lista `pib`. Pegue este valor [aqui](https://pt.wikipedia.org/wiki/Economia_de_Angola)).

# pib = [
#     ["china", 23120],
#     ["usa", 19360],
#     ["india", 9447],
#     ["japan", 5405],
#     ["germany", 4150],
#     ["russia", 4000],
#     ["indonesia", 3243],
#     ["brazil", 3219]
# ]

# pib.append(["turkey", 1565])

# print(pib)


