#requirements.txt 필요

#from tkinter import W
import streamlit as st

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

from utils.pages.home import home
from utils.pages.age import age
from utils.pages.average import average
from utils.pages.bmi import bmi
from utils.pages.smoking import smoking
from utils.pages.observation import observation
from utils.pages.predict_charges import predict_charges


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        st.set_page_config(page_title="EDA on Medical Cost", layout="wide")

        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.selectbox(
            "Select Page", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        app["function"]()


app = MultiApp()

app.add_app("Home Page", home)
app.add_app("EDA-Age", age)
app.add_app("EDA-Smoking", smoking)
app.add_app("EDA-BMI", bmi)
app.add_app("Observation", observation)
app.add_app("Compute average cost", average)
app.add_app("Compute expecting cost", predict_charges)

app.run()
