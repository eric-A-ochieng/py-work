# program to convert temperature 

class Temperature:
    def convert_fahrenheit(self):
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")

    def convert_celsius(self):
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")


temperature_converter = Temperature()

temperature_converter.convert_fahrenheit()

temperature_converter.convert_celsius()

