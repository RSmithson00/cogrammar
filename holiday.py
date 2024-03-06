#dictionary of city_flights and corresponding prices of hotels (locations) and flights (flights)
locations = {"Atlanta": 50,
             "Berlin": 60,
             "Cape Town": 70,
             "Dubrovnik": 40}

flights = {"Atlanta": 30,
           "Berlin": 45,
           "Cape Town": 55,
           "Dubrovnik": 34}

#user inputs
city_flight = input("So you want to go on holiday! Please pick your destination from this list:\n Atlanta, Berlin, Cape Town or Dubrovnik.")

num_nights = int(input("For how many nights will you be staying at a hotel?"))

rental_days = int(input("For how many days will you hire a car?"))

#hotel cost function - arg num_nights
def hotel_cost(num_nights):
    if city_flight in locations:
        destination_cost = locations.get(city_flight)
    accomm_cost = destination_cost * num_nights
    return accomm_cost

#plane cost function - arg city_flight
def plane_cost(city_flight):
    if city_flight in flights:
        aim = flights.get(city_flight)
    flight_cost = aim * 2
    return flight_cost

#car rental function - arg rental_days
def car_rental(rental_days):
    car_rental_cost = rental_days * 50
    return car_rental_cost

#assigning returned values of functions to local variables for easier print/use in holiday_cost function
a = (hotel_cost(num_nights))
b = (plane_cost(city_flight))
c = (car_rental(rental_days))

#call above functions
print(f"The cost of the hotel is £{str(a)}. \nThe cost of flights is £{str(b)}. \nThe cost of car rental is £{str(c)}.")

#holiday_cost function - 3 args, total the above. store in local variables?
def holiday_cost(accomm_cost,flight_cost,car_rental_cost):
    total_cost = a + b + c
    return total_cost

#call holiday_cost for absolute total
print(f"The total cost of your holiday is £{str((holiday_cost(hotel_cost, plane_cost, car_rental)))}.")