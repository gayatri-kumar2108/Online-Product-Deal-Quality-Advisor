import streamlit as st
import os

from llm_parser import extract_deal_details
from fuzzy_logic import calculate_deal_quality


# Page settings
st.set_page_config(
    page_title="Online Deal Quality Advisor",
    page_icon="🛍️",
    layout="centered"
)


# Title
st.title("🛍️ Online Product Deal Quality Advisor")

st.write(
    "Enter a product deal in normal language and the system will "
    "analyze its quality using LangChain, Gemini and Fuzzy Logic."
)


# Input
user_text = st.text_area(
    "Enter your product deal:",
    placeholder="Example: I found a phone for 30000 rupees with 20% discount and 4.5 star rating."
)


# Analyze button
if st.button("🔍 Analyze Deal"):

    if user_text.strip() == "":
        st.warning("Please enter a product deal.")

    else:
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            st.error("GOOGLE_API_KEY is not set.")
            st.stop()

        try:
            # LangChain + Gemini extracts the details
            with st.spinner("Understanding the deal..."):
                price, discount, rating = extract_deal_details(
                    user_text,
                    api_key
                )

            # Fuzzy Logic analyzes the deal
            score, category = calculate_deal_quality(
                price,
                discount,
                rating
            )

            # Display extracted information
            st.subheader("📋 Extracted Details")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Price", f"₹{price:,.0f}")

            with col2:
                st.metric("Discount", f"{discount}%")

            with col3:
                st.metric("Rating", f"{rating}/5")

            # Display fuzzy result
            st.subheader("🎯 Deal Analysis")

            st.metric(
                "Deal Quality Score",
                f"{score}/100"
            )

            if category == "Excellent Deal":
                st.success(f"Category: {category}")

            elif category == "Good Deal":
                st.info(f"Category: {category}")

            elif category == "Fair Deal":
                st.warning(f"Category: {category}")

            else:
                st.error(f"Category: {category}")

        except Exception as e:
            st.error(f"Something went wrong: {e}")