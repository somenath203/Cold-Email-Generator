import streamlit as st 
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv


load_dotenv()


groq_api_key = os.getenv('GROQ_API_KEY')


llm_model = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-70b-versatile"
)


def extract_content_from_url(url):

    loader = WebBaseLoader(url)

    page_data_of_the_url = loader.load().pop().page_content

    return page_data_of_the_url



def generate_cold_email(job_post_data, user_profile_description):

    email_prompt_template = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### USER PROFILE:
        {user_profile_description}
        
        ### INSTRUCTION:
        You are an expert cold email generator. Based on the job description provided and the details of the user, generate a concise, personalized cold email aimed at securing an interview for the user. The email should:
        1. Briefly introduce the user.
        2. Highlight the user’s most relevant skills and experience.
        3. Mention specific projects or achievements that align with the job description.
        4. End with a strong closing statement that encourages further discussion.
        
        ### EMAIL (NO PREAMBLE):
        """
    )

    chain = email_prompt_template | llm_model

    response = chain.invoke({"job_description": job_post_data, "user_profile_description": user_profile_description})

    return response.content 



st.title('📧 Cold E-Mail Generator')


job_post_url_input = st.text_input('Enter the URL of the Job Post')

user_profile_description = st.text_area('Please provide a brief introduction about yourself, highlighting your key skills. Additionally, list 2 to 3 projects you\'ve worked on, giving a brief overview of each.', height=300)



if st.button('Generate Cold Email'):

    if job_post_url_input == "" or user_profile_description == "":

        st.error('Please fill both the input fields')

    else:

        extracted_content_from_url = extract_content_from_url(job_post_url_input)

        generate_cold_email_for_job_post = generate_cold_email(extracted_content_from_url, user_profile_description)

        if generate_cold_email_for_job_post:

            st.success('cold email generated successfully')

            st.markdown(generate_cold_email_for_job_post)

            st.write()

            st.write('**Feel free to edit this generated email as your wish.**')
