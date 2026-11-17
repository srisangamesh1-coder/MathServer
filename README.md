# Ex.03 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
abcd.html
<html>
    <head>
        <title>Simple Webpage</title>
    
    </head>
    <body>
        
        <h1 align="center">Churn Rate Calculator</h1>
        <h2 align="center">Srisangamesh(26010229)</h2>

        <form method="POST">
            {%csrf_token%}<br>

            
            <label>Lost customer:</label>
            <input type="text" name="CustLost" value="{{lost}}" ><br><br>
            <label>Initial customer:</label>
            <input type="text" name="InitCust" value="{{init}}"><br><br>
            <input type="submit" value="Calculate"><br><br>


            <label>Churn Rate:</label>
            <input type="text" name="ChurnRate" value="{{ChurnRate}}">





        </form>
    </body>
</html> 

views.py

from django.shortcuts import render

def calculate_rate(request):
    
    lost=float(request.POST.get("CustLost",'0'))
    init=float(request.POST.get("InitCust",'0'))
    ChurnRate = (lost/init)*100 if request.method == 'POST' else 0
    print(f"Initial Customer: {init}numbers \n Lost Customer: {lost}numbers \n Churn Rate: {ChurnRate}")
    return render(request, "myapp/abcd.html",{"init": init, "lost": lost, "ChurnRate": ChurnRate})

urls.py

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [path('', views.calculate_rate, name='calculate_rate'),]    

```


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-11-17 132036.png>)


## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-11-17 132024.png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
