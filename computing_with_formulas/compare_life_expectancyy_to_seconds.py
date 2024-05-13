# CDC's Life Expectancy Data for a new born is 76.4 years
LifeExp = 76.4
# 1 Billion Seconds in years 
b= 1000000000 / (365.26 * 24 * 60 * 60)
if LifeExp > b:
  print(f'1 billion seconds is {b} years and the Life expectancy is greater than this.')
