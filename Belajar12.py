
import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Fathul Muhtadi S.H.,
##### *Resume* 
''')


image = Image.open('fathulcartoon.jpeg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Detail cost control around with over 2 years of experience in monitoring analyze project
 expense adherence to budget constraints.adept collaborating with project teams based on data 
- Dicipline, Strong Character, Hydbrid Work, loyally employee
- Advantage cost control skills (Earn Value Management,Cost Clasification, Cost Control, Cost Reporting, 
  Planning Control & Budgetting, Cost Allocation, Cost Tracking, SAP)
''')
#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="" target="_blank">Fathul Muhtadi</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#courses">Courses</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work-Experience</a>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################

#####################
st.markdown('''
## Work-Experience
# ''')

txt('**Cost Control** [Jurong Engineering Lestari]','November 2022 - Now')

st.markdown('''
- Coordimation and collaboration with site management for making WBS Element
- Budget Documentation, Invoice, Cost Bid Tabulation
- Handling and coordination with my lead cost control to project builder in SAP
- Handling and coordination with my lead cost control to change project status
- Coordination with  project control for making revenue planning 
- Coordination with project manager for making cost planning
- Creation Of Budget
- Coordination with procurement site for Maintain Service Entry
- Release Service Entry
- Reviewing and documentation CBT document, Invoicing vendor, actuals, and forecast
- Driving cost control across the project team
- Assisting in monthly forecasts (updating cost and forecast)
- Implementing baseline changes in the cost control tool (reclass cost)
- Control monthly payroll an
''')

txt('**Cost Control** [Gunanusa Utama Fabricators]','Mei 2022 - Oktober 2022')

st.markdown('''
- Reporting Weekly Report Progress Project
- Reporting Monthly Report Cost Project from other division
- Analyze data supporting progress portion
- Analyze variant progress claim from subcontractor
- Payment Monitoring
- Collecting data, reporting, and Vessel offshore from subcontractor
- Monitoring Electrical, Instrument, and Telcom works
''')

txt('**Cost Control** [Recon Sarana Utama]','December 2021 - April 2022')

st.markdown('''
- Controlling budget with charts in excel
- Verify Invoice data to site project, procurement division, and finance division
- Verify Contract & Purchase Order to procurement and provide information about the impact with Monthly Report Cost Management
- Cleaning data from several divisions with power query, formula and dax measure
- Calculated recorded cost, unrecorded cost, remaining contract, comitted to date, estimate to complete, 
  estimate at completion, incoming invoice
- Verify Contract & Purchase Order to procurement and provide information about the impact with Monthly Monitoring 
  cash flow from report finance site project, and finance division
  Monitoring cash flow in chart Monthly Report Cost Management 
''')

txt('**General Affair** [Recon Sarana Utama]','March 2018 - September 2021')

st.markdown('''
- Controlling budget with charts in excel
- Verify Invoice data to site project, procurement division, and finance division
- Verify Contract & Purchase Order to procurement and provide information about the impact with Monthly Report Cost Management
- Cleaning data from several divisions with power query, formula and dax measure
- Calculated recorded cost, unrecorded cost, remaining contract, comitted to date, estimate to complete, 
  estimate at completion, incoming invoice
- Verify Contract & Purchase Order to procurement and provide information about the impact with Monthly Monitoring 
  cash flow from report finance site project, and finance division
  Monitoring cash flow in chart Monthly Report Cost Management 
- Payroll Calculation in excel
- Calculated Field Expenses for cost site project
- Calculate back end orders consumable material in excel
- Verify invoice price to vendor ,reporting to Project Manager and Project Control
- Making Offering Letter and Contract employee, reporting to Project Manager
- Supporting administration and documentation in or out employee,reporting to Project
- Manager and Project Control
- Supporting administration and documentation leaving on employee
- Supporting administration and documentation tools of work
- Supporting administration and documentation Consumable for employee 
- Supporting administration and documentation cleanliness of the employee residence
- Supporting administration and documentation in or out employee and reporting to Project
  Manager and Project Control
''')

#####################
st.markdown('''
## Courses
# ''')

txt('**Primavera Basic** [Komunitas Project Control Bersatu]','Des-2023')

st.markdown('''
- Cost Clasification
- Cost Control
- Cost Reporting
''')

