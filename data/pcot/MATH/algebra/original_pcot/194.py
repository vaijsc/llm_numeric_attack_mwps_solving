# Define the one-time equipment fees
equipment_fees = 1000  ### condition: 'equipment_fees': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the cost to produce each widget
cost_per_widget = 0.50  ### condition: 'cost_per_widget': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Define the selling price for each widget
selling_price_per_widget = 2.75  ### condition: 'selling_price_per_widget': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': True}
# Calculate the profit made per widget sold
profit_per_widget = selling_price_per_widget - cost_per_widget  ### condition: 'profit_per_widget': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Assert that the profit per widget is greater than zero to allow for profit
assert profit_per_widget > 0, "Profit per widget must be greater than zero."
# Calculate the minimum number of widgets needed to cover the equipment fees
min_widgets_needed = equipment_fees / profit_per_widget  ### condition: 'min_widgets_needed': {'type': 'float', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Since we need whole widgets, we will take the ceiling of the value
min_widgets_needed = int(min_widgets_needed) + (min_widgets_needed % 1 > 0)  ### condition: 'min_widgets_needed': {'type': 'int', '<=': None, '>=': 0, 'science_constant': False, 'direct_from_question': False}
# Print the minimum number of widgets needed to break even
print(f"Minimum number of widgets needed to sell to make a profit: {min_widgets_needed}")