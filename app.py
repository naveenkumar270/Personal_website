from pathlib import Path
import os
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(os.path.abspath(os.path.dirname(__file__))) if "__file__" in locals() else Path.cwd()
css_code = '''
@import url('https://fonts.googleapis.com/css2?family=Readex+Pro:wght@300;400;500;600;700&display=swap');

* {font-family: 'Readex Pro';}

a {
    text-decoration: none;
    color: white !important;
    font-weight: 500;
}

a:hover {
    color: #d33682 !important;
    text-decoration: none;
}

ul {list-style-type: none;}

hr {
    margin-top: 0px;
    margin-bottom: 5%;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
'''
resume_file = current_dir /"Naveen.pdf"
profile_pic = current_dir /"Naveen.jpg"




# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Naveen Kumar G"
PAGE_ICON = ":wave:"
NAME = "Naveen Kumar G"
DESCRIPTION = """
B.Tech. student in Electronics and Computer Engineering at VIT Chennai, interested in exploring data science.
"""
EMAIL = "naveenkumar67285@gmail.com"
phone = "91+ 9360837080"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/naveen-kumar-g-500469210",
    "Leetcode": "https://leetcode.com/naveen_kumar_g/",
    "GitHub": "https://github.com/naveenkumar270",
    "Kaggle": "https://www.kaggle.com/naveenkum",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
st.markdown(f"<style>{css_code}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.subheader(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)
    st.write("📞",phone)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
  # intro
st.write("\n")
st.subheader("About Me")
st.write("---")
st.write("""Greetings and welcome to my esteemed personal website ! As an Electronics and Computer Engineering student at Vellore Institute of Technology, I have built a strong foundation in programming, circuit design, and electronic components. Through my coursework in Linear Integrated Circuit, Microcontroller, Data Analytics and Visualization, and Machine Learning, I have gained a solid theoretical understanding of these concepts.

My passion for data science has led me to pursue practical experience in data analysis, modeling, and visualization. I am constantly seeking opportunities to expand my skillset and contribute to innovative projects.""")

st.write('\n')


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Pandas,Numpy), C, C++, Java
- 📊 Data Visulization: MS Excel, Matplotlib, Seaborn, Plotly
- 👩‍💻 Web application frameworks: Streamlit
- 🛠️ Tools: Jupyter Nootbook
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("EXPERIENCE")
st.write("---")

# --- JOB 1
st.write("🚧", "**Ashok Leyland LTD., Chennai - Internship**")
st.write("MAY 2022 - JULY 2022")
st.write(
    """
- ► Worked as an intern where I gained hands-on experience with the latest automotive technologies and learned to analyze vehicle parameters using Python programming
- ► Worked with a team of engineers to analyze and optimize vehicle performance using Python-based tools such as Jupyter Notebook, NumPy, and Pandas.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**RapidRoutes | VIT, Chennai - project**")
st.write("SEP 2022 - FEB 2023")
st.write(
    """
- ► In this project I Developed a web application using Python, Pandas, and Streamlit to manage transportation, resulting in efficient allocation of buses based on the number of students and exam schedules.
- ► Utilized data analysis and visualization techniques to optimize transportation management and enhance user experience.
- ► Implemented Pandas and Streamlit to facilitate data processing and web-based interface, respectively, for seamless data management and analysis.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**movie recommendation system | VIT, Chennai - project**")
st.write("JULY 2022 - DEC 2022")
st.write(
    """
- ► Conducted data analysis and pre-processing on a large dataset of user interactions with movies, including ratings and reviews.
- ► Developed a recommendation engine using Python programming to provide personalized movie recommendations to users based on their preferences and behavior.
"""
)

