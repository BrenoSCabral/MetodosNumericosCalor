# Trabalho de Metodos Numericos p calcular o transporte advectivo
#importando bibliotecas que hão de ser utilizadas:
import numpy as np

# definindo variaveis
dt = 0.5 # passo de tempo (livre)
nt = 2000 # numero de passos de tempo (livre)

# grade precisa ser 25x25
j_max = 25 
i_max = 25

dx = 100 # resolucao da grade
dy = 100

# velocidade de 5 (separado em componentes da raiz de 5 p cada)
u_const = 5**(1/2)
v_const = 5**(1/2)

kx = 1 # coeficiente de difusao (livre)



# fonte de emissao continua (posicionando a fonte no canto 
# inferior esquerdo do dominio) mas posicionando fora do contorno
inf_i = 1
sup_i = 6
inf_j = 1
sup_j = 6

# print((nt*dt/3600)) # numero de horas da simulacao


est=(u_const*dt)/dx #tem que ser menor que 1
beta=(kx*dt)/(dx^2) #tem que ser menor que 0.5

# if ((u_const*dt)/dx == (v_const*dt)/dy): print ('foi') #testando se as constantes sao iguais tanto no x quanto no y

matrix = np.zeros((nt ,i_max, j_max))
matrix[:,inf_i:sup_i, inf_j:sup_j] = 25 # definindo a fonte cte

for t in range(nt):
	if t == 0:
		for i in range(i_max):
			for j in range(j_max):
				if i==0 or j==0 or i==i_max or j==j_max: # definindo condicao de contorno = 0 
					matrix[t][i][j] = 0
				else: #trabalhando como cond inicial = 25
					matrix[t][i][j] = 25
	else:
		for i in range(1, i_max-1):
			for j in range(1, j_max-1):
				if j<=sup_j and j>=inf_j and i<=sup_i and i>=inf_i:
					# excluindo a fonte de calor(ja q ela eh cte=25)
					continue


print(matrix)
