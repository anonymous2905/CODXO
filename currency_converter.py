# Define a dictionary with some predefined exchange rates
exchange_rates = {
    'USD': {
        'EUR': 0.85,
        'GBP': 0.75,
        'INR': 73.50,
        'JPY': 110.50
    },
    'EUR': {
        'USD': 1.18,
        'GBP': 0.88,
        'INR': 86.50,
        'JPY': 130.00
    },
    'GBP': {
        'USD': 1.33,
        'EUR': 1.14,
        'INR': 98.50,
        'JPY': 147.00
    },
    'INR': {
        'USD': 0.014,
        'EUR': 0.012,
        'GBP': 0.010,
        'JPY': 1.50
    },
    'JPY': {
        'USD': 0.0091,
        'EUR': 0.0077,
        'GBP': 0.0068,
        'INR': 0.67
    }
}

def currency_converter():
    print("Welcome to the Currency Converter!")
    
    # Get user input
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (USD, EUR, GBP, INR, JPY): ").upper()
    to_currency = input("Enter the currency to convert to (USD, EUR, GBP, INR, JPY): ").upper()
    
    # Check if the currencies are supported
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        # Perform the conversion
        rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * rate
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Unsupported currency conversion.")
        
# Run the converter
if __name__ == "__main__":
    currency_converter()
