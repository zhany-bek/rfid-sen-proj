from django.shortcuts import render, redirect
from decouple import config
import pyrebase
import fb.models
from django.db import IntegrityError

fb_config = {
    'apiKey': config('API_KEY'),
    'authDomain': config('AUTH_DOMAIN'),
    'databaseURL': config('DATABASE_URL'),
    'projectId': config('PROJECT_ID'),
    'storageBucket': config('STORAGE_BUCKET'),
    'messagingSenderId': config('MESSAGING_SENDER_ID'),
    'appId': config('APP_ID'),
}

firebase = pyrebase.initialize_app(fb_config)
authe = firebase.auth()
database = firebase.database()


# Create your views here.
def index(request):
    tag = database.child('tags').child('0x328ba84d').get().val()
    return render(request, 'index.html', {
        'tag': tag
    })



# TAG-PRODUCT REGISTRATION HERE!!!
