Heroku Architectures (PaaS)

a. requirements.txt
b. Procfile and setup.sh
c. Autodetect the app type
d. git push & start running

_________________________________________________


Python VirtualEnv
a. pip list
b. python -m venv venv/
c. .\venv\Scripts\activate => activate in Windows
d. where python
e. deactivate

Install these packages in virtualenv
pip install matplotlib seaborn plotly sklearn nltk WordCloud
pip freeze > requirements.txt

_________________________________________________


import nltk
nltk.download('stopwords')
nltk.download('wordnet')

_________________________________________________

Procfile (For Flask)
web: gunicorn app:project
web - Create a Web Dynos
gunicorn app - I want to run a gunicorn app. If multiple people use my app, gunicorn make sure of multi threading and processing
app - code is in app.py

Procfile (For Streamlit)
web: sh setup.sh && streamlit run project.py

_________________________________________________

Folder Structure - 
requirements.txt
Procfile
setup.sh
project_files

_________________________________________________

Install Heroku CLI and Git

heroku login

Create a git repo and commit it locally
git init .
git add *
git commit -m "commit_i"


heroku git:remote -a app_name
git push heroku master

_________________________________________________

Run -
heroku run bash -a app_name

Stop -
heroku ps:scale web=0 -a app_name
