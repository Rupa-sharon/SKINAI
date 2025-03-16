import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a highly knowledgeable and interactive Skin Care Expert AI designed \
      to provide personalized skincare advice based on user concerns, skin types, and scientific \
      dermatology principles. Your goal is to help users understand their skin, suggest effective \
     skincare routines, recommend suitable products, and educate them on ingredients, common skin \
     issues, and professional treatments."),
    ("user", "{user_query}")  
])

def main():
    """
    Streamlit app for a Skincare chatbot.
    """
    st.title("SKINAI")
    st.write("Glow with Confidence – Your Personal AI Skincare Expert!")

    # User Input
    user_query = st.text_input("Enter your question:")

    if st.button("GENERATE"):
        if user_query:
            chain = prompt | llm
            response = chain.invoke({"user_query": user_query})
            
         
            answer = response.content if hasattr(response, 'content') else response

          
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question before asking.")

if __name__ == "__main__":
    main()
