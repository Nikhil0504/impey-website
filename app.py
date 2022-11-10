import pandas as pd
import streamlit as st

from constants import CATEGORIES, PEOPLE

if "button1" not in st.session_state:
    st.session_state.button_1 = False


def cb1():
    st.session_state.button_1 = True


data = pd.read_pickle("Datasets/links.pkl")
st.title("Link Input Website")


main1, main2 = st.columns(2)

with main1:
    option = st.selectbox("Who are you?", PEOPLE)

with main2:
    c = st.selectbox("Categories", CATEGORIES)

col1, col2, col3 = st.columns(3)

with col1:
    url = st.text_input("Enter URL: ")

with col2:
    rf = st.radio("Real or Fake", ("Real", "Fake"), horizontal=True)

with col3:
    sub = st.button("Submit")

if sub:
    if url in data["URL"].values:
        st.warning("This website has already been entered by someone else.", icon="⚠️")
        ind = data.index[data["URL"] == url].tolist()
        data.at[ind[0], option] = rf
    else:
        row = {"URL": [url], "Categories": [c], option: [rf]}
        new_entry_df = pd.DataFrame.from_dict(row)
        data = data.append(new_entry_df, ignore_index=True)
    data.to_pickle("Datasets/links.pkl")

if st.button("Show URLs"):
    st.dataframe(data['URL'], use_container_width=True)
