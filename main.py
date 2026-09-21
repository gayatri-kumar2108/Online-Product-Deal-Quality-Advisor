import os

from llm_parser import extract_deal_details
from fuzzy_logic import calculate_deal_quality


# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("ERROR: GOOGLE_API_KEY is not set.")
    exit()


# Get user's natural language input
user_text = input("Enter your product deal: ")


# LLM extracts the information
price, discount, rating = extract_deal_details(
    user_text,
    api_key
)


# Fuzzy logic evaluates the deal
score, category = calculate_deal_quality(
    price,
    discount,
    rating
)


# Display result
print("\n========== DEAL ANALYSIS ==========")

print("Price:", price)
print("Discount:", discount, "%")
print("Rating:", rating, "/ 5")

print("\nDeal Quality Score:", score)
print("Deal Category:", category)