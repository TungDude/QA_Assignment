# PostgresSQL with Python
Assignment: Sertis QA Intern

## Prerequisites

1. Install Python (version 3.x) if you don't already have it. You can download it from [python.org](https://www.python.org/).
2. Make sure `pip` (Python's package manager) is installed. It usually comes with Python.
3. Install `virtualenv` if it's not already installed:

   ```bash
   pip install virtualenv

## Setting up the project

1. Clone the repository to your local machine, Using [this](https://github.com/TungDude/Automated-Testing.git) url.
   
   ```bash
   git clone <url>
   
3. Navigate to the project directory.
4. Create a virtual environment.
   
   ```bash
   python -m venv venv
   
5. Activate the virtual environment.
   
   - macOS/Linux
     
     ```bash
     source venv/bin/activate
     
   - Windows
     
     ```bash
     venv\Scripts\activate
     
7. Install the required dependencies
     ```bash
     pip install -r requirements.txt

8. Create a .env file at the root directory containing values for
    - POSTGRES_HOST
    - POSTGRES_DBNAME
    - POSTGRES_USER
    - POSTGRES_PASSWORD
    - POSTGRES_PORT

## Running the query

1. Ensure the virtual environment is activated.
2. Run the test using this command at the root of the project directory.
   
   ```bash
   python main.py

3. The results will be displayed in the terminal 
4. When you are finished with testing, deactivate the virtual environment.
   
   ```bash
   deactivate

### Feel free to reach out for any questions or issues.
