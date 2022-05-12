import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import base64
st.set_page_config(page_title="Retical", layout="wide")

col1, mid, col2,col4 = st.columns([1,1,100,100])
with mid:
    st.image('1611261.png',width=100)
with col2:
    st.title('Retirement Calculator ')


col1, col2 = st.columns(2)
with col1:
    st.header("Retirement Calculator for scenario 1")
    with st.form(key='inputs_form1'):
        name = st.text_input("Name ")
        age = st.slider("Age", 1, 100,30)
        #Scenario = st.selectbox("Choose Scenario",options=[1,2,3])
        currentsalary = st.number_input(" Annual Income ($)" , min_value=0.00,value=60000.00)
        Avg_sal_return = st.number_input("Annual savings (%) " , min_value=0.00,value=10.00)
        Current_nest = st.number_input("Current Retirement Savings ($) " , min_value=0.00,value=00.00)
        Expected_salary_increase = st.number_input("Expected Salary Increase per year (%)" , min_value=0.00,value=2.00)
        Inflation = st.number_input("Inflation (%)",min_value=0.00,value=1.50)
        Interest = st.number_input("Interest rate on saving (%)" ,min_value=0.00,value=4.50)
        Interest_rate_after_retirememt = st.number_input("Interest rate during retirement (%)" ,min_value=0.00,value=4.00)
        Rate_of_SSA = st.number_input("Rate of SSA (%)" ,min_value=0.00,value=1.25)
        retirement_age= st.slider("Age of retirement ", 1, 100, value=70)
        active_year= st.slider(" Till what age you considered yourself in active age ", 1, 100, 80)
        Income_at_ret = st.number_input("Income required at Retirement for active years ($)" ,min_value=0.00,value=44000.00)
        Income_at_ret_after = st.number_input("Income required at Retirement after active years($)" ,min_value=0.00,value=44000.00)
        ssa_amt = st.number_input("Social Security Amount ($)" , min_value=0.00,value=0.00)
        submit_btn1 = st.form_submit_button(label='submit')



with col2:
    st.header("Retirement Calculator for scenario 2")
    with st.form(key='inputs_form2'):
            name2 = st.text_input("Name ")
            age2 = st.slider("Age", 1, 100,30)
            #Scenario2 = st.selectbox("Choose Scenario",options=[1,2,3])
            currentsalary2 = st.number_input(" Annual Income ($)" ,min_value=0.00,value=60000.00)
            Avg_sal_return2 = st.number_input("Annual savings (%) " ,min_value=0.00,value=10.00)
            Current_nest2 = st.number_input("Current Retirement Savings ($) " ,min_value=0.00,value=00.00)
            Expected_salary_increase2 = st.number_input("Expected Salary Increase per year (%)" ,min_value=0.00,value=2.00)
            Inflation2 = st.number_input("Inflation (%)",min_value=0.00,value=1.25)
            Interest2 = st.number_input("Interest rate on saving (%)" ,min_value=0.00,value=4.50)
            Interest_rate_after_retirememt2 = st.number_input("Interest rate during retirement (%)" ,min_value=0.00,value=4.00)
            Rate_of_SSA2 = st.number_input("Rate of SSA (%)" ,min_value=0.00,value=1.25)
            retirement_age2= st.slider("Age of retirement ", 1, 100, 62)
            active_year2= st.slider(" Till what age you considered yourself in active age ", 1, 100, 80)
            Income_at_ret2 = st.number_input("Income required at Retirement for active years ($)" ,min_value=0.00,value=52000.00)
            Income_at_ret_after2 = st.number_input("Income required at Retirement after active years($)" ,min_value=0.00,value=62500.00)
            ssa_amt2 = st.number_input("Social Security Amount ($)" , min_value=0.00,value=29327.00)
            submit_btn2 = st.form_submit_button(label='submit')


with st.form(key='inputs_form3'):
    submit_btn12 = st.form_submit_button(label='Click to see report for both Scenarios ')
col1, col2 = st.columns(2)

