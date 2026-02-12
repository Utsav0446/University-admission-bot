import streamlit as st
from src.data_loader import load_admission_data
from src.chatbot import get_response

# Page configuration
st.set_page_config(page_title="University Admissions Bot", layout="centered")

# Simple UI styling
st.markdown("""
<style>
.stTextInput>div>div>input {
    background-color: #1e1e1e;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🎓 University Admissions Bot")
st.caption("Helping students understand admission requirements easily")

# Load data
data = load_admission_data("data/admissions_data.json")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------------- CHATBOT SECTION ----------------
user_input = st.text_input("Ask your question")

if user_input:
    response = get_response(user_input, data)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", response))

# Display chat history
for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"🧑 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot:** {msg}")

# ---------------- DIVIDER ----------------
st.divider()

# ================= STEP 3 STARTS HERE =================
# Eligibility Checker Section
st.subheader("🎯 Quick Eligibility Check (MS Computer Science)")

gpa = st.number_input("Your GPA", 0.0, 4.0, step=0.1)
degree = st.selectbox(
    "Bachelor's Degree",
    ["Computer Science", "Related Field", "Other"]
)

if st.button("Check Eligibility"):
    if gpa >= 3.0 and degree != "Other":
        st.success("✅ You are eligible for MS Computer Science")
    else:
        st.error("❌ You may not meet the eligibility criteria")

# ================= STEP 3 ENDS HERE =================