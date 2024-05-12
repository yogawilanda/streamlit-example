import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlite!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices

# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })

# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))


# get from local server

# server =" http://localhost:1234/v1/models"

# Set up the LM Studio server URL
lm_studio_url = "http://localhost:1234/v1"

# Set up the Streamlit app
st.set_page_config(page_title="LLM Chat App")

# Create a text input for user prompts
prompt = st.text_input("Enter your prompt:")

# Send the prompt to the LM Studio server
response = requests.post(lm_studio_url, json={"prompt": prompt})

# Display the response from the server
st.write(response.text)


