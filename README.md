## 🚀 How to Run with Docker
This project is containerized with Docker for easy and consistent execution.

---
### ⚙ Prerequisites
- Docker Desktop must be installed and running.

---
### 🏗 Step 1: Build the Docker Image

You can build the Docker image in two ways: from your local files or directly from a GitHub repository.

---
#### Build from Local Files

Open your terminal (PowerShell, Command Prompt, etc.),  
navigate to the Challenge_1a project directory,  
and run:

bash
docker build --platform linux/amd64 -t trial7 .


---
### 🧪 Step 2: Run the Analysis

The command below runs the application.  
The -v flag maps your local folder to /app/data inside the container.

---
#### ▶ Run with Sample Collections

To run analysis on a sample collection like Collection_3, run:

bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output trial6 python main_enhanced.py
