import streamlit as st


class UserInput:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.is_member = False

    def get_name(self):
        self.name = st.text_input('Enter your name:')

    def get_age(self):
        self.age = st.number_input('Enter your age:', min_value=0, max_value=120, step=1)
    
    def get_is_member(self):
        self.is_member = st.checkbox('Are you a member?')

    def display(self):
        st.write(f"Name: {self.name}")
        st.write(f"Age: {self.age}")
        st.write(f"Membership: {'Yes' if self.name else 'No'}")


def main():
    user_input = UserInput()
    user_input.get_name()
    user_input.get_age()
    user_input.get_is_member()

    if st.button('Submit'):
        user_input.display()


if __name__ == '__main__':
    main()