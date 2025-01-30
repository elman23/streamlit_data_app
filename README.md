# Streamlit Data App

A Streamlit app that accepts user input for different types of fields and saves the data into a MongoDB database. 

The app includes text, number, date, and boolean inputs. 

You'll need to have `streamlit`, `pymongo`, and `python-dotenv` installed.

This script connects to a MongoDB database, collects input from the user, and saves it upon submission. Make sure your MongoDB instance is running, and update the `MONGO_URI`, `DB_NAME`, and `COLLECTION_NAME` variables as needed. 

## MongoDB

To run and set up MongoDB as a Docker container for development, follow these steps.

Run the following command in your terminal:
```bash
docker run -d --name mongodb-dev -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=adminpass mongo
```
This does the following:

- Runs MongoDB in detached mode (`-d`).
- Names the container `mongodb-dev`.
- Exposes MongoDB on port `27017`.
- Sets a default admin username and password.

Connect Streamlit to MongoDB

In your `.env` file (or set environment variables) you should have:
```
MONGO_URI=mongodb://admin:adminpass@localhost:27017/
DB_NAME=streamlit_db
COLLECTION_NAME=user_inputs
```
In your Streamlit app, the MongoDB connection shall be:
```
MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:adminpass@localhost:27017/")
```

### Persist Data

If you want MongoDB to retain data after the container stops, create a volume:
```bash
docker volume create mongodb_data
```
Run the MongoDB container with:
```bash
docker run -d --name mongodb-dev -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=adminpass -v mongodb_data:/data/db mongo
```

## Setup

To install Streamlit and set up the environment for your project, follow the indicated steps.

### Virtual Environment

Create a Virtual Environment. Open a terminal or command prompt and navigate to your project folder, then (on Unix) run:
```bash
python3 -m venv venv
```
Or (for Windows):
```powershell
python -m venv venv
```
Activate the virtual environment. On macOS/Linux:
```bash
source venv/bin/activate
```
On Windows:
```powershell
venv\Scripts\activate
```

### Dependencies

Install the required dependencies. Once the virtual environment is activated, install the necessary packages:
```bash
pip install streamlit pymongo python-dotenv
```

### Envorinment Variables

Set up environment variables. Create a `.env` file in your project directory and add:
```
MONGO_URI=mongodb://admin:adminpass@localhost:27017/
DB_NAME=streamlit_db
COLLECTION_NAME=user_inputs
```
This ensures that sensitive database credentials are not hardcoded in the script.

## Run 🚀

Run the Streamlit app. To start your Streamlit app, navigate to your script's directory and run:
```bash
streamlit run your_script.py
```