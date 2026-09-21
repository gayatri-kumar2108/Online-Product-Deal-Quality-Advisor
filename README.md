# Online Product Deal Quality Advisor

## About the Project

This project is an AI-based application that checks the quality of an online product deal.

The user enters a deal in normal language, for example:

"I found a phone for 30000 rupees with 20% discount and 4.5 star rating."

The application extracts the price, discount, and rating and then gives a Deal Quality Score.

---

## How It Works

1. User enters the product deal.
2. Google Gemini understands the sentence.
3. LangChain extracts:
   - Price
   - Discount
   - Rating
4. Fuzzy Logic evaluates the deal.
5. The system gives a score and deal category.

---

## AI Used

- Google Gemini 3.6 Flash
- LangChain

Gemini is used to understand the user's sentence and extract the required information.

---

## Fuzzy Logic

The fuzzy system uses:

**Price**
- Low
- Medium
- High

**Discount**
- Low
- Medium
- High

**Rating**
- Poor
- Average
- Excellent

The final result is:

- Poor Deal
- Fair Deal
- Good Deal
- Excellent Deal

The system uses fuzzification, fuzzy rules, and defuzzification to calculate the final score.

---

## Technologies Used

- Python
- LangChain
- Google Gemini
- scikit-fuzzy
- Streamlit

---
## Project Files

```text
app.py             → Streamlit web application
main.py            → Runs the complete system
llm_parser.py      → Extracts deal details using Gemini
fuzzy_logic.py     → Performs fuzzy logic analysis
README.md          → Project information

## Used liabaries
streamlit
langchain
langchain-google-genai
scikit-fuzzy
numpy


