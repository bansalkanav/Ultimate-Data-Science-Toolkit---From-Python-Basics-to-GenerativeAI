# Heroku Deployment

## Heroku is PaaS Architecture

Along with your application files you need to take care of below mentioned steps:  
1. You need all the below metioned files for deployment:  
  a. requirements.txt  
  b. Procfile  
  c. setup.sh (You need setup.sh only for Streamlit)  
2. Autodetect the app type  
3. git push & start running  

_________________________________________________


Create a Python VirtualEnv  
a. `pip list`  
b. `python -m venv venv/`  
c. `.\venv\Scripts\activate` => activate virtual environment in Windows  
d. `where python`  
e. `deactivate`  

Install these packages in virtualenv:  
`pip install matplotlib seaborn plotly sklearn nltk WordCloud`  

Create requirement.txt file using below mentioned command:  
`pip freeze > requirements.txt`

_________________________________________________
`This part is required for NLP Projects`

import nltk  
nltk.download('stopwords')  
nltk.download('wordnet')

_________________________________________________

Procfile (For Flask)  
`web: gunicorn app:project`  
web - Create a Web Dynos  
gunicorn app - I want to run a gunicorn app. If multiple people use my app, gunicorn make sure of multi threading and processing  
app - code is in app.py  

Procfile (For Streamlit)  
`web: sh setup.sh && streamlit run project.py`  

_________________________________________________

Folder Structure -  
requirements.txt  
Procfile  
setup.sh  
project_files  

_________________________________________________

Install Heroku CLI and Git  

`heroku login`  

Create a git repo and commit it locally
`git init .`  
`git add *`  
`git commit -m "commit_i"`  


`heroku git:remote -a app_name`  
`git push heroku master`

_________________________________________________

Run -  
`heroku run bash -a app_name`  

Stop -  
`heroku ps:scale web=0 -a app_name`  
