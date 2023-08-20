from django.shortcuts import render, redirect
from .forms import SignupForm, NewItemForm, LoginForm
from .models import PredictResult
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from cancerWeb import settings
import os
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Create your views here.
def modelPredict(direct):
    model = load_model(os.path.join(settings.BASE_DIR,'blog/static/data/model2.h5'))
    read = lambda imname: np.asarray(Image.open(imname).convert("RGB"))
    image = [read(direct)]
    image = np.array(image, dtype='uint8')
    image = image/255.
    #print(image)
    y_pred = model.predict(image)
    target = {0:'benign', 1:'malignant'}
    #print(np.argmax(y_pred, axis=1))
    return target[np.argmax(y_pred, axis=1)[0]]

def index(request):
    items = PredictResult.objects.all()
    return render(request, 'blog/index.html', {'items':items,})

def add_photo(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            result = modelPredict(settings.MEDIA_ROOT+item.image.url)
            item.result = result
            item.save()
            return redirect('blog:index')
    else:
        form = NewItemForm()
        return render(request, 'blog/add_photo.html', {'form': form})

def signup(request):
    if request.method == 'POST' and request.POST['password1'] == request.POST['password2']:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
        user.save()
        login(request, user)
        return redirect('blog:index')
    else: form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/signup.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:index')
    else:
        form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
    
def logout_page(request):
    logout(request)
    return redirect('blog:index')
