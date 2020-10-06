import funciones_final as funciones
import os #Interactuar con el entorno
from sklearn.neural_network import MLPClassifier
import joblib #Para guardar/cargar clases en archivos
from sklearn.model_selection import train_test_split
#Función que obtiene las características extraídas de cada rostro de las imágenes que conforman la base de datos
def carga_datos():
    dirs=os.listdir(path='./BD/')
    encodings_final=[]
    tags=[]
    #Se extraen las características de las imágenes
    print("Analizando directorios:")
    for (directorio,index) in zip(dirs, range(len(dirs))):
        print(str(index+1) + ') ' + directorio)
        funciones.load_dir(directorio, encodings_final, index, tags)
    #Guarda los datos en dos ficheros para evitar repetir este proceso en los experimentos
    joblib.dump(encodings_final, './Model/encodings.pkl')
    joblib.dump(tags, './Model/tags.pkl')
    #Función que realiza los experimentos
def experimentos(n_iter):
    #Carga los vectores de características guardados de cada rostro y su correspondiente etiqueta para identificar de quién se trata
    X=joblib.load('./Model/encodings.pkl')
    Y=joblib.load('./Model/tags.pkl')
    (aciertos_prc1_total, aciertos_prc2_total, aciertos_prc3_total)=(0,0,0)
    (prob_total1, prob_total2, prob_total3)=(0,0,0)
    #Se realizará el número de iteraciones que se elija al llamar a la función
    for iteration in range(n_iter):
        #print("Iteración número:", iteration+1)
        #Divide la base de datos en entrenamiento y validación
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        #Crea y entrena los diferentes MLPs
        clf1 = MLPClassifier(verbose=False, max_iter=1000, random_state=1,activation= 'tanh', hidden_layer_sizes = (200,200,200))
        clf2 = MLPClassifier(verbose=False, max_iter=1000, random_state=1,activation= 'tanh', hidden_layer_sizes = (150,150,150))
        clf3 = MLPClassifier(verbose=False, max_iter=1000, random_state=1,activation= 'tanh', hidden_layer_sizes = (100,100,100))

        model1=clf1.fit(X_train, Y_train)
        model2=clf2.fit(X_train, Y_train)
        model3=clf3.fit(X_train, Y_train)

        #Calcula el númmero de aciertos a partir de los datos de validación
        aciertos_prc1_total+=model1.score(X_test, Y_test)*100
        aciertos_prc2_total+=model2.score(X_test, Y_test)*100
        aciertos_prc3_total+=model3.score(X_test, Y_test)*100

        #Calcula las probabilidades obtenidas por los MLP y calcula su media
        probs1=model1.predict_proba(X_test)
        probs2=model2.predict_proba(X_test)
        probs3=model3.predict_proba(X_test)

        (probi1, probi2, probi3)=(0,0,0)

        for prob1, prob2, prob3, label in zip(probs1, probs2, probs3, Y_test):
            probi1+=prob1[label]
            probi2+=prob2[label]
            probi3+=prob3[label]
        N=len(probs1)
        prob_total1+=probi1/N
        prob_total2+=probi2/N
        prob_total3+=probi3/N
    #Prepara los datos finales diviendo entre el número de iteraciones paracalcular la media de cada parámetro
    aciertos_prc1_total/=n_iter
    aciertos_prc2_total/=n_iter
    aciertos_prc3_total/=n_iter
    aciertos = [aciertos_prc1_total, aciertos_prc2_total, aciertos_prc3_total]
    prob_total1/=n_iter
    prob_total2/=n_iter
    prob_total3/=n_iter
    probabilidades=[prob_total1*100, prob_total2*100, prob_total3*100]
    # print(aciertos[0:2])
    print(aciertos)
    print(probabilidades)

    return aciertos, probabilidades

carga_datos()
experimentos(2)