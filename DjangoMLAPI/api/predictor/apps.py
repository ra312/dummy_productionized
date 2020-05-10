"""
We load the trained model

"""
from django.apps import AppConfig
from django.conf import settings
import os
import pickle
class PredictorConfig(AppConfig):    # create path to models
	path = os.path.join(settings.MODELS, 'models.pickle')
 
    # load models into separate variables
    # these will be accessible via this class
	with open(path, 'rb') as pickled:
		data = pickle.load(pickled)    
	regressor = data['regressor']
	vectorizer = data['vectorizer']
