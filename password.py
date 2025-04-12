import streamlit as st
import re

# Page Configuration
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# Title and Description
st.title("🔐 Password Strength Checker")
st.markdown(
    """
    Check the strength of your password and receive real-time feedback along with 
    tips to improve it. A strong password helps protect your sensitive information. 🔒
    """
)

# Password Input
password = st.text_input("Enter your password", type="password", placeholder="Type your password here...")

# Password Evaluation
if password:
    length = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Strength Logic
    if all([length, has_upper, has_lower, has_digit, has_special]):
        st.success("✅ Your password is strong.")
    elif length and (has_upper or has_lower) and has_digit:
        st.warning("⚠️ Your password is moderate. Consider adding special characters and mixing upper & lower case letters.")
    else:
        st.error("❌ Your password is weak.")
        st.markdown("#### Tips to improve your password:")
        st.markdown("""
        - Use at least **8 characters**
        - Include both **uppercase** and **lowercase** letters
        - Add **numbers** (e.g. 0–9)
        - Incorporate **special characters** (e.g. `!@#$%^&*`)
        - Avoid using common words or personal info
        """)

else:
    st.info("Please enter a password above to check its strength.")
