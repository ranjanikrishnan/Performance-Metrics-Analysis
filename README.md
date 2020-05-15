# Marketing Performance Merics Analysis - Adjust Task

## Project Description

## Prerequisites

- Please find all the necessary dependencies in requirements.txt

## Project Setup

- Clone the repo
    ```
    git clone https://github.com/ranjanikrishnan/Adjust-Home-Task
    ```
- Install the dependencies
    ```
    pip install -r requirements.txt
    ```
- Start the application
    ```
    python manage.py runserver
    ```

### API Details

- Exposed API Endpoint : http://127.0.0.1:8000/marketing/metrics  

- Following are the different possible URLs for each of the 4 cases mentioned in the task.

1. GET /marketing/metrics?fields=impressions,country,clicks,channel&sum=impressions,clicks&date_before=2017-06-01&ordering=-clicks

2. GET /marketing/metrics?fields=os,date,installs&sum=installs&date_after=2017-05-01&date_before=2017-05-31&ordering=date&os=ios

3. GET /marketing/metrics?fields=revenue,os&sum=revenue&date=2017-06-01&ordering=-revenue