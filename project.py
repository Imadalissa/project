
# Define the data structures to store the drivers and cities
drivers = []
cities = {
    "beirut": ["jbeil"],
    "jbeil": ["beirut", "akkar"],
    "akkar": ["jbeil"],
    "saida": ["zahle"],
    "zahle": ["saida"]
}

# Function to add a new driver
# Function to add a new driver
def add_driver():
    # Validate driver's name (no spaces only)
    while True:
        name = input("Enter the driver's name: ").strip()
        if not name:
            print("You can't enter only spaces in the name.")
        else:
            break

    # Validate driver's start city (no spaces only)
    while True:
        start_city = input("Enter the driver's start city: ").strip().lower()
        if not start_city:
            print("You can't enter only spaces in the start city.")
        else:
            break

    # Check if the start city is in the database
    if start_city not in cities:
        print(f"The city '{start_city}' is not in the database.")
        while True:
            add_city = input("Do you want to add it? (y/n) ").strip().lower()
            if add_city == 'y':
                add_new_city(start_city)
                print("City added successfully.")
                break
            elif add_city == 'n':
                print("Okay, you cancelled.")
                return
            else:
                print("You can't enter any other value. Please enter 'y' or 'n'.")

    # Generate a unique driver ID
    driver_id = f"ID{len(drivers) + 1:03}"

    # Add the new driver to the list
    drivers.append({
        "id": driver_id,
        "name": name,
        "start_city": start_city
    })
    print(f"Driver {name} with ID {driver_id} added successfully.")

# Function to add a new city
def add_new_city(city):
    # Add city logic (assuming this is where you'd add it to the cities structure)
    cities[city] = []
    print(f"The city '{city}' has been added to the database.")

# Function to view all drivers
def view_all_drivers():
    if not drivers:
        print("There are no drivers in the database.")
    else:
        print("List of all drivers:")
        for driver in drivers:
            print(f"{driver['id']}, {driver['name']}, {driver['start_city']}")

# Function to check similar drivers
def check_similar_drivers():
    if not drivers:
        print("There are no drivers in the database.")
    else:
        # Group drivers by their start city
        driver_groups = {}
        for driver in drivers:
            start_city = driver['start_city']
            if start_city not in driver_groups:
                driver_groups[start_city] = []
            driver_groups[start_city].append(driver['name'])

        # Print the grouped drivers
        for city, driver_names in driver_groups.items():
            print(f"{city}: {', '.join(driver_names)}")

# Function to show all cities
def show_cities():
    if not cities:
        print("There are no cities in the database.")
    else:
        # Sort the cities in descending alphabetical order
        sorted_cities = sorted(cities.keys(), reverse=True)
        print("List of all cities:")
        for city in sorted_cities:
            print(city)

# Function to search for cities
def search_city():
    key = input("Enter a search key: ").lower().strip()
    matching_cities = [city for city in cities if key in city]
    if not matching_cities:
        print("No matching cities found.")
    else:
        print("Matching cities:")
        for city in matching_cities:
            print(city)

# Function to print neighboring cities
def print_neighboring_cities():
    city_name = input("Enter a city name: ").lower().strip()
    if city_name not in cities:
        print(f"The city '{city_name}' is not in the database.")
    else:
        neighbors = cities[city_name]
        if neighbors:
            print(f"Neighboring cities of {city_name.capitalize()}: {', '.join(neighbors)}")
        else:
            print(f"{city_name.capitalize()} has no neighboring cities listed.")

# Function to print drivers delivering to a city
def print_drivers_for_city():
    city_name = input("Enter a city name: ").lower().strip()
    
    if city_name not in cities:
        print(f"The city '{city_name}' is not in the database.")
    else:
        # Find drivers that start from the specified city
        drivers_in_city = [driver['name'] for driver in drivers if driver['start_city'] == city_name]
        
        if drivers_in_city:
            print(f"Drivers delivering to {city_name.capitalize()}:")
            for driver_name in drivers_in_city:
                print(driver_name)
        else:
            print(f"No drivers are delivering to {city_name.capitalize()}.")
# Main menu
while True:
    print("\nHello! Please enter:")
    print("1. To go to the drivers' menu")
    print("2. To go to the cities' menu")
    print("3. To exit the system")

    choice = input("Enter your choice (1-3): ").strip().replace(" ","")

    if choice == '1':
        # Drivers' menu
        while True:
            print("\nDrivers' Menu:")
            print("Enter:")
            print("1. To view all the drivers")
            print("2. To add a driver")
            print("3. To check similar drivers")
            print("4. To go back to the main menu")

            driver_choice = input("Enter your choice (1-4): ").strip().replace(" ","")

            if driver_choice == '1':
                view_all_drivers()
            elif driver_choice == '2':
                add_driver()
            elif driver_choice == '3':
                check_similar_drivers()
            elif driver_choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == '2':
        # Cities' menu
        while True:
            print("\nCities' Menu:")
            print("1. Show cities")
            print("2. Search city")
            print("3. Print neighboring cities")
            print("4. Print Drivers delivering to city")
            print("5. To go back to the main menu")

            city_choice = input("Enter your choice (1-5): ").strip().replace(" ","")

            if city_choice == '1':
                show_cities()
            elif city_choice == '2':
                search_city()
            elif city_choice == '3':
                print_neighboring_cities()
            elif city_choice == '4':
                print_drivers_for_city()
            elif city_choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")



