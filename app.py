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

leetcode_emoji = '\U0001F5F3'



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
