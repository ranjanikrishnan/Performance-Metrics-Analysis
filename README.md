# Performance Metrics Analysis - Adjust Task

## Project Description
- Exposess the sample dataset through a single generic HTTP API endpoint which is capable of filtering, grouping and sorting. Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system. 

- Client of this API is able to:

    - filter by time range (date_from / date_to is enough), channels, countries, operating systems
    - group by one or more columns: date, channel, country, operating system
    - sort by any column in ascending or descending order
    - see derived metric CPI (cost per install) which is calculated as cpi = spend / installs

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
- View the exposed API in the browser or Postman

### API Details

- Exposed API Endpoint : http://127.0.0.1:8000/marketing/metrics  

- Following are the different possible URLs for each of the cases mentioned in the task.

    - GET /marketing/metrics?fields=impressions,country,clicks,channel&sum=impressions,clicks&date_before=2017-06-01&ordering=-clicks

    - GET /marketing/metrics?fields=os,date,installs&sum=installs&date_after=2017-05-01&date_before=2017-05-31&ordering=date&os=ios

    - GET /marketing/metrics?fields=revenue,os&sum=revenue&date=2017-06-01&ordering=-revenue
 
    - GET /marketing/metrics?fields=country,channel,cpi&cpi_sum&country=CA

### TO DO

- Follwing are yet to be worked on
    - show sum of spend broken down by channel ordered by cpi in descending order 
    - Tests