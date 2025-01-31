import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:adminpass@localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "streamlit_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "user_inputs")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def show_sidebar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Input Data", "View & Edit Data"])
    return page

def show_input_data():
    st.title("Streamlit MongoDB Example")
    
    # User input fields
    name = st.text_input("Name", "")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    birth_date = st.date_input("Birth Date", datetime.today())
    is_subscribed = st.checkbox("Subscribe to newsletter")

    if st.button("Submit"):
        user_data = {
            "name": name,
            "age": age,
            "birth_date": birth_date.strftime("%Y-%m-%d"),
            "is_subscribed": is_subscribed,
            "created_at": datetime.utcnow()
        }
        result = collection.insert_one(user_data)
        st.success(f"Data saved successfully! ID: {result.inserted_id}")

def show_view_and_edit_data():
    st.title("View & Edit Records")
    
    documents = list(collection.find())
    if not documents:
        st.warning("No records found.")
    else:
        for doc in documents:
            with st.expander(f"{doc['name']} (ID: {doc['_id']})"):
                new_name = st.text_input("Edit Name", doc['name'], key=f"name_{doc['_id']}")
                new_age = st.number_input("Edit Age", min_value=0, max_value=120, step=1, value=doc['age'], key=f"age_{doc['_id']}")
                new_birth_date = st.date_input("Edit Birth Date", datetime.strptime(doc['birth_date'], "%Y-%m-%d"), key=f"birth_{doc['_id']}")
                new_is_subscribed = st.checkbox("Subscribed?", doc['is_subscribed'], key=f"sub_{doc['_id']}")
                
                if st.button("Update", key=f"update_{doc['_id']}"):
                    collection.update_one({"_id": doc["_id"]}, {"$set": {
                        "name": new_name,
                        "age": new_age,
                        "birth_date": new_birth_date.strftime("%Y-%m-%d"),
                        "is_subscribed": new_is_subscribed
                    }})
                    st.success("Record updated successfully!")

page = show_sidebar()

if page == "Input Data":
    show_input_data()

elif page == "View & Edit Data":
    show_view_and_edit_data()

