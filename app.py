import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv


from sidebar import Sidebar
from view_and_edit import ViewAndEdit
from input_data import InputData
from mongo_db_client import MongoDbClient

def main():
    mongo_db_client = MongoDbClient()
    collection = mongo_db_client.get_collection()

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