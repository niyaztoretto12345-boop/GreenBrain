import streamlit as st
import random
import datetime

# Page setup
st.set_page_config(page_title="🌱 GreenBrain", page_icon="🌱", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🌱 GreenBrain – AI Energy-Saving Assistant 🌱</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Helping you save energy every day with smart AI tips and fun facts!</p>", unsafe_allow_html=True)

# Initialize energy score
if 'score' not in st.session_state:
    st.session_state.score = 100

# Tips, facts, solutions
tips = [
    "Turn off the lights when leaving a room.",
    "Unplug chargers when not in use to save standby energy.",
    "Use natural sunlight instead of lamps during the day.",
    "Set your AC to 24°C to save electricity while staying cool.",
    "Use energy-efficient LED bulbs instead of regular bulbs.",
    "Close curtains in hot weather to reduce AC use.",
    "Switch off your computer or TV when you’re done — not just standby mode.",
    "Run full loads in your washing machine or dishwasher to save energy.",
    "Use a fan instead of AC when possible.",
    "Cook with lids on pots to save energy.",
    "Replace old appliances with energy-efficient ones when possible."
]

facts = [
    "Worldwide, households waste up to 30% of energy due to inefficient use.",
    "In the UAE, lighting accounts for around 25% of residential electricity use.",
    "LED bulbs use up to 80% less energy than traditional bulbs.",
    "Using natural ventilation can save up to 50% of AC energy in hot climates.",
    "Turning off devices instead of leaving them on standby can save hundreds of dirhams per year in the UAE.",
]

solutions = [
    "Set timers or smart plugs to switch off devices automatically.",
    "Use curtains, blinds, or reflective window films to reduce heat.",
    "Organize your daily routine to reduce electricity peaks.",
    "Educate your family/friends about small changes that save energy.",
]

# Buttons layout
col1, col2 = st.columns(2)

with col1:
    if st.button("💡 Get Advice"):
        current_hour = datetime.datetime.now().hour
        if 6 <= current_hour <= 17:
            tip = "It's daytime — try using natural light instead of lamps!"
        else:
            tip = random.choice(tips)
        st.session_state.score -= random.randint(3, 8)
        st.success(f"{tip}\n\n📊 Daily Energy Score: {st.session_state.score}/100")

with col2:
    if st.button("🌍 Fun Fact"):
        fact = random.choice(facts)
        st.info(f"Fun Fact: {fact}")

col3, col4 = st.columns(2)

with col3:
    if st.button("✅ Quick Solution"):
        solution = random.choice(solutions)
        st.warning(f"Quick Solution: {solution}")

with col4:
    if st.button("📊 Show Daily Energy Score"):
        st.metric("Daily Energy Score", st.session_state.score)
