def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
  return (9. / 5) * celsius_temperature + 32


def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
  return (5. / 9) * (fahrenheit_temperature - 32)


if __name__ == "__main__":
  celsius_tempurature = [0, 21, 100]
  print('T_C\t\tT_C(T_F(T_C))')
  for some_celsius_tempurature in celsius_tempurature:
    converted_tempurature = convert_fahrenheit_temperature_to_celsius(convert_celsius_temperature_to_fahrenheit(some_celsius_tempurature))
    print(f'{some_celsius_tempurature}\t\t{converted_tempurature:.0f}')
