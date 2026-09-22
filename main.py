import os
from llm_parser import extract_deal_details
from fuzzy_logic import calculate_deal_quality

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("ERROR: GOOGLE_API_KEY is not set.")
    exit()

user_text = input("Enter your product deal: ")

price, discount, rating = extract_deal_details(user_text, api_key)

score, category = calculate_deal_quality(
    price,
    discount,
    rating
)

print("\n========== DEAL ANALYSIS ==========")
print("Price:", price)
print("Discount:", discount, "%")
print("Rating:", rating, "/ 5")

print("\nDeal Quality Score:", score)
print("Deal Category:", category)