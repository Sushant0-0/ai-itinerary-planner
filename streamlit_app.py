import streamlit as st
from typing import List
from google.generativeai import configure, GenerativeModel

# Setup Gemini
configure(api_key="AIzaSyDLHg168oWOSyJjNO5qnxK6BopYInpgO_A")
model = GenerativeModel("gemini-2.0-flash")

def generate_itinerary(city: str, interests: List[str], days: int) -> str:
    interest_str = ", ".join(interests)
    prompt = f"""
    Create a unique {days}-day travel itinerary for {city} based on the following interests: {interest_str}.
    Each day's plan should include:
    - Morning: sightseeing or cultural visits.
    - Afternoon: adventure or food experiences.
    - Evening: nightlife or relaxation.

    Format the response clearly.
    """
    try:
        response = model.generate_content(prompt)
        return response.text if response else "⚠️ Could not generate itinerary."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

st.set_page_config(page_title="🌍 AI Travel Planner", layout="wide")
st.title("🌍 AI Travel Planner")

city = st.text_input("Enter City")
days = st.number_input("Enter Number of Days", min_value=1, step=1)
interests_input = st.text_input("Enter Interests (comma separated)")

if st.button("✨ Generate AI Itinerary ✨"):
    if city and interests_input and days:
        interests = [i.strip() for i in interests_input.split(",")]
        result = generate_itinerary(city, interests, days)
        st.markdown(f"## ✈️ {days}-Day Itinerary for {city}")
        st.markdown(result)
    else:
        st.warning("Please fill out all fields.")
