print ("Application To Domestrate Industrial Programming")


def Addition(value1,value2):
     Ans=  value1 + value2
     return Ans



def main():
    print("Enter First number : ")
    no1=int(input())
    
    print("Enter Second number : ")
    no2=int(input())
    
    Sum = Addition(no1,no2)

   
    print("Addition is : ",Sum)

if __name__  == "__main__":

    main()