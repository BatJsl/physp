import streamlit as st


def disp_app():

    # Titre de la page
    st.title("Comment obtenir le coup de pied parfait avec un ballon de rugby?")


    # Pour mettre une séléction avec plusieurs choix

    # add_selectbox = st.selectbox(
    #     'How would you like to be contacted?',
    #     ('Email', 'Home phone', 'Mobile phone')
    # )

    # Divise une partie de la page en 2
    left_column, right_column = st.columns(2)
    # Afficher une image
    image_path = '/Users/bat/Desktop/physp/'
    st.image(image_path + 'image_rugby.jpg')

    with right_column:
        st.image(image_path + 'coup_de_pied.jpg')
    with left_column:
        st.image(image_path + 'image_rugby.jpg')

    st.header('Introduction')
    # st.subheader('My sub')

    st.write("Voici un projet réalisé par 3 étudiants en deuxième année à l'école des Ponts. "
            "Le projet a été réalisé dans le cadre du cours : Mécanique et physique de sport. "
            "Le but est de voir l'influence de plusieurs paramètres sur la trajectoire d'un "
            "ballon de rugby. Pour cela, vous pouvez observer les trajectoirs de balles avec "
            "plusieurs conditions différentes: avec ou sans frottements, et pour un ballon"
            "rond ou ovale. La mise en équation est beaucoup plus délicate lorsque l'on prend"
            " en compte la forme ovale du ballon de rugby. Sur les différentes pages que vous"
            " voyez sur le côté, vous pouvez accéder aux simulations sous les hyputhèses "
            " différrentes. ", wrap=True)


    return 0

def disp_sans_frott():
    st.title("Courbe de ballon de rugby")
    st.write("Ici on peut observer la courbe réalisée par un ballon si on ne prend pas les fortemments en compte. La seule force éxercée sur le ballon est celle de l'attraction terrestre. C'est ce qu'on appelle un vol en chute libre. ", wrap=True)
    st.write("L'équation différentielle qui régit le mouvement de la balle est donc:", wrap=True)
    st.latex(r''' \ddot{y} = - g''')

    st.write("En intégrant cette équation on obtient l'équation de mouvement suivante:")
    st.latex(r''' y(x) = -\frac{1}{2} g x^2 + v_0 x ''')

    st.write("La courbe que l'on affiche ici est l'équation de mouvent. On a donc y (en ordonnée) en fonction de x (en abscisse). On peut faire varier la vitesse initiale, l'angle initial, et le temps auquel on se place.", wrap=True)
    return 0