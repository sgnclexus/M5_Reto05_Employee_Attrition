import streamlit as st
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DATA_URL = 'Employees.csv'



@st.cache_data
def load_data(nrows):
    
    data = pd.DataFrame()

    if(nrows == -1):
        data = pd.read_csv(DATA_URL)
    else:
        data = pd.read_csv(DATA_URL, nrows=nrows)

    return data


st.title('R05 Employee Attrition')
st.header(':gray[_Dataframe:bar_chart:_]')
#st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')
#st.dataframe(load_data(5))

# We fill our pandas dataframe
dfEmployeeAttrition = load_data(-1)

placeholder = st.empty()
container = st.container()

st.markdown("___")

fig, ax = plt.subplots()
ax.hist(dfEmployeeAttrition.Age)
st.header("Age Histogram")
st.pyplot(fig)

st.markdown("___")


fig2, ax = plt.subplots()
ax = sns.countplot(x=dfEmployeeAttrition['Unit'])
ax.set_title('Employees by Unit')
plt.xticks(rotation=90)
for label in ax.containers:
  ax.bar_label(label)
try:
    st.pyplot(fig2)    
except Exception as e:
    st.exception(e)

st.markdown("___")

employees_by_hometown = dfEmployeeAttrition.groupby(['Hometown'])[['Attrition_rate']].mean()

#st.dataframe(employees_by_hometown)

fig3, ax = plt.subplots()
ax.pie(employees_by_hometown.Attrition_rate, labels=employees_by_hometown.index,  autopct='%1.1f%%')
ax.set_title('Attrition rate grouped by hometown')
#ax.set_ylabel('')

st.pyplot(fig3)

st.markdown("___")

attition_by_age = dfEmployeeAttrition.groupby(['Age'])[['Attrition_rate']].mean()
fig4, ax = plt.subplots()
ax.plot(attition_by_age.index, attition_by_age.Attrition_rate)
ax.set_title('Attrition rate grouped by age')
#ax.set_ylabel('')

st.pyplot(fig4)


st.markdown("___")

fig5, ax = plt.subplots()
ax.scatter(x=dfEmployeeAttrition.Time_of_service, y=dfEmployeeAttrition.Attrition_rate)
ax.set_title('Time of service vs Attrition rate')
st.pyplot(fig5)

##################################################################
# Filters for sidebar
##################################################################
sidebar = st.sidebar
sidebar.title('Filters')

agree = sidebar.checkbox('Show datasource : ')

if agree:
    #dfFilterEmployeesAttrition = st.dataframe(dfEmployeeAttrition)
    with placeholder.container():
        st.write(dfEmployeeAttrition)

sidebar.markdown("##")

fEmployeeID = sidebar.text_input('Employee ID : ')

if sidebar.button('Search by ID'):
    st.write(fEmployeeID)
    #dfFilterEmployeesAttrition = st.dataframe(dfEmployeeAttrition.loc[dfEmployeeAttrition['Employee_ID'] == fEmployeeID])
    with placeholder.container():    
        st.write(dfEmployeeAttrition.loc[dfEmployeeAttrition['Employee_ID'] == fEmployeeID])

sidebar.markdown("___")        

fUnit = sidebar.radio('Select Unit : ', load_data(-1)['Unit'].unique())
fHometown = sidebar.multiselect('Select Hometown : ', options=load_data(-1)['Hometown'].unique(), default=load_data(-1)['Hometown'].unique())

if sidebar.button('Search by Unit and Hometown'):
    with placeholder.container():    
        st.write(dfEmployeeAttrition.query("Unit == @fUnit & Hometown == @fHometown"))


#df_selection=df.query("gender == @gender & performance_score == @performance_score & marital_status == @marital_status")