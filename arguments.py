import argparse

def store() -> None:
    parser= argparse.ArgumentParser()
    parser.add_argument(help="Enter the quantity",dest="quantity",type=int)
    parser.add_argument(help="Enter an item",dest="item",type=str)    
    parser.add_argument(help="Enter the cost",dest="price",type=float)

    args=parser.parse_args()

    q = args.quantity
    i = args.item 
    p = args.price

    print("Item: ",i)
    print("Quantity: ",q)
    print("Price: ",p)

if __name__=='__main__': 	
     store()