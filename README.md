# 🚀 Event TriggerX

#### A modern FastAPI-based event trigger system for scheduling, logging, and managing event workflows.
### 📚Table of Contents
      Overview
      Project Structure
      Features
      Mindmap
      Setup Instructions
      Commands
      Run Application
      Contributing
      Contact

## 📝 Overview
#### Event TriggerX is a lightweight, scalable backend service built with FastAPI that allows you to:

    Manage triggers for events.
    Schedule and log triggered events.
    Archive or delete expired event logs.
    This project is ideal for applications that require event scheduling, task management, and database management for logs.


![Screenshot (1290)](https://github.com/user-attachments/assets/ad87f6a9-bc3a-47f2-9e60-d8ad33298233)

## ⭐ Features
       Trigger Management: Create, update, retrieve, and delete triggers.
       Event Logging: Automatically logs triggered events.
       Active and Archived Logs: Query active logs and archived logs.
       Auto-Deletion: Deletes expired logs after a set time.
       API Documentation: Integrated Swagger UI with FastAPI.


![Screenshot (1292)](https://github.com/user-attachments/assets/026058fe-8733-44a1-ab82-f7af60975073)

## 🚀 Setup Instructions
![Screenshot (1296)](https://github.com/user-attachments/assets/fac07f0b-a1a5-4f02-b418-b3289948967a)


## Step 1: Clone the Repository
            Download the project source code to your local system.
            
            git clone https://github.com/vengadesh-max/Event_triggerX-App.git
            cd Event_TriggerX
Explanation: The git clone command copies the project from GitHub, and cd navigates to the project directory.
## Step 2: Create a Virtual Environment
            Set up an isolated Python environment for the project dependencies.
            
## For Linux/Mac
            python -m venv venv
            source venv/bin/activate

## For Windows
            python -m venv venv
            venv\Scripts\activate
Explanation:
python -m venv venv creates a virtual environment named venv.
source (Linux/Mac) or venv\Scripts\activate (Windows) activates the environment.

## Step 3: Install Dependencies
            Install the required libraries and packages.
            pip install -r requirements.txt
Explanation: This command reads the requirements.txt file and installs all necessary dependencies for the project.

## Step 4: Set Up the Database
            Initialize the database to ensure proper setup.
            python -c "from app.database import init_db; init_db()"
Explanation: This runs a script to set up the database tables and structure (using SQLite or any configured database).

## Step 5: Run the Application
            Start the FastAPI server in development mode.
            uvicorn app.main:app --reload
Explanation:
uvicorn is the server that runs the FastAPI app.
--reload automatically restarts the server upon file changes.

## Access the App:

            Swagger UI: http://127.0.0.1:8000/docs
            Redoc UI: http://127.0.0.1:8000/redoc
## Step 6: Run with Docker :
            If you prefer running the project in a Docker container:
            docker-compose up --build
Explanation: This builds the Docker image and runs the project in a containerized environment.

### Run command  : uvicorn app.main:app --reload :

![Screenshot (1293)](https://github.com/user-attachments/assets/303052ab-2891-4569-8b99-9776a1cd4401)

## 📹 Live Project Walkthrough
[https://youtu.be/eNDIlcZbdws](https://github.com/user-attachments/assets/1e80e88b-b7bb-453e-840c-7b3e8eefc425
)

## Next step : add \docs to the local hosted link = > 

#### When you add /docs to your FastAPI local server link, such as http://127.0.0.1:8000/docs, it opens the Swagger UI that FastAPI automatically generates for your application.
![Screenshot (1294)](https://github.com/user-attachments/assets/75729f8b-418a-4268-92a5-10eae698410a)



## 📌 API Endpoints
### 1. Trigger Management

        Create a Trigger
            Method: POST
            Endpoint: /api/triggers/
            Description: Add a new trigger.
            Payload Example:
            json
            {
              "name": "Daily Backup",
              "trigger_type": "schedule",
              "schedule_time": "2024-06-15T10:00:00",
              "interval_seconds": 86400,
              "api_payload": {"key": "value"}
            }
            
Retrieve All Triggers

            Method: GET
            Endpoint: /api/triggers/
            Description: Fetch all triggers.
            
Retrieve Trigger by ID

            Method: GET
            Endpoint: /api/triggers/{trigger_id}
            Description: Get a specific trigger by ID.
            
Update a Trigger

            Method: PUT
            Endpoint: /api/triggers/{trigger_id}
            Description: Update an existing trigger.
            
##### Payload Example:
            json
            {
              "name": "Updated Trigger Name",
              "interval_seconds": 3600
            }
            
Delete a Trigger

            Method: DELETE
            Endpoint: /api/triggers/{trigger_id}
            Description: Delete a trigger by ID.
            
### 2. Event Logs Management
 Retrieve Active Event Logs

              Method: GET
              Endpoint: /api/event_logs/
              Description: Fetch logs that are currently active.
              
  Retrieve Archived Event Logs

              Method: GET
              Endpoint: /api/event_logs/archived
              Description: Fetch logs that are archived.
              
  Delete Expired Event Logs

             Method: DELETE
             Endpoint: /api/event_logs/expired
             Description: Remove logs that have expired.
        
### 3. Health Check
         Check API Status
           Method: GET
           Endpoint: /
           Description: A simple endpoint to confirm that the API is running.

## 📧 Contact
If you have any questions, feel free to reach out:
📧 Your Email: bvengadesh25504@gmail.com

⭐ Show Your Support
If you liked this project, please give it a ⭐ on GitHub!
Happy Coding! 🚀
