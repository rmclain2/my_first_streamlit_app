from gettext import install
from lib2to3.pgen2.pgen import DFAState
import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create."
)

x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(start=0, stop=101, step=1)

# Create a random array of data that we will use for our y values
y_data = np.random.rand(101)*100
df = pd.DataFrame({'X data': x_axis,
                     'Y data': y_data})
st.dataframe(df)


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
)

scatter = alt.Chart(df).mark_point().encode(
    x='X data',
    y='Y data'
)
st.altair_chart(scatter, use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

scatter = alt.Chart(df).mark_point().encode(
    x='X data',
    y='Y data',
    tooltip=['X data', 'Y data']).properties(
        title = 'Random X and Y Data'
    ).configure_mark(
         color = 'purple',
         opacity = 0.6,
         filled = True,

    ).interactive()
st.altair_chart(scatter, use_container_width=True)

st.markdown("""
The 5 changes I made were:
- Changing the color of the data points to purple
- Changing the opacity of the data points to 0.6
- Change the datapoints so they were filled instead of empty
- Adding a tooltip to each datapoint displaying the coordinate value
- Added a title to the chart
""")

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html. \n"
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual. \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

x = np.arange(100)
source = pd.DataFrame({
  'x': x,
  'f(x)': np.sin(x / 5)
})

line = alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)'
).properties(
        title = 'Random Github Line Chart').interactive()

st.altair_chart(line, use_container_width=True)

st.markdown("""
The 2 changes I made were:
- Changing the title of the chart
- Making the data interactive (can zoom and move side to side or up and down)
"""
)






