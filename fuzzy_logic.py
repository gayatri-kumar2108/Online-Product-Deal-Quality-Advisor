import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# -------------------------------
# 1. Create input variables
# -------------------------------

price = ctrl.Antecedent(np.arange(0, 100001, 1000), 'price')
discount = ctrl.Antecedent(np.arange(0, 51, 1), 'discount')
rating = ctrl.Antecedent(np.arange(0, 5.1, 0.1), 'rating')


# -------------------------------
# 2. Create output variable
# -------------------------------

deal_quality = ctrl.Consequent(
    np.arange(0, 101, 1),
    'deal_quality'
)


# -------------------------------
# 3. Membership functions
# -------------------------------

# Price
price['low'] = fuzz.trimf(
    price.universe, [0, 0, 30000]
)

price['medium'] = fuzz.trimf(
    price.universe, [20000, 50000, 70000]
)

price['high'] = fuzz.trimf(
    price.universe, [60000, 100000, 100000]
)


# Discount
discount['low'] = fuzz.trimf(
    discount.universe, [0, 0, 15]
)

discount['medium'] = fuzz.trimf(
    discount.universe, [10, 25, 40]
)

discount['high'] = fuzz.trimf(
    discount.universe, [30, 50, 50]
)


# Rating
rating['poor'] = fuzz.trimf(
    rating.universe, [0, 0, 2.5]
)

rating['average'] = fuzz.trimf(
    rating.universe, [2, 3, 4]
)

rating['excellent'] = fuzz.trimf(
    rating.universe, [3.5, 5, 5]
)


# Deal Quality
deal_quality['poor'] = fuzz.trimf(
    deal_quality.universe, [0, 0, 30]
)

deal_quality['fair'] = fuzz.trimf(
    deal_quality.universe, [20, 40, 60]
)

deal_quality['good'] = fuzz.trimf(
    deal_quality.universe, [50, 70, 85]
)

deal_quality['excellent'] = fuzz.trimf(
    deal_quality.universe, [75, 100, 100]
)


# -------------------------------
# 4. Fuzzy rules
# -------------------------------

rule1 = ctrl.Rule(
    discount['high'] &
    rating['excellent'] &
    price['medium'],
    deal_quality['excellent']
)

rule2 = ctrl.Rule(
    discount['high'] &
    rating['excellent'] &
    price['low'],
    deal_quality['excellent']
)

rule3 = ctrl.Rule(
    discount['medium'] &
    rating['excellent'] &
    price['medium'],
    deal_quality['good']
)

rule4 = ctrl.Rule(
    discount['medium'] &
    rating['excellent'] &
    price['low'],
    deal_quality['good']
)

rule5 = ctrl.Rule(
    discount['high'] &
    rating['average'],
    deal_quality['good']
)

rule6 = ctrl.Rule(
    discount['medium'] &
    rating['average'],
    deal_quality['fair']
)

rule7 = ctrl.Rule(
    discount['low'] &
    rating['average'],
    deal_quality['fair']
)

rule8 = ctrl.Rule(
    discount['low'] &
    rating['poor'],
    deal_quality['poor']
)

rule9 = ctrl.Rule(
    price['high'] &
    discount['low'],
    deal_quality['poor']
)

rule10 = ctrl.Rule(
    rating['excellent'] &
    discount['low'],
    deal_quality['fair']
)


# -------------------------------
# 5. Create fuzzy control system
# -------------------------------

deal_control = ctrl.ControlSystem([
    rule1,
    rule2,
    rule3,
    rule4,
    rule5,
    rule6,
    rule7,
    rule8,
    rule9,
    rule10
])


# -------------------------------
# 6. Calculate deal quality
# -------------------------------

def calculate_deal_quality(price_value, discount_value, rating_value):

    simulation = ctrl.ControlSystemSimulation(deal_control)

    simulation.input['price'] = price_value
    simulation.input['discount'] = discount_value
    simulation.input['rating'] = rating_value

    simulation.compute()

    score = simulation.output['deal_quality']

    if score < 40:
        category = "Poor Deal"

    elif score < 60:
        category = "Fair Deal"

    elif score < 80:
        category = "Good Deal"

    else:
        category = "Excellent Deal"

    return round(score, 2), category


# -------------------------------
# 7. Test the fuzzy system
# -------------------------------

if __name__ == "__main__":

    score, category = calculate_deal_quality(
        30000,
        20,
        4.5
    )

    print("Deal Quality Score:", score)
    print("Deal Category:", category)