def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(String):
    if String=="Charlotte":
        return 183
    elif String=="Tampa":
        return 220
    elif String=="Pittsburgh":
        return 222
    elif String == "Los Angeles":
        return 475

def rental_car_cost(days):
    car_cost = 40*days
    if days >=7:
        return car_cost-50
    elif days>=3:
        return car_cost-20
    else:
        return car_cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)
