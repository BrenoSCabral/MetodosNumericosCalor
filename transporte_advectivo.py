# Trabalho de Metodos Numericos p calcular o transporte advectivo
#importando bibliotecas que hão de ser utilizadas:
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation


# definindo variaveis
dt = 1 # passo de tempo (livre)
nt = 2000 # numero de passos de tempo (livre)

# grade precisa ser 25x25
j_max = 25 
i_max = 25

dx = 100 # resolucao da grade
dy = 100

# velocidade de 5 (separado em componentes da raiz de 5 p cada)
u_const = (25/2) ** (1 / 2)  # Modulo da velocidade do vento =  5 m/s
v_const = (25/2) ** (1 / 2)

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
print(est, beta)

# if ((u_const*dt)/dx == (v_const*dt)/dy): print ('foi') #testando se as constantes sao iguais tanto no x quanto no y

matrix = np.zeros((nt ,i_max, j_max))
matrix[:,inf_i:sup_i, inf_j:sup_j] = 25 # definindo a fonte cte

for t in range(nt-1): # botamos nt-1 pra nao dar porblema de indice
	if t == 0:
		for i in range(i_max-1):
			for j in range(j_max-1):
				if i==0 or j==0 or i==i_max or j==j_max: # definindo condicao de contorno = 0 
					matrix[t][i][j] = 0
				else: #trabalhando como cond inicial = 25
					# matrix[t][i][j] = 25
					# fazendo o chute inicial
					difx= (matrix[t, i+1,j] - 2*matrix[t,i,j] + matrix[t, i-1,j])/(dx**2)
					dify= (matrix[t, i,j+1] - 2*matrix[t,i,j] + matrix[t, i,j-1])/(dy**2)
					advx= (matrix[t, i+1,j] - matrix[t,i-1,j])/(dx*2)
					advy= (matrix[t, i,j+1] - matrix[t,i,j-1])/(dy*2)

					matrix[t+1,i,j] = (dt*(kx*(difx+dify)-(u_const*advx)-(v_const*advy)))+matrix[t,i,j]

	else:		
		for i in range(1, i_max-1):
			for j in range(1, j_max-1):
				if sup_j-1 >= j >= inf_j and sup_i-1 >= i >= inf_i:  # Simplifcado
					# excluindo a fonte de calor(ja q ela eh cte=25)
					continue
				else: #avancando no tempo
					difx= (matrix[t, i+1,j] - 2*matrix[t,i,j] + matrix[t, i-1,j])/(dx**2)
					dify= (matrix[t, i,j+1] - 2*matrix[t,i,j] + matrix[t, i,j-1])/(dy**2)
					advx= (matrix[t, i+1,j] - matrix[t,i-1,j])/(dx*2)
					advy= (matrix[t, i,j+1] - matrix[t,i,j-1])/(dy*2)
					matrix[t+1,i,j] = (2*dt*(kx*(difx+dify)-(u_const*advx)-(v_const*advy)))+matrix[t-1,i,j]


# Eixos
x = np.arange(0, i_max)
y = np.arange(0, j_max)
X, Y = np.meshgrid(x, y, indexing='ij')

# Propriedades do plot
vmin = math.floor(np.min(matrix))
vmax = math.ceil(np.max(matrix))
print(vmin, vmax)  # se estes valores tiverem uma diferencia enorme, vai dar problema no plot e nas operacoes seguintes.
plot_kwargs = {'vmin': vmin, 'vmax': vmax}
levels = np.arange(vmin, vmax, 1)

# Plotar o Contourf da matrix

fig, ax1 = plt.subplots()
plot = ax1.contourf(X, Y, matrix[0], levels, **plot_kwargs)
cb = fig.colorbar(plot)


# Animacao do Plot
def update_plot(frame):
    ax1.clear()
    count = ax1.contourf(X, Y, matrix[frame], levels, **plot_kwargs)
    return count,


ani = FuncAnimation(fig, update_plot, np.arange(nt), interval=5)  # se estiver muito rapido, tenta aumentar interval

# Mostra o plot
plt.show()
