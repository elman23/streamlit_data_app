import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv


class InputData:
    def __init__(self, collection, title="Streamlit MongoDB Example"):
        self.collection = collection
        self.title = title
        self.name = ""
        self.age = 0
        self.birth_date = None
        self.is_subscribed = False

    def get_data(self):
        st.title(self.title)
        
        self.name = st.text_input("Name", "")
        self.age = st.number_input("Age", min_value=0, max_value=120, step=1)
        self.birth_date = st.date_input("Birth Date", datetime.today())
        self.is_subscribed = st.checkbox("Subscribe to newsletter")

    def save(self):
            user_data = {
                "name": self.name,
                "age": self.age,
                "birth_date": self.birth_date.strftime("%Y-%m-%d"),
                "is_subscribed": self.is_subscribed,
                "created_at": datetime.utcnow()
            }
            result = self.collection.insert_one(user_data)
            st.success(f"Data saved successfully! ID: {result.inserted_id}")


def main():
    load_dotenv()

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:adminpass@localhost:27017/")
    DB_NAME = os.getenv("DB_NAME", "streamlit_db")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "user_inputs")

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    input_data = InputData(collection)
    input_data.get_data()
    if st.button("Submit"):
        input_data.save()


if __name__ == '__main__':
    main()