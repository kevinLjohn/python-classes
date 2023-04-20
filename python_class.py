
class Best_Cokies:
    def __init__(self, type, rating, populatity):
        self.type = type
        self.rating = rating
        self.populatity = populatity

cookie1= Best_Cokies("Chocolate Chip", "10/10", "most popular cookie")
cookie2= Best_Cokies("super cookies", "9/10", "fifth most popular cookie")
cookie3= Best_Cokies("Macaroons", "8/10", "10th most popular cookie")
print(cookie1.type) 
print(cookie1.rating)
print(cookie1.populatity)
print(cookie2.type)
print(cookie2.rating)
print(cookie2.populatity)
print(cookie3.type) 
print(cookie3.rating)
print(cookie3.populatity)