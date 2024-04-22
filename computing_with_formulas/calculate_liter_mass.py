iron = 7850         # kg/m^3
air = 1.200         # kg/m^3
gasoline = .755     # g/cm^3
ice = 916.7         # Kg/m^3
human_body = 1.096  # g/cm^3
silver = 10500      # kg/m^3
platinum = 21450    # kg/m^3

# to get the mass of a liter of iron, air, gasoline, ice, human_body, silver
# you take the density of each material in kg/m^3 and multiply that by .001 to get the mass in KG. For the ones that have density in g/cm^3 mult that density by 1 to get the KG per Liter.

print(f'The mass of a liter of iron is {iron * .001:.2f} KG')
print(f'The mass of a liter of air is {air * .001:.8f} KG')
print(f'The mass of a liter of gasoline is {gasoline * 1:.3f} KG')
print(f'The mass of a liter of ice is {ice * .001:.4f} KG')
print(f'The mass of a liter of human_body is {human_body * 1:.4f} KG')      
print(f'The mass of a liter of silver is {silver * .001:.2f} KG')
print(f'The mass of a liter of platinum is {platinum * .001:.2f} KG')
