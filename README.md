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

🛠️ Setup Instructions
Follow these steps to set up the project locally.

1. Clone the Repository
bash
Copy code
git clone https://github.com/your_username/Event_TriggerX.git
cd Event_TriggerX
2. Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Set Up Database
Initialize the SQLite database (or other configured database):

bash
Copy code
python -c "from app.database import init_db; init_db()"
📦 Commands
Command	Description
uvicorn app.main:app --reload	Run the FastAPI application (development).
python -m pytest	Run the tests using pytest.
docker-compose up --build	Start the application using Docker.
python -c "from app.database import init_db; init_db()"	Initialize the database.
🚀 Run Application
1. Run with Uvicorn
bash
Copy code
uvicorn app.main:app --reload :
![Screenshot (1293)](https://github.com/user-attachments/assets/303052ab-2891-4569-8b99-9776a1cd4401)

## 📹 Live Project Walkthrough
[https://youtu.be/eNDIlcZbdws](https://github.com/user-attachments/assets/1e80e88b-b7bb-453e-840c-7b3e8eefc425
)

## next step : add \docs to the local hosted link = > 

#### When you add /docs to your FastAPI local server link, such as http://127.0.0.1:8000/docs, it opens the Swagger UI that FastAPI automatically generates for your application.
![Screenshot (1294)](https://github.com/user-attachments/assets/75729f8b-418a-4268-92a5-10eae698410a)


Swagger UI: http://127.0.0.1:8000/docs
Redoc UI: http://127.0.0.1:8000/redoc
2. Run with Docker
bash
Copy code
docker-compose up --build
🤝 Contributing
Contributions are welcome!
To contribute:

Fork the repository.
Create a new branch: git checkout -b feature/your-feature-name.
Commit your changes: git commit -m "Add some feature".
Push to the branch: git push origin feature/your-feature-name.
Submit a pull request.

## 📧 Contact
If you have any questions, feel free to reach out:
📧 Your Email: bvengadesh25504@gmail.com

⭐ Show Your Support
If you liked this project, please give it a ⭐ on GitHub!
Happy Coding! 🚀
