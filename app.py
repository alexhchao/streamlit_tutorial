# Streamlit crash course
# https://www.youtube.com/watch?v=_9WiB2PDO7k
import numpy as np
import streamlit as st 

# Text / tilte
st.title("Streamlit Tutorials")

# header 

st.header("This is a header")

st.subheader("This is a subheader")

#text
st.text("Hello Streamlit")

# markdown
st.markdown("### This is a markdown")

# error / colorful text

st.success("Successful")

st.info("Information")

st.warning("Warning")

st.error("Error")

st.exception("NameError('name not defined')")

# Get Help Info About Python 

st.help(range)

# writing Text / Super Fxn

st.write("Text with write")

st.write(range(10))

# Widget
# Checkbox

if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")


# Radio buttons

status = st.radio("What is the status", ("Active","Inactive"))

if status == 'Active':
	st.success("You are active")
else:
	st.warning("You are Inactive")

# Select box 
occupation = st.selectbox("Your Occupation", ("Programmer",
	"Data Scientist", "Doctor","Lawyer"))

st.write(f"You selected {occupation}")

# Multi select
location = st.multiselect("Where do you work", ("London","New York","Paris"))

st.write(f"You selected {location}")

# Slider

age = st.slider("What is your age",1,99)

st.write(f"your age is {age}")

# Buttons

st.button("Simple Button")

if st.button("About"):
	st.text("Streamlit is cool")

# Text Input 
firstname = st.text_input("Enter your first name")

st.write(f"Your name is {firstname}")

if st.button("Submit"):
	result = firstname.title()
	st.success(result)

# text area 
message = st.text_area("Enter your message")
if st.button("Submit2"):
	result = message.title()
	st.success(result)

# Date input
import datetime

today = st.date_input("Today is", datetime.datetime.now())

# Time

the_time = st.time_input("The time is", datetime.time())

# Display JSON

st.text("Displaying JSON")
#st.json({'name':"Jesse", 'gender':"male"})

st.text("Display Raw Code")

# Display raw code
st.code("import numpy as np")

with st.echo():
	# This will aslo show as a comment
	import pandas as pd
	df = pd.DataFrame()

# Progress Bar
import time

#my_bar = st.progress(0)

#for p in range(10):#
#	my_bar.progress(p+1)


# Spinner
#with st.spinner("Waiting.."):#
#	time.sleep(5)

#st.success("Finished")

# Balloons

#st.balloons()

# Side bars

st.sidebar.header("About")
st.sidebar.text("This is streamlit tutorial")
st.sidebar.selectbox("Name",("Alex","Bob"))
st.sidebar.multiselect("Name",("Alex","Bob"))

# functions
@st.cache
def run_fxn():
	return range(100)

st.write(run_fxn())

# plots

#st.pyplot()

# DataFrames

df = pd.DataFrame({'Alex':[1,2,3],'Bob':[2,3,4]})

# can be sorted
#st.dataframe(df)

# Tables
st.table(df)

##################
# now with another tutorial
# https://towardsdatascience.com/streamlit-101-an-in-depth-introduction-fc8aad9492f2

# @st.cache
# def get_data():
#     url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
#     return pd.read_csv(url)
# df = get_data()

# cols = ["name", "host_name", "neighbourhood", "room_type", "price"]
# st_ms = st.multiselect("Columns", df.columns.tolist(), default=cols)

# values = st.sidebar.slider("Price range", float(df.price.min()), float(df.price.max()), 
# 	(50., 300.))
# st.write(values)
# output = df.loc[:,st_ms]

# st.dataframe(output[(output['price']>= values[0])&(output['price'] <= values[1])])
#st.dataframe(output.query("price.between{values}"))

# f = px.histogram(df.query(f”price.between{values}”), x=”price”, nbins=15, title=”Price distribution”)
# f.update_xaxes(title=”Price”)
# f.update_yaxes(title=”No. of listings”)
# st.plotly_chart(f)

#import plotly.express as px

# f = px.histogram(df.query(f"price.between{values}"), x="price", 
# 	nbins=15, title="Price distribution")
# f.update_xaxes(title="Price")
# f.update_yaxes(title="No. of listings")
# st.plotly_chart(f)

chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#
import matplotlib.pyplot as plt

arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)

st.pyplot()