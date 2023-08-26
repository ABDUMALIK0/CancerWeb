# CancerWeb
For MacOs
1. The first thing to do is to clone the repository:
2. Create a virtual environment to install dependencies in and activate it:
3. Then install the dependencies:
    (env) pip install -r requirements.txt
4. Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.
5. Once pip has finished downloading the dependencies: Run:
        *(env)$ python manage.py makemigrations
        *(env)$ python manage.py migrate
        *(env)$ python manage.py runserver
6. And navigate to http://127.0.0.1:8000/

You have to train your own model. You can get a data from https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification.
Train it and save your model with 'model.h5' name. 
Then you neet to create static/data folder in the blog folder (blog/static/data).
Move your model into blog/static/data.
Open your browser, search localhosts::8000. 
