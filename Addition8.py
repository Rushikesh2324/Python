print ("Application To Domestrate Industrial Programming")

import MarvallousModule



def main():
    print("Value of __name__ from main is :", __name__)
    print("Enter First number : ")
    no1=int(input())
    
    print("Enter Second number : ")
    no2=int(input())
    
    Sum = MarvallousModule.Addition(no1,no2)

   
    print("Addition is : ",Sum)

if __name__  == "__main__":

    main()