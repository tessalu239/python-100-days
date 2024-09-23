travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
#print lille
print(travel_log["France"][1])

#print "D"
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

#print Stuttgart
travel_log2 = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log2["Germany"]["cities_visited"][2])