if submit_btn1:
   with col1:
       st.title('    Report for Run 1  ')
       st.write(f'Name : {name}')
       st.write(f'Age : {age}')
       st.write(f'No of years for retirement : {retirement_age-age}')
       st.write(f'Inflation : {Inflation} %')
       st.write(f'Retirement Age : {retirement_age}')
       st.write(f'Active Age after retirement: {active_year}')
       st.write(f'Expected increment per year in salary:  {Expected_salary_increase} %')
       st.write(f'Interest you will get on your saving : {Interest} %')
       st.write(f'Annual saving : {Avg_sal_return} %')



       df = pd.DataFrame(columns=['Age','Current Salary','Retirement Income  $','Retirement Balance  $'])
       while age < retirement_age :
           saving  = round(((Current_nest+(Current_nest * Interest)/100)+((currentsalary*Avg_sal_return)/100)),2)
           df.loc[age, ['Retirement Balance  $']] = round(saving,2)
           df.loc[age, ['Age']] = round(age,2)
           df.loc[age, ['Retirement Income  $']] = round(0,2)
           df.loc[age, ['Current Salary']] = round(currentsalary,2)
           Current_nest = round(((Current_nest+(Current_nest * Interest)/100)+((currentsalary*Avg_sal_return)/100)),2)
           currentsalary = round(currentsalary+((currentsalary*Expected_salary_increase)/100),2)
           age = age + 1


       while (retirement_age) < (active_year) :
           saving2  = round(((Current_nest+ssa_amt+((Current_nest * Interest_rate_after_retirememt)/100))-Income_at_ret),2)
           df.loc[retirement_age, ['Retirement Balance  $']] = round(saving2,2)
           df.loc[retirement_age, ['Age']] = round(retirement_age,2)
           df.loc[retirement_age, ['Retirement Income  $']] = round(Income_at_ret,2)
           df.loc[retirement_age, ['Current Salary']] = round(0,2)
           Current_nest = round(((Current_nest+ssa_amt+((Current_nest * Interest_rate_after_retirememt)/100))-Income_at_ret),2)
           retirement_age = retirement_age + 1
           Income_at_ret = round(Income_at_ret+((Income_at_ret*Inflation)/100),2)
           ssa_amt=round(ssa_amt+((ssa_amt*Rate_of_SSA)/100),2)


       after_active_Age = active_year
       while (after_active_Age) < 101 :

           saving3  = round((Current_nest+ssa_amt+(Current_nest * Interest_rate_after_retirememt)/100)-Income_at_ret_after,2)
           df.loc[after_active_Age, ['Retirement Balance  $']] = round(saving3,2)
           df.loc[after_active_Age, ['Age']] = round(after_active_Age,2)
           df.loc[after_active_Age, ['Retirement Income  $']] = round(Income_at_ret_after,2)
           df.loc[after_active_Age, ['Current Salary']] = round(0,2)
           Current_nest = round((Current_nest+ssa_amt+(Current_nest * Interest_rate_after_retirememt)/100)-Income_at_ret_after,2)
           Income_at_ret_after = round(Income_at_ret_after+((Income_at_ret_after*Inflation)/100),2)
           after_active_Age = after_active_Age + 1
           ssa_amt=round(ssa_amt+((ssa_amt*Rate_of_SSA)/100),2)

       df = df.round(0)
       df
       Max_Balance = round(df["Retirement Balance  $"].max(),2)
       Sum_Balance = round(df["Retirement Balance  $"].sum(),2)

       #Balance_at_100 = round((df.loc[df["Retirement Balance $"] == 100]),2)
           #col3.write(f' Retirement Savings :  $ {saving}')
           #col2.write(f'Total amount at the time of retirement  : {saving}' )

       #c#ol1, col2 = st.columns(2)

       #with col1:

       st.write(f'Maximum size of retirement Savings: {Max_Balance}')
       st.write(f'Total dollar received: {Sum_Balance}')

       def to_excel(df):
               output = BytesIO()
               writer = pd.ExcelWriter(output, engine='xlsxwriter')
               df.to_excel(writer, index=False, sheet_name='Sheet1')
               workbook = writer.book
               worksheet = writer.sheets['Sheet1']
               format1 = workbook.add_format({'num_format': '0.00'})
               worksheet.set_column('A:A', None, format1)
               writer.save()
               processed_data = output.getvalue()
               return processed_data
       df_xlsx = to_excel(df)
       st.download_button(label='Download Table Data',
                                           data=df_xlsx ,
                                        file_name= 'Retirement income_secanrio1.xlsx')

       dfa = df.drop(columns=['Retirement Balance  $','Current Salary'])
       chart_data1 = pd.DataFrame(
       dfa,
       columns=['Age','Retirement Income  $'])
       st.line_chart(chart_data1)

       dfb = df.drop(columns=['Retirement Income  $'])
       chart_data2 = pd.DataFrame(
       dfb,
       columns=['Age','Retirement Balance  $',])
       st.line_chart(chart_data2)

