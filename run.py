import Folder1.function1 as one
import Folder2.function2 as two
import Folder3.function3 as three


def main():
    f_one = one.add(3,4)
    f_two = two.sub(3,4)
    f_three = three.mult(3,4)
    print(f_one)
    print(f_two)
    print(f_three)

if __name__=="__main__":
    main()