import json

scorecard_json = {
    "id": 30536,
    "version_id": 0,
    "decision_model_id": 4169,
    "decision_type": "scoring",
    "setting": {
        "age": {
            "type": "rules",
            "weight": "7",
            "attributes": [
                {
                    "rule": [
                        { "condition": "value < 20", "score": 0 },
                        { "condition": "value < 30", "score": 6 },
                        { "condition": "value < 40", "score": 10 },
                        { "condition": "value < 50", "score": 8 },
                        { "condition": "value < 60", "score": 4 },
                        { "condition": True, "score": 0 }
                    ]
                }
            ],
            "description": "Age",
            "maximum_score": "10"
        },
        "gender": {
            "type": "string",
            "weight": "10",
            "attributes": [
                {
                    "key": "female",
                    "score": 10
                },
                {
                    "key": "male",
                    "score": 5
                }
            ],
            "description": "Gender",
            "maximum_score": "10"
        },
        "location": {
            "type": "string",
            "weight": "5",
            "attributes": [
                {
                    "key": "City",
                    "score": 5
                },
                {
                    "key": "Town",
                    "score": 3
                },
                {
                    "key": "Village",
                    "score": 2
                }
            ],
            "description": "Location",
            "maximum_score": "10"
        },
        "customer_tier": {
            "type": "string",
            "weight": "5",
            "attributes": [
                {
                    "key": "Tier 3",
                    "score": "10"
                },
                {
                    "key": "Tier 2",
                    "score": "6"
                },
                {
                    "key": "Tier 1",
                    "score": "2"
                }
            ],
            "description": "Customer Tier",
            "maximum_score": "10"
        },
        "marital_status": {
            "type": "string",
            "weight": "5",
            "attributes": [
                {
                    "key": "Married",
                    "score": "10"
                },
                {
                    "key": "Single",
                    "score": "6"
                },
                {
                    "key": "Separated",
                    "score": "4"
                },
                {
                    "key": "Widowed",
                    "score": "7"
                },
                {
                    "key": "Divorced",
                    "score": "4"
                }
            ],
            "description": "Marital Status",
            "maximum_score": "10"
        },
        "employer_category": {
            "type": "string",
            "weight": "5",
            "attributes": [
                {
                    "key": "National Govt: Public",
                    "score": "10"
                },
                {
                    "key": "Local Govt: Public",
                    "score": "5"
                },
                {
                    "key": "Private Company",
                    "score": "8"
                },
                {
                    "key": "Enterprise",
                    "score": "7"
                },
                {
                    "key": "Non-profit",
                    "score": "6"
                }
            ],
            "description": "Employer Category",
            "maximum_score": "10"
        },
        "employment_status": {
            "type": "string",
            "weight": "10",
            "attributes": [
                {
                    "key": "Employed",
                    "score": "10"
                },
                {
                    "key": "Self-employed",
                    "score": "7"
                },
                {
                    "key": "Unemployed",
                    "score": "0"
                }
            ],
            "description": "Employment Status",
            "maximum_score": "10"
        },
        "type_of_residence": {
            "type": "string",
            "weight": "5",
            "attributes": [
                {
                    "key": "Own House",
                    "score": "10"
                },
                {
                    "key": "Rented Apartment",
                    "score": "7"
                },
                {
                    "key": "Parents Apartment",
                    "score": "5"
                }
            ],
            "description": "Type of Residence",
            "maximum_score": "10"
        },
        "monthly_net_income": {
            "type": "string",
            "weight": "10",
            "attributes": [
                {
                    "key": "Above 1,000,000",
                    "score": "10"
                },
                {
                    "key": "700,000 - 999,999",
                    "score": "9"
                },
                {
                    "key": "400,000 - 699,999",
                    "score": "8"
                },
                {
                    "key": "200,000 - 399,999",
                    "score": "7"
                },
                {
                    "key": "100,000 - 199,999",
                    "score": "5"
                },
                {
                    "key": "55,000 - 99,999",
                    "score": "3"
                },
                {
                    "key": "10,000 - 54,999",
                    "score": "2"
                }
            ],
            "description": "Monthly Net Income",
            "maximum_score": "10"
        },
        "no_of_dependent": {
            "type": "string",
            "weight": "8",
            "attributes": [
                {
                    "key": "0",
                    "score": "5"
                },
                {
                    "key": "1",
                    "score": "8"
                },
                {
                    "key": "2",
                    "score": "10"
                },
                {
                    "key": "3 or more",
                    "score": "5"
                }
            ],
            "description": "Number of Dependents",
            "maximum_score": "10"
        },
        "sector_of_employment": {
            "type": "string",
            "weight": "5",
            "attributes": [
                {
                    "key": "Agriculture",
                    "score": "6"
                },
                {
                    "key": "Banking",
                    "score": "7"
                },
                {
                    "key": "Education",
                    "score": "5"
                },
                {
                    "key": "Healthcare",
                    "score": "6"
                },
                {
                    "key": "Hospitality and Events",
                    "score": "0"
                },
                {
                    "key": "Information Technology",
                    "score": "5"
                },
                {
                    "key": "Law",
                    "score": "10"
                },
                {
                    "key": "Manufacturing and Construction",
                    "score": "4"
                },
                {
                    "key": "Media & Entertainment",
                    "score": "7"
                },
                {
                    "key": "NGO",
                    "score": "0"
                },
                {
                    "key": "Oil and Gas",
                    "score": "6"
                },
                {
                    "key": "Other Financial",
                    "score": "6"
                },
                {
                    "key": "Others",
                    "score": "4"
                },
                {
                    "key": "Public services and administration",
                    "score": "5"
                },
                {
                    "key": "Telecoms",
                    "score": "9"
                },
                {
                    "key": "Tourism & Hospitality",
                    "score": "3"
                },
                {
                    "key": "Transportation & Logistics",
                    "score": "0"
                },
                {
                    "key": "Wholesale and Retail Trade",
                    "score": "6"
                }
            ],
            "description": "Sector of Employment",
            "maximum_score": "10"
        },
        "educational_attainment": {
            "type": "string",
            "weight": "5",
            "attributes": [
                {
                    "key": "Msc and above",
                    "score": "10"
                },
                {
                    "key": "Bsc,HND and other equivalent",
                    "score": "8"
                },
                {
                    "key": "Diploma",
                    "score": "5"
                },
                {
                    "key": "School cert",
                    "score": "5"
                },
                {
                    "key": "Vocation/Technical",
                    "score": "4"
                },
                {
                    "key": "Apprenticeship and Crafts",
                    "score": "0"
                }
            ],
            "description": "Educational Attainment",
            "maximum_score": "10"
        },
        "time_with_current_employer": {
            "type": "rules",
            "weight": "5",
            "attributes": [
                {
                    "rule": [
						{ "condition": "time_with_current_employer == 0", "score": 0 },
						{ "condition": "time_with_current_employer <= 2", "score": 6 },
						{ "condition": "time_with_current_employer <= 5", "score": 8 },
						{ "condition": "time_with_current_employer <= 6", "score": 10 },
						{ "condition": "time_with_current_employer <= 10", "score": 10 },
						{ "condition": "time_with_current_employer < 100", "score": 10 },
						{ "condition": True, "score": 0 }
					]
                }
            ],
            "description": "Time with Current Employer",
            "maximum_score": "10"
        }
    }
}

