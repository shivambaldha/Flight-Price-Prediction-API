from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import streamlit as st
import datetime
app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))

st.title('Flight Fare Predection Model')

def predict(date_dep, date_arr, Total_stops, airline, Source, Source_d):

    # Date_of_Journey
    # date_dep = request.form["Dep_Time"]
    Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
    Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
    # print("Journey Date : ",Journey_day, Journey_month)

    # Departure
    Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
    Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
    # print("Departure : ",Dep_hour, Dep_min)

    # Arrival
    # date_arr = request.form["Arrival_Time"]
    Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
    Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
    # print("Arrival : ", Arrival_hour, Arrival_min)

    # Duration
    dur_hour = abs(Arrival_hour - Dep_hour)
    dur_min = abs(Arrival_min - Dep_min)
    # print("Duration : ", dur_hour, dur_min)

    # Total Stops
    # Total_stops = int(request.form["stops"])
    Total_stops = int(Total_stops)
    # print(Total_stops)

    # Airline
    # AIR ASIA = 0 (not in column)
    # airline=request.form['airline']
    if(airline=='Jet Airways'):
        Jet_Airways = 1
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 

    elif (airline=='IndiGo'):
        Jet_Airways = 0
        IndiGo = 1
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 

    elif (airline=='Air India'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 1
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
        
    elif (airline=='Multiple carriers'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 1
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
        
    elif (airline=='SpiceJet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 1
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
        
    elif (airline=='Vistara'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 1
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='GoAir'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 1
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='Multiple carriers Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 1
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='Jet Airways Business'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 1
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='Vistara Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 1
        Trujet = 0
        
    elif (airline=='Trujet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 1

    else:
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    # print(Jet_Airways,
    #     IndiGo,
    #     Air_India,
    #     Multiple_carriers,
    #     SpiceJet,
    #     Vistara,
    #     GoAir,
    #     Multiple_carriers_Premium_economy,
    #     Jet_Airways_Business,
    #     Vistara_Premium_economy,
    #     Trujet)

    # Source
    # Banglore = 0 (not in column)
    # Source = request.form["Source"]
    if (Source == 'Delhi'):
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

    elif (Source == 'Kolkata'):
        s_Delhi = 0
        s_Kolkata = 1
        s_Mumbai = 0
        s_Chennai = 0

    elif (Source == 'Mumbai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1
        s_Chennai = 0

    elif (Source == 'Chennai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 1

    else:
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

    # print(s_Delhi,
    #     s_Kolkata,
    #     s_Mumbai,
    #     s_Chennai)

    # Destination
    # Banglore = 0 (not in column)
    # Source_d = request.form["Destination"]
    if (Source_d == 'Cochin'):
        d_Cochin = 1
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
    
    elif (Source_d == 'Delhi'):
        d_Cochin = 0
        d_Delhi = 1
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (Source_d == 'New_Delhi'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 1
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (Source_d == 'Hyderabad'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 1
        d_Kolkata = 0

    elif (Source_d == 'Kolkata'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 1

    else:
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    # print(
    #     d_Cochin,
    #     d_Delhi,
    #     d_New_Delhi,
    #     d_Hyderabad,
    #     d_Kolkata
    # )
    

#     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
#    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
#    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
#    'Airline_Jet Airways', 'Airline_Jet Airways Business',
#    'Airline_Multiple carriers',
#    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
#    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
#    'Source_d_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
#    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
#    'Destination_Kolkata', 'Destination_New Delhi']
    
    prediction=model.predict([[
        Total_stops,
        Journey_day,
        Journey_month,
        Dep_hour,
        Dep_min,
        Arrival_hour,
        Arrival_min,
        dur_hour,
        dur_min,
        Air_India,
        GoAir,
        IndiGo,
        Jet_Airways,
        Jet_Airways_Business,
        Multiple_carriers,
        Multiple_carriers_Premium_economy,
        SpiceJet,
        Trujet,
        Vistara,
        Vistara_Premium_economy,
        s_Chennai,
        s_Delhi,
        s_Kolkata,
        s_Mumbai,
        d_Cochin,
        d_Delhi,
        d_Hyderabad,
        d_Kolkata,
        d_New_Delhi
    ]])

    output=round(prediction[0],2)

    return ("Your Flight price is Rs. {}".format(output))

# (date_dep, date_arr, Total_stops, airline, Source, Source_d):

date_dep = st.date_input(
    "Departure Date" ,
    datetime.date(2019, 7, 6))

date_arr = st.date_input(
    "Arrival Date",
    datetime.date(2019, 7, 7))

Source = st.selectbox(
    'Source',
    ('Delhi', 'Kolkata', 'Mumbai', 'Chennai'))

Source_d = st.selectbox(
    'Destination',
    ('New_Delhi', 'Kolkata', 'Mumbai', 'Hyderabad', 'Cochin'))

airline = st.selectbox(
    'Which Airline you want to travel?',
    ('Trujet', 'GoAir', 'Jet Airways','Air India', 'SpiceJet', 'Vistara'))

Total_stops = st.number_input('Insert a number of Stopage')

# start_date = st.date_input('Enter start date', value=datetime(2019,7,6))
# start_time = st.time_input('Enter start time', datetime.time(8, 45))

btn = st.button("Submit")

if btn:

	a = predict(date_dep, date_arr, Total_stops, airline, Source, Source_d)
	#st.write("The Remaining time Of the Next Earthquake Is")
	#st.subheader('{} Sec'.format(a))
	st.metric(label="Prediction By Model ", value= ('{}'.format(a)))
        

st.write('Copyright © 2020 , Flight Fare Prediction')
st.write('All Rights Reserved Developed & Maintained by Shivam Baldha')
