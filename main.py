import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(
    page_title="Environmental Impact Calculator",
    page_icon="🌱"
)

st.title("🌱 Environmental Impact Calculator")
st.write("Answer the questions below to assess your environmental impact.")

score = 0

# Question 1
q1 = st.selectbox(
    "1. How do you travel to office/school?",
    [
        "Walking/Cycle",
        "Public Transport",
        "Carpool",
        "Bike",
        "Car Alone"
    ]
)

travel_scores = {
    "Walking/Cycle": 1,
    "Public Transport": 2,
    "Carpool": 3,
    "Bike": 4,
    "Car Alone": 5
}

score += travel_scores[q1]

# Question 2
q2 = st.selectbox(
    "2. Distance travelled daily?",
    [
        "< 5 km",
        "5 - 15 km",
        "15 - 30 km",
        "> 30 km"
    ]
)

distance_scores = {
    "< 5 km": 1,
    "5 - 15 km": 2,
    "15 - 30 km": 3,
    "> 30 km": 5
}

score += distance_scores[q2]

# Question 3
q3 = st.selectbox(
    "3. AC temperature at home/office?",
    [
        "24-26°C",
        "22-24°C",
        "Below 22°C"
    ]
)

score += {
    "24-26°C": 1,
    "22-24°C": 3,
    "Below 22°C": 5
}[q3]

# Question 4
q4 = st.selectbox(
    "4. Do you switch off lights/computers when not in use?",
    [
        "Always",
        "Sometimes",
        "Rarely"
    ]
)

score += {
    "Always": 1,
    "Sometimes": 3,
    "Rarely": 5
}[q4]

# Question 5
q5 = st.selectbox(
    "5. Use of disposable plastic items?",
    [
        "Never",
        "Occasionally",
        "Daily"
    ]
)

score += {
    "Never": 1,
    "Occasionally": 3,
    "Daily": 5
}[q5]

# Question 6
q6 = st.selectbox(
    "6. Do you segregate waste at home?",
    [
        "Yes",
        "Sometimes",
        "No"
    ]
)

score += {
    "Yes": 1,
    "Sometimes": 3,
    "No": 5
}[q6]

# Question 7
q7 = st.selectbox(
    "7. Do you keep tap running unnecessarily?",
    [
        "Never",
        "Sometimes",
        "Frequently"
    ]
)

score += {
    "Never": 1,
    "Sometimes": 3,
    "Frequently": 5
}[q7]

# Question 8
q8 = st.selectbox(
    "8. Printing habits at office/school?",
    [
        "Mostly Digital",
        "Limited Printing",
        "Frequent Printing"
    ]
)

score += {
    "Mostly Digital": 1,
    "Limited Printing": 3,
    "Frequent Printing": 5
}[q8]

name = st.text_input("Enter your Name")

if st.button("Calculate Result"):

    if not name:
        st.warning("Please enter your name.")
    else:

        if 8 <= score <= 15:
            category = "🌿 Green Champion"
        elif 16 <= score <= 25:
            category = "♻️ Eco Aware"
        elif 26 <= score <= 35:
            category = "⚠️ Needs Improvement"
        else:
            category = "☁️ Carbon Intensive"

        st.success(f"Total Score: {score}")
        st.subheader(category)

        response = pd.DataFrame([{
            "Timestamp": datetime.now(),
            "Name": name,
            "Travel": q1,
            "Distance": q2,
            "AC Temp": q3,
            "Switch Off Devices": q4,
            "Plastic Usage": q5,
            "Waste Segregation": q6,
            "Water Usage": q7,
            "Printing Habits": q8,
            "Score": score,
            "Category": category
        }])

        file_name = "survey_responses.csv"

        if os.path.exists(file_name):
            response.to_csv(
                file_name,
                mode="a",
                header=False,
                index=False
            )
        else:
            response.to_csv(
                file_name,
                index=False
            )

        st.info("Response saved successfully.")