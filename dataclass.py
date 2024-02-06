from dataclasses import dataclass

@dataclass
class Candy:
    sweet:str
    sour:str
    ordernum:int

def main():
    candy = [
        Candy("skittles", "warheads", 1),
        Candy("gummybears", "sourpunch", 2)
    ]
    
    print(candy[0])
    print(candy[1])

if __name__=="__main__":
    main()

