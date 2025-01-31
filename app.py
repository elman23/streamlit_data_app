import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv


from sidebar import Sidebar
from view_and_edit import ViewAndEdit
from input_data import InputData


def main():
    load_dotenv()

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:adminpass@localhost:27017/")
    DB_NAME = os.getenv("DB_NAME", "streamlit_db")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "user_inputs")

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    view_and_edit = ViewAndEdit(collection)
    input_data = InputData(collection)

    sidebar = Sidebar()
    page = sidebar.get_page()

    if page == "Input Data":
        input_data.get_data()
        if st.button("Submit"):
            input_data.save()
    elif page == "View & Edit Data":
        view_and_edit.get_data()


if __name__ == '__main__':
    main()