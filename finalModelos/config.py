import os
class config(object):
	SECRET_KEY = 'llave_de_pepito'
	
class DevelopmentConfig(config):
	DEBUG = True