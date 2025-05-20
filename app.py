import streamlit as st

# Title of the app
st.title("💰 Tip Calculator")

# Input for total bill
bill = st.number_input("What was your total bill?", min_value=0.0, format="%.2f")

# Input for tip percentage
tip = st.slider("Select a tip percentage", min_value=0, max_value=100, value=15)

# Input for number of people to split the bill
people = st.number_input("How many people will split the bill?", min_value=1, step=1)

# When the button is clicked, perform the calculation
if st.button("Calculate"):
    # Calculate tip amount and total bill with tip
    bill_with_tip = bill + ((tip / 100) * bill)
    
    # Calculate the amount each person should pay
    bill_per_person = bill_with_tip / people
    final_amount = round(bill_per_person, 2)
    
    # Display the result
    st.success(f"Each person should pay: ${final_amount}")
