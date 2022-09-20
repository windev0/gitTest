from math import exp, fabs, sqrt

def saisie_bornes():
    try:
        x1 = int(input("Veuillez saisir la borne inférieure X1 = "))
        x2 = int(input("Veuillez saisir la borne supérieure X2 = "))
        assert x1 < x2
        if x1 < x2:
            return x1, x2
    except AssertionError:
        print('la borne inférieure doit etre strictement inférieure à la borne supérieure')
    except ValueError:
        print("Saisie invalide")
#---------------------------------------------------------------------------------------------
def saisie_X0():
    try:
        x0 = int(input("Veuillez saisir une valeur initiale: "))
        return x0
    except ValueError:
        print("Saisie invalide, choisir une autre valeur")
#---------------------------------------------------------------------------------------------
def saisie_epsilon_N():
    try:
        epsi = float(input("Quel est le critere d'arret e = "))
        N = int(input("Quel est le nombre maximal d'itération N = "))
        return epsi, N
    except ValueError:
        print("Saisie invalide")
#---------------------------------------------------------------------------------------------
def convergence(x1, x2, epsi, nb, xm = 1):
    if nb == 1: # 1 s'il s'agit de la convergence de la methode dichotomie
        return (fabs(x2-x1) / 2*fabs(xm)) < epsi
    else:   # autre entier pour la convergence des methodes de points fixes, NEWTON
        return (fabs(x2-x1) / fabs(xm)) < epsi
#---------------------------------------------------------------------------------------------
def nbre_solutions(x1, x2, pas):    # cette fonction retourne le nb de solution apres balayage
    a = x1 + pas                    # initialisation de a, et servira de borne sup temporaire
    cpt = 0                         # initialisation de cpt, pour compter les solutions
    while a <= x2:                  # tant que nous ne sommes pas arrivé à la borne supérieure
        x1 += pas                   # x1 est augmente d'un pas vers la gauche
        a += pas                    # a egalement est augmente d'un pas vers la gauche
        if f(x1)*f(a) < 0:          # si la fonction change de signe sur [x1, a], alors...
            cpt += 1                # il y a existence d'une solution, on incrémente cpt
    return cpt                      # on retourne le nombre de solutions trouvées
#---------------------------------------------------------------------------------------------
def f(x):
    # return pow(x,3) + pow(x,2) - 3 * x - 3
    # return pow(x,2) - 2
    # return sqrt(2*x + 3)
     return exp(-x) - x
    # return pow(x,2) - 2*x + 0.5
    # return pow(x,2) - 3*x + 2
#---------------------------------------------------------------------------------------------
def devf(x):
    return -exp(-x) - 1
#---------------------------------------------------------------------------------------------
def secante():
    print("\n**********METHODE DE LA SECANTE******************")
    try:
        e, N = saisie_epsilon_N()
        x0 = saisie_X0()
        x1 = saisie_X0()
        assert x0 < x1
        x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)-f(x0)))  # initialisation de x2
        i = 0
        while not(convergence(x1, x2, e, 2, x2)) and i < N - 1:
            # mise a jour des valeurs 
            x0 = x1
            x1 = x2
            x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)-f(x0)))
            i += 1
        # Saisie des résultats
        print('-----------------------------------------------')
        if convergence(x1, x2, e, 2, x2):
            print("convergence atteinte")
        if i == N-1 and (not convergence(x1, x2, e, 2, x2)):
            print("Convergence non atteinte en {} itérations".format(i+1))
        print("la solution est: Xn+1 = {}".format(x2))
        print('-----------------------------------------------')
    except TypeError:
        print("\nUne ou plusieurs donnée(s) entrée(s) est (sont) non valide(s)")
    except AssertionError:
        print("\nErreur: La premiere valeur initiale doit etre inférieure à la seconde!")
#---------------------------------------------------------------------------------------------

