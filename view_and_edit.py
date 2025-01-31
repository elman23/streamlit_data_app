import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv


class ViewAndEdit:
    def __init__(self, collection, title="View & Edit Records"):
        self.collection = collection
        self.title = title
        self.docs_to_update = []
        

    def get_data(self):
        st.title(self.title)

        documents = list(self.collection.find())
        if not documents:
            st.warning("No records found.")
        else:
            for doc in documents:
                with st.expander(f"ID: {doc['_id']})"):
                    new_doc = {}
                    new_doc['_id'] = doc['_id']
                    new_doc['name'] = st.text_input("Edit Name", doc['name'], key=f"name_{doc['_id']}")
                    new_doc['age'] = st.number_input("Edit Age", min_value=0, max_value=120, step=1, value=doc['age'], key=f"age_{doc['_id']}")
                    new_doc['birth_date'] = st.date_input("Edit Birth Date", datetime.strptime(doc['birth_date'], "%Y-%m-%d"), key=f"birth_{doc['_id']}")
                    new_doc['is_subscribed'] = st.checkbox("Subscribed?", doc['is_subscribed'], key=f"sub_{doc['_id']}")
                    if st.button("Update", key=f"update_{doc['_id']}"):
                        self.save(new_doc)

    def save(self, doc):
        self.collection.update_one({"_id": doc["_id"]}, {"$set": {
            "name": doc['name'],
            "age": doc['age'],
            "birth_date": doc['birth_date'].strftime("%Y-%m-%d"),
            "is_subscribed": doc['is_subscribed']
        }})
        st.success("Record updated successfully!")

def main():
    load_dotenv()

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:adminpass@localhost:27017/")
    DB_NAME = os.getenv("DB_NAME", "streamlit_db")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "user_inputs")

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    view_and_edit = ViewAndEdit(collection)
    view_and_edit.get_data()


if __name__ == '__main__':
    main()