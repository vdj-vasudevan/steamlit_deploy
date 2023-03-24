import streamlit as st
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Define Streamlit app
def main():
    st.title('My spaCy app')
    text = st.text_input('Enter some text:')
    doc = nlp(text)
    for token in doc:
        st.write(token.text, token.pos_, token.dep_)

if __name__ == '__main__':
    main()
