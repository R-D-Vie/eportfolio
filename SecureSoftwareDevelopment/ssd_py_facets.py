"""
Create a basic outline design of how to create a 
faceted information flow system in python
"""

# Step one: define a class which represents facets or security labels:
class facet:
    def __init__(self, label, private_value, public_value):
        self.label = label
        self.private_value = private_value
        self.public_value = public_value
    
    # Step two: build operations which use the facets to enforce information flow policies:
    def get_value(self):
        if self.label == "admin":
            return self.private_value
        else:
            return self.public_value
        
    def classify(self, credit_card_number):
        self.credit_card_number = credit_card_number
        self.label = "public"
        self.last_four_digits = credit_card_number[-4:]

    # continue...
