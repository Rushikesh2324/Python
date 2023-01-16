def displayFactors(NO):
     i=1
     print("FACTORS are : ")
    #for i in range (1,int(NO/2)+1,1):
     while(i<=int(NO/2)):


        if NO % i == 0:
            print(i)
        i=i+1   
            