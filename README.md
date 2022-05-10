# Face Recognition Multilayer Perceptron

## Description

This is a personal project to understan how the multilayer perceptron works
aplied in computer vision field

## Data Sources

The project consumes photos to be trained this need to be placed in a folder 
with the name of the person you want to identify this folder need to be in
bd folder


<!-- ## Development

Parameters needed for configuration are in the file config.ini, this file 
contains:

* **AWS_S3_SETTINGS**: Parameters for the connection to S3 and views in Athena.

* **QUERY_4_ATHENA**: Queries for AWS Athena, used for updating the data.

* **PATHS**: Directory Paths for inputs and outputs.

 -->
### Requirements and Installation

directories and file structure:
```
Face_recognition_MLP/
    |---BD/
          |---PERSON1
              |---PHOTO1
              |---PHOTO2
              |---PHOTON
    
    |---MODEL/
          |---MLPClassifier.pkl
          |---Names.pkl
    |---.gitignore
    |---GUI.py
    |---funciones.py
    |---evaluacion-.py
    |---README.md
    |---requirements.txt
```

It requires Python 3.6 or higher, check your Python version first.

The [requirements.txt](requirements.txt) should list and install all the required Python 
libraries that the Master Table depend on, and they can be installed using:

`pip install -r requirements.txt`

  To run the app, you have to execute [GUI.py](GUI.py) file:

`python GUI.py`

This will run the the gui to train and explore the functions
