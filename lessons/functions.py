from datetime import datetime

def show_date() -> None:
    print("==========functions==========")
    print("this is current time: ")
    print(datetime.now())
    

def greet(name: str) -> None:
    print("==========functions==========")
    print(f"Hello, {name}")