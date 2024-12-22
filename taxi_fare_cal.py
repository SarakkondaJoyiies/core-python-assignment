def cal_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare +distance_fare

trips = [5, 10, 3]
fares = [cal_fare(d) for d in trips]

for i, fare in enumerate(fares, 1):
    print(f"Trip {i}: ${fare}")
print(f"Total Fare: ${sum(fares)}")
