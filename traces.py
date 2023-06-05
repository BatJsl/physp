import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from trajectoire_v2_jj import système
from scipy.integrate import solve_ivp

g = 9.81  # Accélération due à la gravité
masse = 0.45  # Masse en kg
intervalle = 0.01  #taille de l'intervalle en s



"""

Vol sans frottements

"""

def compute_ball_coordinates(v0, angle, t):
    radian_angle = np.deg2rad(angle)
    x = v0 * np.cos(radian_angle) * t
    y = v0 * np.sin(radian_angle) * t - 0.5 * g * t**2
    return t, x, y


def search_t_flight(v0, angle):
    g = 9.81  # Accélération due à la gravité
    radian_angle = np.radians(angle)
    t_flight = (2 * v0 * np.sin(radian_angle)) / g
    d_max = (v0 ** 2 * np.sin(2 * radian_angle)) / g
    h_max = (v0**2 * np.sin(radian_angle)**2) / (2 * g)

    return t_flight, d_max, h_max


def trace_sans_frott():

    """
    sur streamlit
    """
    # st.title("Courbe de ballon de rugby")
    # v0 = st.number_input("Vitesse initiale (en m/s)", min_value=0.0, step=1.0, value=10.0)
    # angle = st.number_input("Angle initial (en degrés)", min_value=0.0, max_value=90.0, step=1.0, value=45.0)
    #
    # tflight, xmax, ymax = search_t_flight(v0, angle)
    #
    # print(type(float(tflight)))
    # tfinal = st.slider("Temps (en secondes)", min_value=0.0, max_value=float(tflight), step=0.01, value=float(tflight/2))

    """
    debugage
    """
    # v0 = 10
    # angle = 45

    X, Y = [], []
    t = 0
    step = 0.001

    while t < tfinal:
        t, x, y = compute_ball_coordinates(v0, angle, t)
        X.append(x)
        Y.append(y)
        t += step

    lim = max(xmax, ymax)

    fig, ax = plt.subplots()
    plt.plot(X, Y)
    plt.ylim(-lim*0.05, lim*1.1)
    plt.xlim(-lim*0.05, lim*1.1)
    plt.xlabel("Distance (m)")
    plt.ylabel("Hauteur (m)")
    plt.title("Trajectoire du ballon de rugby en fonction du temps")
    # plt.show()
    # st.pyplot(fig)
    return 0






"""

Avec frottements

"""

def compute_ball_coordinates_frott(v0, angle, amortissement):

    x = [0]
    y = [0]
    vx = [v0*np.cos(angle)]
    vy = [v0*np.sin(angle)]
    yi = 0
    t = 0
    while yi >= 0:

        vxi = vx[-1]
        vyi = vy[-1]
        xi = x[-1]
        yi = y[-1]
        acceleration_x = - amortissement * vxi**2 / masse
        acceleration_y = - g - amortissement * vyi**2 / masse
        nvx = vxi + acceleration_x * intervalle
        nvy = vyi + acceleration_y * intervalle
        nx = xi + nvx * intervalle
        ny = yi + nvy * intervalle

        x.append(nx)
        y.append(ny)
        vx.append(nvx)
        vy.append(nvy)

        t += intervalle
    return x, y, t

def trace_avec_frottements():

    """sur streamlit"""
    st.title("Courbe de ballon de rugby avec frottements")
    v0 = st.number_input("Vitesse initiale (en m/s)", min_value=0.0, step=1.0, value=40.0)
    angle = st.number_input("Angle initial (en degrés)", min_value=0.0, max_value=90.0, step=1.0, value=45.0)
    amortissement = st.slider("Coefficient d'amortissement", min_value=0.0, max_value=0.1, step=0.01, value=0.05)
    amortissement = amortissement/10
    tvol = st.slider("Temps (en secondes)", min_value=0.0, max_value=10., step=0.01, value=1.)


    """debug"""
    # v0 = 40
    # angle = 45
    # amortissement = 0.02
    # tfinal = 10

    x, y, tfinal = compute_ball_coordinates_frott(v0, np.radians(angle), amortissement)
    xm = max(x)
    ym = max(y)
    lim = max(ym, xm)

    x = x[:int(tvol/intervalle)]
    y = y[:int(tvol/intervalle)]

    fig, ax = plt.subplots()
    plt.plot(x, y)
    plt.ylim(-lim*0.05, lim*1.1)
    plt.xlim(-lim*0.05, lim*1.1)
    plt.xlabel("Distance (m)")
    plt.ylabel("Hauteur (m)")
    plt.title("Position d'un ballon rond avec frottements en fonction du temps")
    # plt.show()
    st.pyplot(fig)
    return 0




