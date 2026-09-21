import os
import re
from langchain_google_genai import ChatGoogleGenerativeAI


def extract_deal_details(user_text, api_key):

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0,
        google_api_key=api_key
    )

    prompt = f"""
You are a product deal information extractor.

Read the user's sentence and extract:

1. Price
2. Discount percentage
3. Product rating out of 5

User sentence:
{user_text}

Return ONLY:

Price: number
Discount: number
Rating: number
"""

    response = llm.invoke(prompt)

    result = response.text

    price_match = re.search(
        r"Price:\s*(\d+(?:\.\d+)?)",
        result
    )

    discount_match = re.search(
        r"Discount:\s*(\d+(?:\.\d+)?)",
        result
    )

    rating_match = re.search(
        r"Rating:\s*(\d+(?:\.\d+)?)",
        result
    )

    price = float(price_match.group(1))
    discount = float(discount_match.group(1))
    rating = float(rating_match.group(1))

    return price, discount, rating


if __name__ == "__main__":

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("ERROR: GOOGLE_API_KEY is not set.")
        exit()

    text = input("Enter your product deal: ")

    price, discount, rating = extract_deal_details(
        text,
        api_key
    )

    print("\nExtracted Details:")
    print("Price:", price)
    print("Discount:", discount)
    print("Rating:", rating)