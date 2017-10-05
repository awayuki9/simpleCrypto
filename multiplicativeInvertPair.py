r = input("input number of modulus to find multiplicative invert pairs : ")
for i in range(1,r):
    for j in range(1,r):
        if((i*j)%r==1):
            print(i,j,i*j) 
