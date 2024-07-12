import streamlit as st
import google.generativeai as palm
from PIL import Image

# Configure the PaLM API
palm.configure(api_key="Enter API KEY")
model_name = "models/text-bison-001"

def generate_resume(name, experience, skills, projects, education, awards, linkedin=None, github=None):
    prompt = f"My name is {name}."
    prompt += f"Experience:\n{experience}\n\n"
    prompt += "\n\nCareer Objective:\nProvide a brief career objective based on the inputs.\n\n"
    prompt += f"Skills:\n{skills}\n\n"

    prompt += "Projects:\nProvide detailed descriptions of the following projects:\n"
    
    for project in projects:
        prompt += f"- {project}\n"

    prompt += f"\nEducation:\n{education}\n\nAwards and Recognition:\n{awards}"
    
    if linkedin or github:
        prompt += "\n\nLinks:\n"
        if linkedin:
            prompt += f"LinkedIn: {linkedin}\n"
        if github:
            prompt += f"GitHub: {github}\n"

    response = palm.generate_text(model=model_name, prompt=prompt, temperature=0)
    return response.result


def generate_cover_letter(company_name, job_title):
    prompt = f"I am interested in the {job_title} position at {company_name}."
    response = palm.generate_text(model=model_name, prompt=prompt,temperature=0)
    return response.result

def generate_interview_questions(skills):
    prompt = f"Generate interview questions based on my {skills}?"
    response = palm.generate_text(model=model_name, prompt=prompt,temperature=0)
    return response.result

def add_logo(logo_path, width, height):
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

def main():
    st.sidebar.header("**Start Your Journey**")

    im = Image.open('logo/job.jpg')
    resize = im.resize((200, 200))
    st.sidebar.image(resize)
    st.sidebar.markdown("Whether you're a recent graduate, a career changer, or a professional seeking advancement, JobSwift is here to support your career aspirations. Let's get started!")
    option = st.sidebar.selectbox("Select Option", ["Home", "Generate Resume", "Generate Cover Letter", "Generate Interview Questions"])

    content_placeholder = st.empty()

    if option == "Home":
        with content_placeholder.container():
            st.title("Jobswift: Accelerating Careers With AI-Powered Applications")
            st.markdown("""
            # Welcome to JobSwift!

            JobSwift is an innovative platform leveraging AI technology to streamline the job application process and empower users in their career advancement journey. 

            ## User Guidelines

            1. **Accurate Information**: Please ensure that all information you provide, including career details, skills, and job preferences, is accurate and up-to-date.
            2. **Personalization**: Use the platform to generate personalized resumes, cover letters, and interview preparation materials that reflect your unique profile and career goals.
            3. **Privacy**: Your data is confidential and will only be used to enhance your job application materials. We prioritize your privacy and data security.
    
            """)

    elif option == "Generate Resume":
        with content_placeholder.container():
            st.subheader("Generate Resume")
            name = st.text_input("Enter Your Name")
            experience = st.text_input("Enter Your Experience in Years")
            skills = st.text_area("Enter Your Skills")
            projects = st.text_area("Enter Your Projects")
            education = st.text_area("Enter Your Education")
            awards = st.text_area("Enter Your Awards and Recognition")
            linkedin=st.text_input("Enter LinkedIn profile(Optional)")
            github=st.text_input("Enter Github profile(Optional)")
            if st.button("Generate Resume"):
                if name and experience and skills and projects and education and awards:
                    st.write(generate_resume(name, experience, skills, projects, education, awards,linkedin,github))
                else:
                    st.error("Please fill all the fields")

    elif option == "Generate Cover Letter":
        with content_placeholder.container():
            st.subheader("Generate Cover Letter")
            company_name = st.text_input("Enter Company Name")
            job_title = st.text_input("Enter Job Title")
            if st.button("Generate Cover Letter"):
                if company_name and job_title:
                    st.write(generate_cover_letter(company_name, job_title))
                else:
                    st.error("Please fill all the fields")

    elif option == "Generate Interview Questions":
        with content_placeholder.container():
            st.subheader("Generate Interview Questions")
            skills = st.text_area("Enter your skills")
            if st.button("Generate Interview Questions"):
                if skills:
                    st.write(generate_interview_questions(skills))
                else:
                    st.error("Please fill all the fields")

main()
