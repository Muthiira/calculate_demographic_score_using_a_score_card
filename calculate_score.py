import json

# Import scorecard data from scorecard.json
with open('scorecard.json', 'r') as scorecard_file:
    scorecard = json.load(scorecard_file)

# Import borrower data from borrower_data.json
with open('borrower_data.json', 'r') as borrower_data_file:
    borrower_data = json.load(borrower_data_file)


def calculate_demographic_score(borrower_data, scorecard):
    # Initialize the total score to 0
    total_score = 0

    # Iterate through each attribute in the scorecard settings
    for attribute, settings in scorecard['setting'].items():
        # Extract attribute details from the scorecard settings
        attribute_type = settings['type']
        attribute_weight = int(settings['weight'])
        attribute_attributes = settings['attributes']

        # Get the value of the attribute from borrower_data or None if not present
        attribute_value = borrower_data.get(attribute, None)

        if attribute_value is not None:
            if attribute_type == 'rules':
                # Initialize the rule score to 0
                rule_score = 0

                # Iterate through the rules for this attribute
                for rule in attribute_attributes[0]['rule']:
                    condition = rule['condition']

                    # Replace "value" in the condition with the actual attribute value
                    condition = condition.replace("value", "attribute_value")

                    # Evaluate the condition and update the rule score if it's True
                    if eval(condition, {'attribute_value': attribute_value}):
                        rule_score = int(rule['score'])
                        break

                # Add the minimum of rule_score and maximum_score to the total score
                total_score += min(rule_score, int(settings['maximum_score']))

            elif attribute_type == 'string':
                # Iterate through attribute attributes (key-value pairs)
                for attr in attribute_attributes:
                    if attr['key'] == attribute_value:
                        # Add the score associated with the attribute value to the total score
                        total_score += int(attr['score'])
                        break

    # Return the calculated total score
    return total_score

demographic_score = calculate_demographic_score(borrower_data, scorecard)

print(f"Demographic Score: {demographic_score}")