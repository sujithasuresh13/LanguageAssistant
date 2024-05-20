import openai
import streamlit as st

st.title('Language Learning Assistant')

api_key = st.sidebar.text_input('Enter your OpenAI API key: ', type='password')

client = openai.OpenAI(
    api_key= api_key,
    base_url="https://api.aimlapi.com/",
)

def generate_response(english_query, target_language):
    chat_completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": f"You are an assistant that helps users learn {target_language}. Help translate the below content. "},
            {"role": "user", "content": english_query},
        ],
        temperature=0.7,
        max_tokens=512,
    )
    chat_completion.choices[0].message.content

with st.form('my_form'):

    english_query = st.text_input("Enter text to translate:")
    target_language = st.selectbox("Select target language:", ["Spanish", "French", "German", "Chinese"])


    submitted = st.form_submit_button('Submit')
   
    if submitted:
        try:
            generate_response(english_query, target_language)
        except Exception as e:
            print('Failed to generate : %s', repr(e))
