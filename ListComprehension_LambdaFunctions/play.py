capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]

locations = [f"{city}, {country}" for (city, country) in zip(capitals, countries)]
print(locations)

possible_ms = [m * 0.1 for m in range(-100, 101)]
print(possible_ms)
# outputs list of -10 to 10 in increments of 0.1

# Can set coordinate variables like this
x1, y1 = (3, 4)
# Now can refer to them separately
print(x1)