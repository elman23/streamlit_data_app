import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv


from sidebar import Sidebar
from view_and_edit import ViewAndEdit
from input_data import InputData


class MongoDbClient:
    def __init__(self):
        load_dotenv()

        MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:adminpass@localhost:27017/")
        DB_NAME = os.getenv("DB_NAME", "streamlit_db")
        COLLECTION_NAME = os.getenv("COLLECTION_NAME", "user_inputs")

        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def get_client(self):
        return self.client

    def get_db(self):
        return self.db

    def get_collection(self):
        return self.collection


def main():
    mongo_db_client = MongoDbClient()


if __name__ == '__main__':
    main()