def newton():
    print("\n**********METHODE DE NEWTON******************")
    try:
        e, N = saisie_epsilon_N()
        x0 = saisie_X0()
        x1 = x0 - (f(x0) / devf(x0)) # initialisation de x1
        i = 0
        while not(convergence(x0, x1, e, 2, x1)) and i < N - 1:
            # mise a jour des valeurs 
            x0 = x1
            x1 = x0 - (f(x0) / devf(x0))
            i += 1
        # Saisie des résultats
        print('-----------------------------------------------')
        if convergence(x0, x1, e, 2, x1):
            print("convergence atteinte")
        if i == N-1 and (not convergence(x0, x1, e, 2, x1)):
            print("Convergence non atteinte en {} itérations".format(i+1))
        print("la solution est: Xn+1 = {}".format(x1))
        print('-----------------------------------------------')
    except TypeError:
        print("\nUne ou plusieurs donnée(s) entrée(s) est (sont) non valide(s)")
# -----------------------------------------------------------------------------------------------------------------------------------------

def point_fixe():
    print("\n**********METHODE DES POINTS FIXES******************")
    try:
        e, N = saisie_epsilon_N()
        x0 = saisie_X0()
        x1 = f(x0)  # initialisation de x1
        i = 0
        while not(convergence(x0, x1, e, 2, x1)) and i < N - 1:
            # mise a jour des valeurs 
            x0 = x1
            x1 = f(x0)
            i += 1
        # Saisie des résultats
        print('-----------------------------------------------')
        if convergence(x0, x1, e, 2, x1):
            print("convergence atteinte")
        if i == N-1 and (not convergence(x0, x1, e, 2, x1)):
            print("Convergence non atteinte en {} itérations".format(i+1))
        print("la solution est: Xn+1 = {}".format(x1))
        print('-----------------------------------------------')
    except TypeError:
        print("\nUne ou plusieurs donnée(s) entrée(s) est (sont) non valide(s)")
#---------------------------------------------------------------------------------------------
        
def dichotomie():
    print("\n**********METHODE DE DICHOTOMIE******************")
    try:
        x1, x2 = saisie_bornes()    # saisie des bornes de l'intervale
        print("on a {} solutions".format(nbre_solutions(x1, x2, 0.01))) # affichage du nombre de solutions trouvées
        if nbre_solutions(x1, x2, 0.01) > 0:
            if f(x1)*f(x2) < 0:
                print("La fonction change de signe sur l'intervalle [{},{}]".format(x1, x2))
                e, N = saisie_epsilon_N()   # saisie du critère d'arret et le nb max d'itération
                xm = (x1 + x2 )/2           # initialisation du milieu de l'intervalle
                i = 0
                while (not (convergence(x1, x2, e, 1, xm))) and i < N-1 and f(x1)*f(x2) < 0:
                    if f(x1)*f(xm) < 0:
                        x2 = xm             # changement de la borne supérieure
                    if f(xm)*f(x2) < 0:
                        x1 = xm             # changement de la borne inférieure
                    xm = (x1 + x2 )/2       # mise à jour du milieu de l'intervalle
                    i += 1                  # incrémentation du nb d'itérations
                print('-----------------------------------------------')
                if i == N-1 and (not convergence(x1, x2, e, 1, xm)):    # nb d'itération atteinte
                    print("Convergence non atteinte en {} itérations".format(i+1))
                if convergence(x1, x2, e, 1, xm):           # si la convergence est atteinte, alors...
                    print("Convergence atteinte")
                # Saisie des résultats
                print("\n X1 = {}\t\t\t X2 = {}\t\t\t Xm = {}\n f(X1) = {}\t\t f(X2) = {}\t\t f(Xm) = {}".format(x1, x2, xm, f(x1), f(x2), f(xm)))
                print('-------------------------------------------------------------------------------------------')
            #elif f(x1)*f(x2) > 0: 
                #print("on a {} solutions".format(nbre_solutions(x1, x2, 0.01))) # affichage du nombre de solutions trouvées
            else:
                print("la fonction ne change pas de signe sur cet intervalle")
    except TypeError:
        print("\nUne ou plusieurs donnée(s) entrée(s) est (sont) non valide(s)")
# -----------------------------------------------------------------------------------------------------------------------------------------

dichotomie()
# point_fixe()
# newton()
# secante()

    