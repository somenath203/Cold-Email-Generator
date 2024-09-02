# Cold Email Generator

## Demo video of the project

 ![Screenshot (699)](https://github.com/user-attachments/assets/25d18317-2a50-4d53-96b0-ff9618404309)
 
https://www.youtube.com/watch?v=ji9AfqqClrA

## Introduction

The Cold Email Generator is a web application designed to help job seekers create personalized cold emails tailored to specific job postings. By providing the URL of a job post and a brief description of your skills and experience, the application automatically generates a well-crafted email to increase your chances of securing an interview.

## Features of the Application

- **Automatic Content Extraction**: The application extracts the job description directly from the provided URL, ensuring that the email is tailored specifically to the job post.
- **Personalized Email Generation**: It uses the ChatGroq language model to generate a concise and effective cold email based on the job description and your profile information.
- **User-Friendly Interface**: The app provides a simple and intuitive interface where you can easily input the necessary information and receive your email in seconds.

## Technologies Used

- **Streamlit**: Used for building the user interface of the application.
- **LangChain**: Utilized for creating the email generation prompt and managing the flow between the extracted job description and the language model.
- **ChatGroq (LLaMA-3.1-70B-Versatile)**: A highly advanced language model with 70 billion parameters, used to generate contextually relevant and personalized cold emails that are specifically created to match the job description and user profile.
- **Langchain Community WebBaseLoader**: Employed for web scraping to extract content from the job post URL.

## Disclaimer

The creator of this application is not responsible for any incorrect content created as LLaMA-3.1-70B's functioning is beyond the creator's control.