txt('**Project Cost Control In Oil And Gas** [Improove Skills]','Des-2023')

st.markdown('''
- Create a baseline
- Reading schedule
- Update schedule
- Critical Path Method
''')

txt('**ISO Courses** [PT Mutiara Mutu Sertifikasi]','June-2023')

st.markdown('''
- ISO 9001:2015
- ISO 14001:2015
- ISO 45001:2018
- ISO 19011:2018
''')

txt('**Supply Chain Management for Oil And Gas Program** [Bangun Energy]','February-2023')

st.markdown('''
- Introduction to Supply Chain Management in Oil and Gas Industry
- Defining Contracting and Procurement Strategy in Oil and Gas Capital Project
- Material management in Capital Project
- Contract Strategy Tactics
- Managing supply chain performance in oil and gas
- Contract Series (Contract administration, Contract Provision, Claim Management)
- Responsible Supply Chain
''')

txt('**Data Science For Accounting Program** [Narasio Data]','January-2023')

st.markdown('''
- Data Preparation
- Predictive Analytics - Regression
- Predictive Analytics - Clasification
- Binary Classification (Decision Tree)
- Diagnostics Analytics - Clustering
- Clustering
- Hiearchical Clustering
- Time series analysis
- Time Series (Arima)
- Mini Project 1  (Loan Construct Portofolio)
''')

txt('**Data Analytics For Accounting Program** [Narasio Data]','January-2023')

st.markdown('''
- Introduction Data Analytics
- Model Cycle Process
- Relational Database
- Pivot Table
- Introduction Power Pivot
- Introduction of Power Query
- Introduction to Python Pandas
- Exploring Dataframe With Pandas
- Statistics for Data analyst Part 1
- Statistics for Data Analyst Part 2
- Introduction to Power BI
- Run Python Script in Power BI
''')

txt('**Budgetting & Cost Control** [Eltasa Prima Konsulta]','December-2022')

st.markdown('''
- Planning Control & Budgetting
- Master Budgets
- Operating Budgets
- Financial Budgets
- Flexible Budget (activity level)
- Budget Committe
- Budgetary Control
- Preparation of the Budget
- Features of an effective budget
- Problems with budgeting
- Standarts Cost System
- Cost Allocation
''')

txt('**Project Management with Primavera** [Eltasa Prima Konsulta]','December-2022')

st.markdown('''
- Introduction Primavera
- Create EPS & OBS
- Create New Files
- Set & Display Layout
- Create Calendar
- Create WBS
- Create Activity
- Create Relationship  
- Create Baseline
- Create Resource
- Tracking Project 
- Display Print Preview & Report 
''')

txt('**Implementation Of Schedulre Risk Analysis In Project** [Bangun Energy]','July-2022')

st.markdown('''
- Home Work Project
- Schedule Risk Register
- Schedule Risk Analysis
''')

txt('**Energy Audit** [Institute Teknologi Surabaya]','July-2022')

st.markdown('''
- Audit Preparation
- Planning Audit 
- Collecting Data And Analyze
- Rootcause Analysis
''')

txt('**EDA** [Shift Academy]','June-2022')

st.markdown('''
- Basic Python
- EDA
- Data Modelling
- Statistica Model
- Dashboard
''')

txt('**Data Story Telling** [Shift Academy]','June-2022')

st.markdown('''
- Context
- Data Visualization
- Structure And Story Arc
''')

txt('**Data Analysis and Reporting with Excel** [Shift Academy]','June-2022')

st.markdown('''
- Cell, table name, wildcard characters, data and type conversion, popular basic function
- Advance name, decision and logics, data validation
- Choose, vlookup, offset, match-index, volatile function
- Advance index-match, data validation and form
''')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python Basic`,`Visual Basic`')
txt3('Data processing/wrangling', '`pandas`,`Power Query`')
txt3('Data visualization', '`Power BI`,`Excel`')
txt3('Machine Learning', '`Timeseries`')
txt3('Model deployment', '`streamlit`')
txt3('Cost Control', '`Earn Value Management`,`Cost Clasification`, `Cost Control`, `Cost Reporting`, `Planning Control & Budgetting`,`Cost Allocation`, `Cost Tracking`, `SAP`')
