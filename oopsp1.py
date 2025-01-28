class findcity:
    def __init__(self,city,state):
        self.city=city
        self.state=state
    def displayit(self):
        print(f"The city {self.city} is in {self.state} state")

city1=findcity("Hyderabad","Telangana")
# city2=findcity("Bangalore","Karnataka")
# city3=findcity("Amaravathi","Andhra Pradesh")
# city1.displayit()
# city2.displayit()
# city3.displayit()
print(city1.city)