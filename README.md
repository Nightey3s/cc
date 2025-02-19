## StressBook
StressBook is a streamlined database-focused project to analyze and optimize performance, speed, and memory usage in an event booking system. This project simulates a concert booking environment, emphasizing efficient data management and high-performance querying under load. The project inspiration comes from a friend that complains about the hardship of booking a popular concert or theater.  

## Prerequisite Software
1. Python
2. MongoDB
3. Install packages from requirements.txt

## Getting Started:
### Step 1 : Download The Virutal Package In Your Computer
```bash
pip install virtualenv
```
Or
```bash
py -m pip install virtualenv
```

### Step 2 : Change To The Project Folder Directory 
Note: Everyone Project Folder Directory Is Different
```bash
cd C:\Users\PC\Desktop\booking_system\INF2003-database-second-project
```

### Step 3 : Create Virtual Environment 
Note: env is the name for our environment, it can be venv too, just a name
```bash
py -m venv env 
```

### Step 4 : Activate Virutal Environment 
Operating System : Window
```bash
env\Scripts\activate
```
Operating System : MacOS
```bash
source env/bin/activate
```

### Step 5 : Install Required Packages From Requirements.txt

```bash
pip install -r requirements.txt
```
Or
```bash
py -m pip install -r requirements.txt
````

### Step 6 : To Run The Flask Project
Change To The Project Directory
```bash
cd stressbook
```
Run The Project
``` bash
py main.py
```
Or
```bash
python main.py
```
Or
```bash
python -m main run
```

Copy The Local Host Link And Paste It To The Browser For Example:
```bash
http://127.0.0.1:5000
```
### Step 7 : To Run Locust File
Change To The Locust File Directory 
```bash
cd locust_tests
```
Lets Say You Are Planning To Do Locust Test File Named "simulate_concurrent_users" In concurrent_user_load Folder
<br>
Type This Command In The Command Prompt
```bash
locust -f concurrent_user_load/simulate_concurrent_users.py
```
Copy The Local Host Link And Paste It To The Browser For Example:
```bash
http://localhost:8089
```

### Step 8: Changing And Understanding Locust Interface Parameters
1. Number Of Users (Peak Concurrency): Total Number Of Simulated Users That Would Be Using Your Program Through Locust Test Script
2. Ramp Up (Users Started/second): The Rate At Which New Users Are Spawned Until The Peak Concurrency Is Reached. For Example, Value Set To "5" And "Number Of Users" To "100", Locust Will Add 5 Users Per Second Until It Reaches 100 Users.
3. Host: http://127.0.0.1:5000 (For Our Project, Follow Your Port Number, Thank You) Unless We Are Planning To Deploy Our Website Then We Use Real URL
4. Advanced Options : https://docs.locust.io/en/stable/configuration.html , Can Type Through Command Prompt Or Create A Locust Environment File With The Necessary Environment Variables , In The Code Then We Access Those Environment Variables (Later Stage, After UI And Backend Logic Done, Then Will Take A Look)
### Self Note For Future Self When Creating Virtual Environment
1. After step 4, you pip install the packages that you needed for the project
2. Pip freeze > requirements.txt (Create the requirements.txt file, inside contains all the packages and the respective versions)
3. Proceed to step 5 for the people who have pulled the project and created the virutal environment.
