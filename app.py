import streamlit as st
import page1 as p1
import page2 as p2

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "main"
    if st.session_state.page == "main":
        title_placeholder = st.empty()
        text_placeholder = st.empty()
        image_placeholder = st.empty()
        button_placeholder = st.empty()
        title_placeholder.title("Loan Default System")
        text_placeholder.text("This is an loan default system.\nIt predicts if the borowwer's loan will be default or not.")
        image_placeholder.image("loan default.jpeg")

        clicked = button_placeholder.button("START")
        if clicked:
            st.session_state.page = "page1"
            title_placeholder.empty()
            text_placeholder.empty()
            image_placeholder.empty()
            button_placeholder.empty()
            p1.page1()
    elif st.session_state.page == "page1":
        p1.page1()
    elif st.session_state.page == "page2":
        p2.page2()

if __name__ == "__main__":
    main()

