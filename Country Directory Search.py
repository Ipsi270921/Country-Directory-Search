# Tuple containing fixed country names
countries = ("India", "USA", "Japan", "Germany", "UK", "France", "Canada")

print("===== COUNTRY SEARCH =====")

# Take input from user
country = input("Enter country name to search: ")

# Check if user input exists in tuple
if country in countries:
    print("✔ Country found in the directory!")
else:
    print("✘ Country not found in the directory.") 
