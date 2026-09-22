# 🛍️ Online Product Deal Quality Advisor

## Student Details

**Student Name:** Gayatri Kumar
**Roll Number:** 19003

---

## Project Title

**Online Product Deal Quality Advisor**

## Short Description

The **Online Product Deal Quality Advisor** is an AI-based web application that analyzes the quality of an online product deal.

The user enters a product deal in normal language, such as:

> I found a phone for 30000 rupees with 20% discount and 4.5 star rating.

The application uses **Google Gemini and LangChain** to extract the price, discount percentage, and product rating from the user's sentence. These values are then evaluated using **Fuzzy Logic** to generate a Deal Quality Score between 0 and 100 and classify the deal as Poor, Fair, Good, or Excellent.

---

## Main Features

* Accepts product deal information in natural language.
* Uses Google Gemini to understand the user's input.
* Uses LangChain for Gemini integration.
* Extracts:

  * Product price
  * Discount percentage
  * Product rating
* Uses Fuzzy Logic to evaluate the deal.
* Uses triangular membership functions.
* Applies predefined fuzzy rules.
* Generates a Deal Quality Score from 0 to 100.
* Classifies the deal as:

  * Poor Deal
  * Fair Deal
  * Good Deal
  * Excellent Deal
* Provides a simple and user-friendly Streamlit interface.

---

## IKS Connection

The project is connected to the **Indian Knowledge Systems (IKS) syllabus through the topic of Fuzzy Logic**.

The project applies concepts covered in the Fuzzy Logic portion of the syllabus, including:

* Fuzzy Sets
* Membership Functions
* Triangular Membership Functions
* Fuzzy Rules
* Fuzzy Inference System
* Defuzzification

In the project, fuzzy sets are created for **price, discount, and product rating**.

For example:

* Price → Low, Medium, High
* Discount → Low, Medium, High
* Rating → Poor, Average, Excellent
* Deal Quality → Poor, Fair, Good, Excellent

The system applies predefined fuzzy rules to these inputs and produces a numerical Deal Quality Score.

Thus, the project demonstrates the practical application of the **Fuzzy Logic concepts covered in the IKS syllabus** to an online shopping and deal evaluation problem.

---

## Technologies / Tech Stack

| Technology        | Purpose                                                   |
| ----------------- | --------------------------------------------------------- |
| **Python**        | Main programming language                                 |
| **Google Gemini** | Natural-language understanding and information extraction |
| **LangChain**     | Integration with the Gemini LLM                           |
| **scikit-fuzzy**  | Implementation of Fuzzy Logic                             |
| **NumPy**         | Numerical calculations                                    |
| **Streamlit**     | Web application interface                                 |
| **Git & GitHub**  | Version control and source-code management                |

---

## Project Workflow

```text
User enters product deal
          ↓
Google Gemini
          ↓
LangChain
          ↓
Extract Price, Discount and Rating
          ↓
Fuzzy Logic
          ↓
Fuzzy Rules and Membership Functions
          ↓
Defuzzification
          ↓
Deal Quality Score
          ↓
Deal Category
          ↓
Streamlit Output
```

---

## Fuzzy Logic Implementation

The project uses Fuzzy Logic to evaluate the quality of a product deal.

### Input Variables

**Price**

* Low
* Medium
* High

**Discount**

* Low
* Medium
* High

**Rating**

* Poor
* Average
* Excellent

### Output Variable

**Deal Quality**

* Poor
* Fair
* Good
* Excellent

The project uses **triangular membership functions** and predefined fuzzy rules.

Example:

```text
High Discount + Excellent Rating + Medium Price
                    ↓
             Excellent Deal
```

The final fuzzy output is converted into a score between **0 and 100**.

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/gayatri-kumar2108/Online-Product-Deal-Quality-Advisor.git
```

### 2. Open the Project Folder

```bash
cd Online-Product-Deal-Quality-Advisor
```

### 3. Install Required Libraries

```bash
pip install -r requirements.t
```
