import numpy as np
from numpy import vectorize
from matplotlib import pyplot as plt
from math import cos,sin,pi
try:
    import tkinter
except:
    import Tkinter as tkinter


def bala_de_canhao():
    t_0 = 0 # tempo inicial, s
    t_final = 10 # tempo final, s
    N = 1000 # timestep
    teta = np.deg2rad(45) # angulo teta
    A = 0.1 # Ns/m
    m = 1.0 # massa, kg
    g = 10.0 # aceleração da gravidade, m/s^2

    # Vetor do tempo
    t = np.linspace(t_0, t_final, N+1)

    # Determina o tamanho de cada timestep dt (final - inicial)
    dt = t[1] - t[0]
    print("dt (delta t) =",dt,"s")

    # Vetores de aceleração, velocidade e posição relativa, respectivamente
    a = np.zeros((N+1,2))
    v = np.zeros((N+1,2))
    r = np.zeros((N+1,2))
    r2 = np.zeros((N+1,2))
    r3 = np.zeros((N+1,2))

    # Condições iniciais
    v[0] = (10*np.cos(teta), 10*np.sin(teta)) # vetor de velocidade, m/s
    r[0] = (0,0)  # posição inicial, m

    # Calculo da velocidade inicial (modulo do vetor v)
    vO = np.sqrt(pow((10*np.cos(teta)),2)+(pow((10*np.sin(teta)),2)))
    print("Velocidade inicial (v0) =", vO,"m/s")

    # Calculo do alcance sem o arraste
    R = ((pow(vO,2))/g * ((np.sin(2*teta))))
    Hmax = (np.sin(teta)**2)/2*g
    print("Altura maxima da bala(H) =",Hmax)
    print("Alcance da bala(R) sem a força de arraste =", R,"m")

    # Calculo da força de arraste seguindo Fr = -A*v
    def calc_arraste(r, v, t):
        return (-A * v)

    def indices(x):
        small_indices = y <= 0 
        x[small_indices] = 0
        x[invert(small_indices)] *= 10
        return x

    # Resolvendo as equações iterativamente com a força de arraste (dt=0.01)
    def calculo_com_arraste():
        stop = 0
        dt = 0.01
        for i in range(N):
            if stop != 1:
                a[i] = (calc_arraste(r[i], v[i], t[i]) - (0, m*g))/m
                v[i+1] = v[i] + a[i]*dt
                r[i+1] = r[i] + v[i]*dt
                # para o programa se a bala atingir o chão (y <= 0)
                if r[i,1] < 0:
                    stop = 1

    # Resolvendo as equações iterativamente com a força de arraste (dt=0.1)
    def calculo_com_arraste2():
        stop = 0
        dt = 0.1
        for i in range(N):
            if stop != 1:
                a[i] = (calc_arraste(r[i], v[i], t[i]) - (0, m*g))/m
                v[i+1] = v[i] + a[i]*dt
                r2[i+1] = r2[i] + v[i]*dt
                # para o programa se a bala atingir o chão (y <= 0)
                if r2[i,1] < 0:
                    stop = 1

    # Resolvendo as equações iterativamente sem a força de arraste (dt=0.1)
    def calculo_sem_arraste():
        stop = 0
        dt = 0.01
        for i in range(N):
            if stop != 1:
                a[i] = (0,-g)
                v[i+1] = v[i] + a[i]*dt
                r3[i+1] = r3[i] + v[i]*dt
                # para o programa se a bala atingir o chão (y <= 0)
                if r3[i,1] < 0:
                    stop = 1
    
    calculo_com_arraste()
    # Recuperando as coordenada x e y
    x = r[:,0]
    y = r[:,1]

    calculo_com_arraste2()
    # Recuperando as coordenada x e y
    x1 = r2[:,0]
    y1 = r2[:,1]

    calculo_sem_arraste()
    # Recuperando as coordenada x e y
    x2 = r3[:,0]
    y2 = r3[:,1]

    # Plotando o gráfico
    line1, = plt.plot(x,y, label="Com força de arraste e " r'$\Delta t$' "=0.01")
    plt.legend(handles=[line1], loc=1)
    line2, = plt.plot(x1,y1, label="Com força de arraste e " r'$\Delta t$' "=0.1")
    plt.legend(handles=[line2], loc=2)
    line3, = plt.plot(x2,y2, label="Sem força de arraste")
    plt.legend(handles=[line3], loc=3)

    plt.subplot(223)
    plt.plot(x,y, label="Com força de arraste e " r'$\Delta t$' "=0.01")
    plt.plot(x1,y1, label="Com força de arraste e " r'$\Delta t$' "=0.1")
    plt.plot(x2,y2, label="Sem força de arraste")
    plt.legend(bbox_to_anchor=(1.1, 1), loc=2, borderaxespad=0.)

    plt.xlabel('Distância horizontal (m)')
    plt.ylabel('Distância vertical (m)')
    plt.title('Trajetória de uma bala de canhão')
    plt.text(20, 2.5, r'$\theta=45,\ $ m=1.0kg, v0=10m/s')
    plt.grid()
    plt.axis([0, 15, 0, 15])

    #Exibir e salvar o gráfico
    plt.show() 
    plt.savefig('resultado.png')

bala_de_canhao();
