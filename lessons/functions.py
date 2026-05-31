from datetime import datetime

def show_date() -> None:
    print("==========functions==========")
    print("this is current time: ")
    print(datetime.now())
    

def greet(name: str) -> None:
    print("==========functions with parameter==========")
    print(f"Hello, {name}")
    
def add(a: float, b: float) -> float:
    print("==========functions with return value==========")
    return a + b