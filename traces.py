import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

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
