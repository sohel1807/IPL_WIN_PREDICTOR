import sklearn
import streamlit as st
import pandas as pd
import pickle
pipe=pickle.load(open("pipe.pkl","rb"))
page_by_img='''
<style>
body{
background-image:url("https://wallpapercave.com/wp/wp4059913.jpg");
background-size:cover;
}
</style>
'''
st.markdown(page_by_img,unsafe_allow_html=True)
st.title("IPL PREDICTOR")
team=["Chennai Super Kings","Delhi Capitals","Gujarat Titans","Punjab Kings","Lucknow Super Giants","Mumbai Indians","Kolkata Knight Riders","Rajasthan Royals","Royal Challengers Bangalore","Sunrisers Hyderabad"]
city=['Ahmedabad', 'Kolkata', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai',
       'Abu Dhabi', 'Sharjah', 'Delhi', 'Chennai','Dharmashala', 'Hyderabad',
       'Visakhapatnam', 'Bengaluru', 'Jaipur', 'Bangalore', 'Ranchi',
       'Nagpur', 'Johannesburg', 'Centurion', 'Port Elizabeth', 'Durban',
       'Kimberley', 'East London', 'Cape Town']
col1,col2=st.columns(2)
with col1:
    BattingTeam=st.selectbox("select Batting team",sorted(team))
with col2:
    BowlingTeam=st.selectbox("select Bowling team",sorted(team))
city=st.selectbox("select city",sorted(city))
col3,col4,col5,col6=st.columns(4)
with col3:
    total_run_y=st.number_input("Target")
with col4:
    currentscore=st.number_input("Score")
with col5:
    wickets=st.number_input("Wickets")
with col6:
    overs=st.number_input("overs_completed")
if st.button('Predict probability'):
    runs_left=total_run_y-currentscore
    balls_left=120-(overs*6)
    wickets_left=10-wickets
    CRR=currentscore/(overs+1)
    RRR=(runs_left*6)/balls_left
    final=pd.DataFrame({"BattingTeam":[BattingTeam],"BowlingTeam":[BowlingTeam],"City":[city],"runs_left":[runs_left],"total_run_y":[total_run_y],"balls_left":[balls_left],"wickets_left":[wickets_left],"CRR":[CRR],"RRR":[RRR]})
    result=pipe.predict_proba(final)
    st.text(BattingTeam+":-"+str(round((result[0][1])*100))+"%")
    st.text(BowlingTeam + ":-" + str(round((result[0][0]) * 100))+"%")
