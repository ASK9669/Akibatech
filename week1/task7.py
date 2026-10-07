Destination = input("Enter the destination: ")
distance = float(input("Enter the distance in kilometers: "))
Average_speed = float(input("Enter the average speed in km/h: "))
Time = distance / Average_speed

print("=" * 30)

print(f"Destination: {Destination}")
print(f"Distance: {distance} km")
print(f"Average Speed: {Average_speed} km/h")
print(f"\n Estimated Time of Travel : {Time:.2f} hours")
