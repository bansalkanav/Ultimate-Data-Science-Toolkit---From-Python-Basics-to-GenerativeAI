# Managing Machine Learning Workflows using Prefect 2.0


### Why Prefect?
- Python based open source tool  
- Manage ML Pipelines  
- Schedule and Monitor the flow  
- Gives observability into failures  
- Native dask integration for scaling (Dask is used for parallel computing)

***

### Creating and activating a Virtual Environment
In order to install prefect, create a virtual environment:
> `$ python -m venv mlops`  

Enter the Virtual Environment using below mentioned command:
> `$ .\mlops\Scripts\activate`

### Installing Prefect 2.0
Now install Prefect:
> `$ pip install prefect`  

OR  if you have Prefect 1, upgrade to Prefect 2 using this command:  
> `$ pip install -U prefect`  

OR to install a specific version:  
> `$ pip install prefect==2.4`  

### Check Prefect Version
Check the prefect version:
> `$ prefect version`

***

### Running Prefect Dashboard

> `$ prefect server start`  

```
 ___ ___ ___ ___ ___ ___ _____
| _ \ _ \ __| __| __/ __|_   _|
|  _/   / _|| _|| _| (__  | |
|_| |_|_\___|_| |___\___| |_|

Configure Prefect to communicate with the server with:

    prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api

View the API reference documentation at http://127.0.0.1:4200/docs

Check out the dashboard at http://127.0.0.1:4200
```
***

**Note - In one of the earliest update of Prefect Orion, in Windows OS, if your path contains spaces, it will generate error (as mentioned below) when you try to run prefect orion. Sharing this so that you know what it is if you see it.**

```
___ ___ ___ ___ ___ ___ _____    ___  ___ ___ ___  _  _
| _ \ _ \ __| __| __/ __|_   _|  / _ \| _ \_ _/ _ \| \| |
|  _/   / _|| _|| _| (__  | |   | (_) |   /| | (_) | .` |
|_| |_|_\___|_| |___\___| |_|    \___/|_|_\___\___/|_|\_|
Configure Prefect to communicate with the server with:
    prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
View the API reference documentation at http://127.0.0.1:4200/docs
Check out the dashboard at http://127.0.0.1:4200/
Usage: uvicorn [OPTIONS] APP

Try 'uvicorn --help' for help.

Error: Got unexpected extra argument (prefect.orion.api.server:create_app)
Orion stopped!
```


### Make your code schedulable

Check the .ipynb file for details.