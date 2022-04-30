import streamlit as st
from multiapp import MultiApp
import home, notebook


app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Notebook", notebook.app)
app.run()