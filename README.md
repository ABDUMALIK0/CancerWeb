# CancerWeb
For MacOs
First of all, you have to train your own model. you can get data from https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification
and save your model with 'model.h5' name. Create new folder 'CancerWeb' and create python venv and Pull CancerWeb from github. Then you neet to create static/data folder in the blog folder (blog/static/data).
Move your model into blog/static/data. Run commands [source venv/bin/activate, pip install -r requirements.txt, python manage.py makemigrations, python manage.py migrate, python manage.py runserver].
Open your browser, search localhosts::8000. 
