def main():
    print("enter Number : ")
    NO= int(input())

    i=1

    print("FACTORS are : ")
    #for i in range (1,int(NO/2)+1,1):
    while(i<=int(NO/2)):


        if NO % i == 0:
            print(i)
        i=i+1   
            


if __name__=="__main__" : 
    main()
