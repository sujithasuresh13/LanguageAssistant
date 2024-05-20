import streamlit as st
import openai

st.title("Language Learning Assistant")

aimlkey = st.text_input("Enter your OpenAI API key:", type="password")

if aimlkey:
    openai.api_key = aimlkey

    text_to_translate = st.text_area("Enter text to translate:")
    target_language = st.selectbox("Select target language:", ["Tamil", "Spanish", "French", "German", "Chinese"])

    if st.button("Translate"):
        if text_to_translate:
            prompt = f"Translate the following text to {target_language} and provide example sentences: {text_to_translate}"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are an assistant that helps users learn {target_language}."},
                    {"role": "user", "content": prompt},
                ],
            )
            translation = response.choices[0].message['content']
            st.write(translation)
        else:
            st.warning("Please enter text to translate.")
else:
    st.warning("Please enter your OpenAI API key.")
