# =========== Holiday Cost Calculator ===========

# Function to display and calculate plane cost based on the chosen city
def plane_cost():
    while True:
        print("Flight Options:")
        print("1. Warsaw - £500 per flight")
        print("2. Oslo - £700 per flight")
        print("3. Berlin - £1000 per flight")

        choice = input("Choose your destination (1, 2, or 3): ")

        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid option. Please enter a valid choice.")

# Function to display and calculate car rental cost based on the type of car and number of rental days
def car_rental():
    while True:
        print("Car Rental Options:")
        print("1. Economy Car - £50 per day")
        print("2. Standard Car - £60 per day")
        print("3. Luxury Car - £80 per day")

        choice = input("Choose your car rental option (1, 2, or 3): ")

        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid option. Please enter a valid choice.")

# Function to display and calculate hotel cost based on the number of nights and room type
def hotel_cost():
    while True:
        print("Hotel Options:")
        print("1. Standard Room - £100 per night")
        print("2. Deluxe Room - £150 per night")
        print("3. Suite - £200 per night")

        choice = input("Choose your room type (1, 2, or 3): ")

        if choice in ['1', '2', '3']:
            num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
            return int(choice), num_nights
        else:
            print("Invalid option. Please enter a valid choice.")

# Function to calculate total holiday cost
def holiday_cost(hotel_choice, plane_choice, car_choice, num_nights, rental_days):
    room_prices = [100, 150, 200]
    flight_prices = [500, 700, 1000]
    car_prices = [50, 60, 80]

    hotel_total = room_prices[hotel_choice - 1] * num_nights
    plane_total = flight_prices[plane_choice - 1]
    car_total = car_prices[car_choice - 1] * rental_days

    return hotel_total, plane_total, car_total


# Get user inputs
plane_choice = plane_cost()
hotel_choice, num_nights = hotel_cost()
car_choice = car_rental()
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

# Calculate costs using the functions
hotel_total, plane_total, car_total = holiday_cost(hotel_choice, plane_choice, car_choice, num_nights, rental_days)
total_cost = hotel_total + plane_total + car_total

# Print out details about the holiday
print("\nHoliday Details:")
print(f"Flight Cost: £{plane_total}")
print(f"Car Rental Cost: £{car_total}")
print(f"Hotel Cost: £{hotel_total}")
print(f"Total Holiday Cost: £{total_cost}")
