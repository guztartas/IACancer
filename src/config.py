
from pathlib import Path

name_model = 'model_best'
path_to_model = Path('') # /models 
classes = ['Ceratose actínica', 'Carcinoma basocelular', 'Ceratose benigna',
        'Dermatofibroma', 'Nevo melanocítico (pinta ou beleza)', 'Melanoma', 'Lesões vasculares']
port = 8008

def config(name_model, path_to_model, classes, port):
    name_model = name_model
    path_to_model = path_to_modelmodels 
    classes = classes
    port = port
    return name_model, path_to_model, classes, port