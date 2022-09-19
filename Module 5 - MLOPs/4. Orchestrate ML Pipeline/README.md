# Managing Machine Learning Workflows using Prefect 2.0

## In this repository, you will find three versions of app.

### version_1 -> Basic Code without workflow management
### version_2 -> Code with Prefect Workflow - Defining the workflow and running them
### version_3 -> Dealing with the variables and monitoring the workflow with Prefect Cloud

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

### Why Prefect?
- Python based open source tool  
- Manage ML Pipelines  
- Schedule and Monitor the flow  
- Gives observability into failures  
- Native dask integration for scaling (Dask is used for parallel computing)