if submit_btn2:
   with col1:
       st.title('    Report for Run 2  ')
       #col1, col2 ,col3= st.columns(3)
       st.write(f'Name : {name2}')
       st.write(f'Age : {age2}')
       st.write(f'No of years for retirement : {retirement_age2-age2}')
       st.write(f'Inflation : {Inflation2} %')
       st.write(f'Retirement Age : {retirement_age2}')
       st.write(f'Active Age after retirement: {active_year2}')
       st.write(f'Expected increment per year in salary:  {Expected_salary_increase2} %')
       st.write(f'Interest you will get on your saving : {Interest2} %')
       st.write(f'Annual saving : {Avg_sal_return2} %')


       df2 = pd.DataFrame(columns=['Age','Current Salary','Retirement Income  $','Retirement Balance  $'])
       while age2 < retirement_age2 :
           saving2  = round(((Current_nest2+(Current_nest2 * Interest2)/100)+((currentsalary2*Avg_sal_return2)/100)),2)
           #col3.write(f'Total retirement Balance at age {age} :  $ {saving}' )
           df2.loc[age2, ['Retirement Balance  $']] = round(saving2,2)
           df2.loc[age2, ['Age']] = round(age2,2)
           df2.loc[age2, ['Retirement Income  $']] = round(0,2)
           df2.loc[age2, ['Current Salary']] = round(currentsalary2,2)
           Current_nest2 = round(((Current_nest2+(Current_nest2 * Interest2)/100)+((currentsalary2*Avg_sal_return2)/100)),2)
           currentsalary2 = round(currentsalary2+((currentsalary2*Expected_salary_increase2)/100),2)
           age2 = age2 + 1

           #col1.write(f'Amount you will get at age (active years)  :  $ {Income_at_ret}')

       #retirement_age=retirement_age+1
       #Interest_rate_after_retirememt2=4.00
       #Rate_of_SSA2=1.25
       while (retirement_age2) < (active_year2) :
           #col3.write(f' Retirement Savings :  $ {saving}')
           saving2  = round(((Current_nest2+ssa_amt2+((Current_nest2 * Interest_rate_after_retirememt2)/100))-Income_at_ret2),2)
           df2.loc[retirement_age2, ['Retirement Balance  $']] = round(saving2,2)
           df2.loc[retirement_age2, ['Age']] = round(retirement_age2,2)
           df2.loc[retirement_age2, ['Retirement Income  $']] = round(Income_at_ret2,2)
           df2.loc[retirement_age2, ['Current Salary']] = round(0,2)
           #col1.write(f'Amount you will get at age {retirement_age}  :  $ {Income_at_ret}')
           #col2.write(f' Total Retirement Balance at age {retirement_age}:  $ {saving2}')
           Current_nest2 = round(((Current_nest2+ssa_amt2+((Current_nest2 * Interest_rate_after_retirememt2)/100))-Income_at_ret2),2)
           retirement_age2 = retirement_age2 + 1
           Income_at_ret2 = round(Income_at_ret2+((Income_at_ret2*Inflation2)/100),2)
           ssa_amt2=round(ssa_amt2+((ssa_amt2*Rate_of_SSA2)/100),2)
       #col2.write(f'Amount you will get at age {active_year}  :  $ {Income_at_ret_after}')
       #after_active_Age = (active_year-1)
       after_active_Age2 = active_year2
       while (after_active_Age2) < 101 :

           saving3  = round((Current_nest2+ssa_amt2+(Current_nest2 * Interest_rate_after_retirememt2)/100)-Income_at_ret_after2,2)
           df2.loc[after_active_Age2, ['Retirement Balance  $']] = round(saving3,2)
           df2.loc[after_active_Age2, ['Age']] = round(after_active_Age2,2)
           df2.loc[after_active_Age2, ['Retirement Income  $']] = round(Income_at_ret_after2,2)
           df2.loc[after_active_Age2, ['Current Salary']] = round(0,2)
           #col1.write(f'Amount you will get at age {after_active_Age}  :  $ {Income_at_ret_after}')
           #col2.write(f' Total Retirement Balance at age {after_active_Age}:  $ {saving3}')
           Current_nest2 = round((Current_nest2+ssa_amt2+(Current_nest2 * Interest_rate_after_retirememt2)/100)-Income_at_ret_after2,2)
           Income_at_ret_after2 = round(Income_at_ret_after2+((Income_at_ret_after2*Inflation2)/100),2)
           after_active_Age2 = after_active_Age2 + 1
           ssa_amt2=round(ssa_amt2+((ssa_amt2*Rate_of_SSA2)/100),2)
       df2 = df2.round(0)
       df2
       Max_Balance2 = round(df2["Retirement Balance  $"].max(),2)
       Sum_Balance2 = round(df2["Retirement Balance  $"].sum(),2)
   #Balance_at_100 = round((df.loc[df["Retirement Balance $"] == 100]),2)
       #col3.write(f' Retirement Savings :  $ {saving}')
       #col2.write(f'Total amount at the time of retirement  : {saving}' )

   #col1, col2 = st.columns(2)

       st.write(f'Maximum size of retirement Savings: {Max_Balance2}')
       st.write(f'Total dollar received: {Sum_Balance2}')

       dfa = df2.drop(columns=['Retirement Balance  $'])
       chart_data1 = pd.DataFrame(
       dfa,
       columns=['Age','Retirement Income  $'])
       st.line_chart(chart_data1)
       dfb = df2.drop(columns=['Retirement Income  $'])
       chart_data2 = pd.DataFrame(
       dfb,
       columns=['Age','Retirement Balance  $',])
       st.line_chart(chart_data2)

       def to_excel(df):
                output = BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')
                df2.to_excel(writer, index=False, sheet_name='Sheet1')
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                format1 = workbook.add_format({'num_format': '0.00'})
                worksheet.set_column('A:A', None, format1)
                writer.save()
                processed_data = output.getvalue()
                return processed_data
       df_xlsx = to_excel(df2)
       st.download_button(label='Download Table Data',
                                          data=df_xlsx ,
                                          file_name= 'Retirement income scenario2.xlsx')