# Parse the scorecard JSON into a Python dictionary
scorecard = json.loads(json.dumps(scorecard_json))

def calculate_demographic_score(borrower_data, scorecard):
    total_score = 0

    for attribute, settings in scorecard['setting'].items():
        attribute_type = settings['type']
        attribute_weight = int(settings['weight'])
        attribute_attributes = settings['attributes']

        # Retrieve the value of the attribute from borrower_data
        attribute_value = borrower_data.get(attribute, None)

        if attribute_value is not None:
            if attribute_type == 'rules':
                # Iterate through the rules and apply them
                for rule in attribute_attributes[0]['rule']:
                    condition = rule['condition']
                    if isinstance(condition, bool):
                        if condition:
                            rule_score = int(rule['score'])
                            total_score += rule_score
                            break  # Exit loop on the first matching rule
                    else:
                        condition_operator, condition_value = condition.split(' ', 1)
                        if condition_operator == "<":
                            if attribute_value < eval(condition_value):
                                rule_score = int(rule['score'])
                                total_score += rule_score
                                break  # Exit loop on the first matching rule
                        elif condition_operator == "<=":
                            if attribute_value <= eval(condition_value):
                                rule_score = int(rule['score'])
                                total_score += rule_score
                                break  # Exit loop on the first matching rule
            elif attribute_type == 'string':
                # Match the attribute value to predefined keys and assign the score
                for attr in attribute_attributes:
                    if attr['key'] == attribute_value:
                        total_score += int(attr['score'])
                        break  # Exit loop on the first matching key

    return total_score


borrower_data = {
    "age": 40,
    "gender": "female",
    "location": "City",
    "customer_tier": "Tier 2",
    "marital_status": "Married",
    "employer_category": "Private Company",
    "employment_status": "Employed",
    "type_of_residence": "Rented Apartment",
    "monthly_net_income": "100,000 - 199,999",
    "no_of_dependent": "2",
    "sector_of_employment": "Information Technology",
    "educational_attainment": "Bsc,HND and other equivalent",
    "time_with_current_employer": 10
}

# Calculate the demographic score
demographic_score = calculate_demographic_score(borrower_data, scorecard)

print(f"Demographic Score: {demographic_score}")