"""

fonction hilaire 

"""


def trajectoire_reelle():
    t0 = 0
    dt = 0.1
    tf = 10

    ### Paramètres initiaux sur le ballon

    m = 0.450  # Masse du ballon en kg
    a = 0.25  # longueur en m
    b = 0.19  # largeur en m
    Vb = 0.0048  # volume du ballon

    alpha = 60  # angle d'attaque du coup de pied
    gamma = 30  # angle de trajectoire de vol
    khi = 0  # angle d'azimuth de la vitesse

    w = 20  # norme de la vitesse de rotation en tour par seconde


    X0 = 10  # position initiale du ballon
    Y0 = 35
    Z0 = 0

    U = st.number_input("Vitesse initiale (en m/s)", min_value=0.0, step=1.0, value=32.0)  # composantes de la vitesse initiale
    V = 0.1
    W = 0.1

    P = 10  # composante du vecteur vitesse angulaire (en s-1)
    Q = 0
    R = 0

    PSI = np.radians(0.0)  # angles d'euler initiaux
    THET = np.radians(st.number_input("Angle initial", min_value=0.0, step=1.0, value=20.0))
    PHI = 0

    initial_variables = [X0, Y0, Z0, U, V, W, P, Q, R, PSI, PHI, THET]
    num_points = 100
    t_eval = np.linspace(t0, tf, num_points)

    solution = solve_ivp(système, (t0, tf), initial_variables, method='DOP853', t_eval=t_eval)

    t = solution.t

    X = solution.y[0]
    Y = solution.y[1]
    Z = solution.y[2]
    U = solution.y[3]
    V = solution.y[4]
    W = solution.y[5]
    P = solution.y[6]
    Q = solution.y[7]
    R = solution.y[8]
    PSI = solution.y[9]
    PHI = solution.y[10]
    THET = solution.y[11]

    k = 0
    for z in Z:
        if z <= 0:
            k += 1

    fig, ax = plt.subplots()
    ax = plt.axes(projection='3d')
    # plt.plot(X, -Z)
    # plt.plot(X, -W)
    # plt.ylim(bottom=0)
    ax.legend()

    ax.set_xlim(-10, 110)
    ax.set_ylim(-10, 80)
    ax.set_zlim(0, 30)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # ax.view_init(azim=90, elev=0)

    ax.plot3D(X[:k], Y[:k], -Z[:k], 'gray')

    """
    
    tracé du terrain
    
    """

    def perches():
        largeur = 5.6
        hauteur = 3
        taille = 11
        X0, Y0, Z0 = 0, 32.2, 0
        X1, Y1, Z1 = 0, 32.2 + largeur, 0

        Z01 = taille
        Z02 = hauteur

        ax.plot3D([X0, X0], [Y0, Y0], [Z0, Z01], 'blue')
        ax.plot3D([X1, X1], [Y1, Y1], [Z0, Z01], 'blue')
        ax.plot3D([X1, X1], [Y0, Y1], [Z02, Z02], 'blue')

        X0, X1 = 100, 100

        ax.plot3D([X0, X0], [Y0, Y0], [Z0, Z01], 'blue')
        ax.plot3D([X1, X1], [Y1, Y1], [Z0, Z01], 'blue')
        ax.plot3D([X1, X1], [Y0, Y1], [Z02, Z02], 'blue')

        return 0

    def terrain():
        X0, Y0 = 0, 0
        X1, Y1 = 0, 70
        X2, Y2 = 100, 70
        X3, Y3 = 100, 0

        plt.plot([X0, X1], [Y0, Y1], 'g')
        plt.plot([X1, X2], [Y1, Y2], 'g')
        plt.plot([X2, X3], [Y2, Y3], 'g')
        plt.plot([X3, X0], [Y3, Y0], 'g')

        # plt.show()
        return 0

    perches()
    terrain()

    # plt.show()
    st.pyplot(fig)
    return 0