if submit_btn12:
    col1, col2 = st.columns(2)
    with col1:
        st.title(' Report for Run 1  ')
        st.write(f'Name : {name}')
        st.write(f'Age : {age}')
        st.write(f'No of years for retirement : {retirement_age-age}')
        st.write(f'Inflation : {Inflation} %')
        st.write(f'Retirement Age : {retirement_age}')
        st.write(f'Active Age after retirement: {active_year}')
        st.write(f'Expected increment per year in salary:  {Expected_salary_increase} %')
        st.write(f'Interest you will get on your saving : {Interest} %')
        st.write(f'Annual saving : {Avg_sal_return} %')


        df = pd.DataFrame(columns=['Age','Scenario','Current Salary','Retirement Income $','Retirement Balance $'])
        while age < retirement_age :
            saving  = round(((Current_nest+(Current_nest * Interest)/100)+((currentsalary*Avg_sal_return)/100)),2)
            #col3.write(f'Total retirement Balance at age {age} :  $ {saving}' )
            df.loc[age, ['Retirement Balance $']] = round(saving,2)
            df.loc[age, ['Age']] = round(age,2)
            df.loc[age, ['Retirement Income $']] = round(0,2)
            df.loc[age, ['Scenario']] = round(1,0)
            df.loc[age, ['Current Salary']] = round(currentsalary,2)
            Current_nest = round(((Current_nest+(Current_nest * Interest)/100)+((currentsalary*Avg_sal_return)/100)),2)
            currentsalary = round(currentsalary+((currentsalary*Expected_salary_increase)/100),2)
            age = age + 1

            #col1.write(f'Amount you will get at age (active years)  :  $ {Income_at_ret}')

        #retirement_age=retirement_age+1
        #Interest_rate_after_retirememt=4.00
        #Rate_of_SSA=1.25
        while (retirement_age) < (active_year) :
            #col3.write(f' Retirement Savings :  $ {saving}')
            saving2  = round(((Current_nest+ssa_amt+((Current_nest * Interest_rate_after_retirememt)/100))-Income_at_ret),2)
            df.loc[retirement_age, ['Retirement Balance $']] = round(saving2,2)
            df.loc[retirement_age, ['Age']] = round(retirement_age,2)
            df.loc[retirement_age, ['Retirement Income $']] = round(Income_at_ret,2)
            df.loc[retirement_age, ['Scenario']] = round(1,0)
            df.loc[retirement_age, ['Current Salary']] = round(0,2)
            #col1.write(f'Amount you will get at age {retirement_age}  :  $ {Income_at_ret}')
            #col2.write(f' Total Retirement Balance at age {retirement_age}:  $ {saving2}')
            Current_nest = round(((Current_nest+ssa_amt+((Current_nest * Interest_rate_after_retirememt)/100))-Income_at_ret),2)
            retirement_age = retirement_age + 1
            Income_at_ret = round(Income_at_ret+((Income_at_ret*Inflation)/100),2)
            ssa_amt=round(ssa_amt+((ssa_amt*Rate_of_SSA)/100),2)
        #col2.write(f'Amount you will get at age {active_year}  :  $ {Income_at_ret_after}')
        #after_active_Age = (active_year-1)
        after_active_Age = active_year
        while (after_active_Age) < 101 :

            saving3  = round((Current_nest+ssa_amt+(Current_nest * Interest_rate_after_retirememt)/100)-Income_at_ret_after,2)
            df.loc[after_active_Age, ['Retirement Balance $']] = round(saving3,2)
            df.loc[after_active_Age, ['Age']] = round(after_active_Age,2)
            df.loc[after_active_Age, ['Retirement Income $']] = round(Income_at_ret_after,2)
            df.loc[after_active_Age, ['Scenario']] = round(1,0)
            df.loc[after_active_Age, ['Current Salary']] = round(0,2)
            #col1.write(f'Amount you will get at age {after_active_Age}  :  $ {Income_at_ret_after}')
            #col2.write(f' Total Retirement Balance at age {after_active_Age}:  $ {saving3}')
            Current_nest = round((Current_nest+ssa_amt+(Current_nest * Interest_rate_after_retirememt)/100)-Income_at_ret_after,2)
            Income_at_ret_after = round(Income_at_ret_after+((Income_at_ret_after*Inflation)/100),2)
            after_active_Age = after_active_Age + 1
            ssa_amt=round(ssa_amt+((ssa_amt*Rate_of_SSA)/100),2)
        df = df.round(0)
        df
        Max_Balance1 = round(df["Retirement Balance $"].max(),2)
        Sum_Balance1 = round(df["Retirement Balance $"].sum(),2)
        st.write(f'Maximum size of retirement Savings: {Max_Balance1}')
        st.write(f'Total dollar received: {Sum_Balance1}')

        dfa = df.drop(columns=['Retirement Balance $'])
        chart_data1 = pd.DataFrame(
        dfa,
        columns=['Age','Retirement Income $'])
        st.line_chart(chart_data1)
        dfb = df.drop(columns=['Retirement Income $'])
        chart_data2 = pd.DataFrame(
        dfb,
        columns=['Age','Retirement Balance $',])
        st.line_chart(chart_data2)



    with col2:
        st.title('Report for Run 2')
        #col1, col2 = st.columns(2)
        st.write(f'Name : {name2}')
        st.write(f'Age : {age2}')
        st.write(f'No of years for retirement : {retirement_age2-age2}')
        #col3.write(f'sex : {sex2}')
        st.write(f'Inflation : {Inflation2} %')

        #col1.write(f'Annual Salary :  $ {currentsalary}')
        #col1.write(f'Current Saving :  $ {round((Current_nest+((Current_nest * Interest)/100)+((currentsalary*Avg_sal_return)/100)),0)}')
        st.write(f'Retirement Age : {retirement_age2}')
        st.write(f'Active Age after retirement: {active_year2}')
        #col2.write(f'Years left for retirement : {No_of_year_retire}')
        st.write(f'Expected increment per year in salary:  {Expected_salary_increase2} %')
        st.write(f'Interest you will get on your saving : {Interest2} %')
        st.write(f'Annual saving : {Avg_sal_return2} %')


        df2 = pd.DataFrame(columns=['Age','Scenario','Current Salary','Retirement Income $','Retirement Balance $'])
        while age2 < retirement_age2 :
            saving2  = round(((Current_nest2+(Current_nest2 * Interest2)/100)+((currentsalary2*Avg_sal_return2)/100)),2)
            #col3.write(f'Total retirement Balance at age {age} :  $ {saving}' )
            df2.loc[age2, ['Retirement Balance $']] = round(saving2,2)
            df2.loc[age2, ['Age']] = round(age2,2)
            df2.loc[age2, ['Retirement Income $']] = round(0,2)
            df2.loc[age2, ['Scenario']] = round(2,0)
            df2.loc[age2, ['Current Salary']] = round(currentsalary2,0)
            Current_nest2 = round(((Current_nest2+(Current_nest2 * Interest2)/100)+((currentsalary2*Avg_sal_return2)/100)),2)
            currentsalary2 = round(currentsalary2+((currentsalary2*Expected_salary_increase2)/100),2)
            age2 = age2 + 1

            #col1.write(f'Amount you will get at age (active years)  :  $ {Income_at_ret}')

        #retirement_age=retirement_age+1
        #Interest_rate_after_retirememt2=4.00
        #Rate_of_SSA2=1.25
        while (retirement_age2) < (active_year2) :
            #col3.write(f' Retirement Savings :  $ {saving}')
            saving2  = round(((Current_nest2+ssa_amt2+((Current_nest2 * Interest_rate_after_retirememt2)/100))-Income_at_ret2),2)
            df2.loc[retirement_age2, ['Retirement Balance $']] = round(saving2,2)
            df2.loc[retirement_age2, ['Age']] = round(retirement_age2,2)
            df2.loc[retirement_age2, ['Retirement Income $']] = round(Income_at_ret2,2)
            df2.loc[retirement_age2, ['Scenario']] = round(2,0)
            df2.loc[retirement_age2, ['Current Salary']] = round(0,2)
            #col1.write(f'Amount you will get at age {retirement_age}  :  $ {Income_at_ret}')
            #col2.write(f' Total Retirement Balance at age {retirement_age}:  $ {saving2}')
            Current_nest2 = round(((Current_nest2+ssa_amt2+((Current_nest2 * Interest_rate_after_retirememt2)/100))-Income_at_ret2),2)
            retirement_age2 = retirement_age2 + 1
            Income_at_ret2 = round(Income_at_ret2+((Income_at_ret2*Inflation2)/100),2)
            ssa_amt2=round(ssa_amt2+((ssa_amt2*Rate_of_SSA2)/100),2)
        #col2.write(f'Amount you will get at age {active_year}  :  $ {Income_at_ret_after}')
        #after_active_Age = (active_year-1)
        after_active_Age2 = active_year2
        while (after_active_Age2) < 101 :

            saving3  = round((Current_nest2+ssa_amt2+(Current_nest2 * Interest_rate_after_retirememt2)/100)-Income_at_ret_after2,2)
            df2.loc[after_active_Age2, ['Retirement Balance $']] = round(saving3,2)
            df2.loc[after_active_Age2, ['Age']] = round(after_active_Age2,2)
            df2.loc[after_active_Age2, ['Retirement Income $']] = round(Income_at_ret_after2,2)
            df2.loc[after_active_Age2, ['Scenario']] = round(2,0)
            df2.loc[after_active_Age2, ['Current Salary']] = round(0,2)
            #col1.write(f'Amount you will get at age {after_active_Age}  :  $ {Income_at_ret_after}')
            #col2.write(f' Total Retirement Balance at age {after_active_Age}:  $ {saving3}')
            Current_nest2 = round((Current_nest2+ssa_amt2+(Current_nest2 * Interest_rate_after_retirememt2)/100)-Income_at_ret_after2,2)
            Income_at_ret_after2 = round(Income_at_ret_after2+((Income_at_ret_after2*Inflation2)/100),2)
            after_active_Age2 = after_active_Age2 + 1
            ssa_amt2=round(ssa_amt2+((ssa_amt2*Rate_of_SSA2)/100),2)
        df2 = df2.round(0)
        df2
        #Max_Balance2= round(df["Retirement Balance 1 $"].max(),2)
        #Sum_Balance2 = round(df["Retirement Balance 1 $"].sum(),2)
        Max_Balance2 = round(df2["Retirement Balance $"].max(),2)
        Sum_Balance2 = round(df2["Retirement Balance $"].sum(),2)
        st.write(f'Maximum size of retirement Savings: {Max_Balance2}')
        st.write(f'Total dollar received: {Sum_Balance2}')


        dfa = df2.drop(columns=['Retirement Balance $','Current Salary'])
        chart_data1 = pd.DataFrame(
        dfa,
        columns=['Age','Retirement Income $'])
        st.line_chart(chart_data1)
        dfb = df2.drop(columns=['Retirement Income $'])
        chart_data2 = pd.DataFrame(
        dfb,
        columns=['Age','Retirement Balance $',])
        st.line_chart(chart_data2)

    frames = [df, df2]
    df3 = pd.concat(frames)

    def to_excel(df3):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df3.to_excel(writer, index=False, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        format1 = workbook.add_format({'num_format': '0.00'})
        worksheet.set_column('A:A', None, format1)
        writer.save()
        processed_data = output.getvalue()
        return processed_data
    df_xlsx = to_excel(df3)
    st.download_button(label='Download Table Data',
                                    data=df_xlsx ,
                                    file_name= 'Retirement incomei scenario(1 and 2).xlsx')
