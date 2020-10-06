import sys
import os 
import numpy as np
import face_recognition  # Librería de reconocimiento facial
import cv2  # Librería de visión artificial
import joblib  # Serializador de objetos
from sklearn.neural_network import MLPClassifier  # Clasificador MLP

# TODO crea el modelo MLP
def model_creator():  
    # ??Carpeta de donde se tom la base de datos
	dirs = os.listdir(path='./BD/')
	encodings_final = []  # Inicializando parámetros
	tags = []
	known_names = []
	print("Analizando directorios:")
	for(directorio, index) in zip(dirs, range(len(dirs))):
		# ? Mostrar las personas en la base de datos
		print(str(index+1) + ') ' + directorio)
		load_dir(directorio, encodings_final, index, tags)
		# ? Si hay al menos un rostro correcto en cada directorio
		known_names.append(directorio)
	# ?Si se han obtenido alg4unas etiquetas (y por tanto encodings)
	if tags:
		print(tags)
		# Crea y entrena el clasificador
		clf = MLPClassifier(verbose=False, max_iter = 1700, activation = 'tanh', hidden_layer_sizes = (150,150,150))
		model = clf.fit(encodings_final, tags)
		# Guarda el modelo de MLP entrenado y la lista de nombres
		joblib.dump(model, './Model/MLPClassifier.pkl')
		joblib.dump(known_names, './Model/Names.pkl')
		print("Clasificador MLP creado.")
	else:
		print("No se obtuvieron rostros")

# TODO Función que toma las imágenes de un directorio y obtiene la codificación susrostros
def load_dir(directorio, encodings_final, index, tags):
	path = './BD/' + directorio +'/'
	# Lista con los nombres de las imágenes de la carpeta de la persona
	file_list = os.listdir(path)
	for imagen in file_list:
		# Forma la ruta de la imagen
		complete_path = path + imagen
		# Carga la imagen y extrae sus caracteristicas
		imagen = face_recognition.load_image_file(complete_path)
		encodings = face_recognition.face_encodings(imagen)
		# Si se ha obtenido, se añade a la lista final de encodings y de etiquetas
		if encodings:
			encodings_final.append(encodings[0])
			tags.append(index)

# TODO Función que muestra los nombres disponibles
def print_names():
	try:		
		# Carga el modelo y los nombres disponibles
		model = joblib.load('./Model/MLPClassifier.pkl')
		known_names = joblib.load('./Model/Names.pkl')
		# Si ambos existen se imprime la lista de nombres
		if known_names and model:
			print("Existen persons regstradas:")
			nombres = np.array(known_names)			
		else:
			print("No existen reostros en la base de datos.")
			nombres = np.empty(1)
		return(nombres)		
		
	except Exception:
		sys.exit("No se pudo cargar el clasificador.")
		return(nombres)
	
# TODO Función que analiza los rostros de una imagen
def image(image_input):
	image = face_recognition.load_image_file(image_input) # Toma la ubicación y encoding de cada rostro de la imagen
	(detected_names, face_locations)=detect(image)
	# Inserta la ventana de identificación en la imagen
	insert_name(detected_names, face_locations, image)
	# Pasa del formato de color de face_recognition (RGB) al de OpenCV
	image = image[:, :, ::-1]
	# Guarda la imagen procesada
	splited_name = os.path.splitext(image_input)
	rchivoo = image_input[image_input.rfind('/'):image_input.rfind('.')]
	name_image = "./Output/" + rchivoo + "_out.jpg"
	cv2.imwrite(name_image, image)
	print(name_image + " creada.")
	detectado=cv2.imread(name_image)
	detectado=cv2.resize(detectado, None, fx = 0.5, fy = 0.5)
	cv2.imshow("reconocimiento", detectado)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# TODO Función que detecta las caras de una imagen y devuelve sus nombres y localizaciones
def detect(rgb_frame):
	try:
		# Carga el modelo
		model = joblib.load('./Model/MLPClassifier.pkl')
		known_names = joblib.load('./Model/Names.pkl')
	except Exception:
		sys.exit("No se pudo cargar el clasificador.")
	detected_names = []
	# Establece el umbral: mínimo parecido posible
	prox_min = 0.94
	# Encuentra todos los rostros del frame y obtiene sus encodings
	face_locations = face_recognition.face_locations(rgb_frame)
	face_encodings = face_recognition.face_encodings(rgb_frame)
	n_face = 0
	for face_encoding in face_encodings:
		[proximities] = model.predict_proba(face_encoding.reshape(1,-1))
		prox_max = max(proximities)
		if prox_max >= prox_min:
			tag=np.argmax(proximities)
			proximity = prox_max*100
			name = known_names[tag] + '(' + str(round(proximity,2)) + '%)'
			detected_names.append(name)
		else:
			name = "Desconocido "
			detected_names.append(name)
		n_face+=1
	return detected_names, face_locations

# Función que añade a una imagen el marco con la identificación de cada rostro detectado
def insert_name(names, face_locations, frame):
	for (top, right, bottom, left), name in zip(face_locations, names):
	# Añade el marco y el texto a la imagen
		cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
		cv2.putText(frame, name, (left, top-6), cv2.FONT_HERSHEY_DUPLEX, .8,(255,255,255), 1)

# Función que analiza los rostros de un vídeo
def detfvid(video_input):
	cap = cv2.VideoCapture(0)
	while(True):
		ret, frame = cap.read()
		# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rgb_frame = frame[:, :, ::-1]
		(detected_names, face_locations)=detect(rgb_frame)
		insert_name(detected_names, face_locations, frame)
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
