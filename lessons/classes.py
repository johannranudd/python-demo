class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower
        
    def __str__(self) -> str:
        print("====string from class====")
        return f"brand={self.brand}, horsepower={self.horsepower}"
    
    
    def drive(self) -> None:
        print(f'{self.brand} is driving')
        
        
    def get_info(self) -> None:
        print(f"{self.brand} with {self.horsepower} horsepower")
        
# volvo: Car = Car("red", 200)
# print("======class Car======")
# print(volvo.color)
# print(volvo.horsepower)