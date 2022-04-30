import streamlit as st
import codecs
import streamlit.components.v1 as stc


def app():
	f=codecs.open("SMS Spam Detection.html", 'r', encoding='utf-8')
	page = f.read()

	stc.html(page, width=700, height=1000, scrolling=True)