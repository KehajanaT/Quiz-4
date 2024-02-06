from dataclasses import dataclass

@dataclass
class Candy:
    sweet:str
    sour:str
    ordernum:int

    def sentence(self) -> str:
        return f"{self.sweet} = 5.00  {self.sour} = 3.00  Order Number = {self.ordernum } "


def main():
    candy = [
        Candy("skittles", "warheads", 1),
        Candy("gummybears", "sourpunch", 2)
    ]
    
    price1 =  candy[0].sentence()
    price2 =  candy[1].sentence()
    print(candy[0])
    print(candy[1])
    print(price1)
    print(price2)

if __name__=="__main__":
    main()    