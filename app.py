# Import all necessary packeges
import streamlit as st
import plotly.express as px 
import pandas as pd


# write a function to calculate EMI
def loanCalc(P, N, R):
    """
    This Function takes principal , no.of years and
    rate of intrest of loan
    
    """
    # convert years into month and rate of intrest to %per month 
    n = N*12
    r = R/1200
    # Calculate emi
    x = (1+r)**n
    emi = P*r*x/(x-1)
    # Calculate total amount
    amt = n*emi 
    # Calculate intrest
    I = amt - P 
    # Calculate percent Intrest
    perI = (I/amt)*100
    return emi, amt, I, perI

# write the streamlit app
def application():
    # Header of the application
    st.set_page_config(page_title= "Loan calculator - Omkar")
    # Show title
    st.title("Loan calculator - Omkar Rajmane")
    # add subheading 
    st.subheader("Please provide loan detail below")
    # get principal priod  & loan of intrest
    P = st.number_input("Principal (INR) : ", min_value=0.00 , step=0.01)
    N = st.number_input("No. of years : ", min_value=0.00 , step=0.01)
    R = st.number_input("Rate of intrest (%) : ", min_value=0.00 , max_value=100.00 , step=00.1)
    # Add a button to perform application 
    btn = st.button("Calculate")
    # After button clicked
    if btn:
        emi ,amt ,I,perI=loanCalc(P,N,R)
        st.subheader("Loan detailed calculated :")
        st.write(f" **EMI** :{emi:.0f} INR ")
        st.write(f"**Intrest** : {I:.0f} INR")
        st.write(f"**Total Amount** : {amt:.0f} INR")
        st.write(f"**Percentage Intrest**  : {perI:.2f} %")
        # plot the visuals
        st.subheader("Visuals :")
        d = {"Details":["Prinicipal", "Intrest"],
             "Values":[P, I]}
        df = pd.DataFrame(d)
        fig = px.pie(data_frame=df, 
                     names="Details",
                     values="Values", 
                     color_discrete_sequence=["green", "orange"])
        st.plotly_chart(fig)

        
# Main application 
if __name__ == "__main__":
    application()