import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')


# # Load a pre-trained Hugging Face model

# chatbot = pipeline("text-generation", model="distilgpt2")

chatbot=pipeline("text2text-generation", model="gpt2")



# Define healthcare-specific response logic (or use a model to generate responses)
def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."

    elif "appointment" in user_input:
        return "Please consult to the nearby clinic and ask for the best doctor"

    elif "medication" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    else:
        # For other inputs, use the Hugging Face model to generate a response
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']


# Streamlit web app interface
def main():
   
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?", "")
    
    # Display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()



