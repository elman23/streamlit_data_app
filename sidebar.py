import streamlit as st


class Sidebar:
    def __init__(self, title="Navigation"):
        self.title = title

    def get_page(self):
        st.sidebar.title(self.title)
        page = st.sidebar.radio("Go to", ["Input Data", "View & Edit Data"])
        return page


def main():
    sidebar = Sidebar()
    page = sidebar.get_page()
    print(page)


if __name__ == '__main__':
    main()