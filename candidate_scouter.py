import streamlit as st
import openai
import pandas as pd
import requests

def fetch_candidate_data(location, profession):
    """Mock function to simulate candidate discovery"""
    # Replace with actual LinkedIn/News API scraping later
    candidates = [
        {"Name": "John Smith", "Profession": "Veteran & Business Owner", "Conservative Score": 85, "Electability Score": 75},
        {"Name": "Emily Davis", "Profession": "Attorney & GOP Activist", "Conservative Score": 90, "Electability Score": 80},
        {"Name": "Michael Brown", "Profession": "Police Chief", "Conservative Score": 95, "Electability Score": 85}
    ]
    return pd.DataFrame(candidates)

def generate_outreach_message(candidate):
    """Uses GPT to create a custom outreach message"""
    prompt = f"Write a persuasive outreach message for {candidate['Name']}, a {candidate['Profession']}, encouraging them to run for office."
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are a political recruiter."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Streamlit UI
st.title("Candidate Scouter AI")
st.subheader("Find and recruit strong conservative candidates for office")

location = st.text_input("Enter a location (City, State)")
profession = st.text_input("Enter preferred professions (e.g., Business, Military, Law Enforcement)")

if st.button("Find Candidates"):
    candidate_df = fetch_candidate_data(location, profession)
    st.write("### Potential Candidates:")
    st.dataframe(candidate_df)

    for index, row in candidate_df.iterrows():
        with st.expander(f"Message for {row['Name']}"):
            message = generate_outreach_message(row)
            st.write(message)
            st.button("Copy to Clipboard", key=f"copy_{index}")
