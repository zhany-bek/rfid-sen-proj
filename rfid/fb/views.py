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

# REGISTERING TAGS HERE!!!
def register_tag(request):
    tags = []
    available_tags = []
    
    try:
        tags_dict = database.child("Tags").get()
        for tag_d in tags_dict.each():
            tags.append(tag_d.key())
    except:
        error_message = "No available tags"
        return render(request, 'reg_tag.html', {'tags': available_tags, 'error_message': error_message})

    taken_tags = fb.models.Tag.objects.values_list('uid', flat=True)

    # Filtering out tags that are already taken
    available_tags = [tag for tag in tags if tag not in taken_tags]
    if not available_tags:
        error_message = "No available tags"
        return render(request, 'reg_tag.html', {'tags': available_tags, 'error_message': error_message})

    if request.method == 'POST':
        selected_tag = request.POST.get('tag_select', None)

        if selected_tag:
            try:
                # Try to create a Tag with the selected UID
                tag_instance = fb.models.Tag.objects.create(uid=selected_tag)
                return redirect('success-page')
            except IntegrityError:
                # Handle the case where the UID is already associated with another Tag
                error_message = "UID is already associated with another Tag."
                return render(request, 'reg_tag.html', {'tags': available_tags, 'error_message': error_message})

    return render(request, 'reg_tag.html', {'tags': available_tags})

def reg_success(request):
    return render(request, 'reg_success.html')

# TAG-PRODUCT ASSOCIATION HERE!!!
