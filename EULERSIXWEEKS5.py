import time

count=0
booleans = [0]*6
numbouncy=0
digits=[num for num in xrange(0,10)]
print digits

numbouncy21780=0

start=time.clock()
for num in digits[1:]:
    for num2 in digits:
        print num2
        if(num2>num):
            booleans[0]=1
        elif(num2<num):
            booleans[0]=-1
        else:
            booleans[0]=0
        for num3 in digits:
            booleans[2]=0
            booleans[3]=0
            booleans[4]=0
            booleans[5]=0
            if(num3>num2):
                booleans[1]=1
            elif(num3<num2):
                booleans[1]=-1
            else:
                booleans[1]=0
            if(booleans.count(-1)>=1):
                if(booleans.count(1)>=1):
                    numbouncy+=1
            for num4 in digits:
                booleans[3]=0
                booleans[4]=0
                booleans[5]=0
                if(num4>num3):
                    booleans[2]=1
                elif(num4<num3):
                    booleans[2]=-1
                else:
                    booleans[2]=0
                if(booleans.count(-1)>=1):
                    if(booleans.count(1)>=1):
                        numbouncy+=1
                for num5 in digits:
                    booleans[4]=0
                    booleans[5]=0
                    if(num5>num4):
                        booleans[3]=1
                    elif(num5<num4):
                        booleans[3]=-1
                    else:
                        booleans[3]=0
                    if(booleans.count(-1)>=1):
                        if(booleans.count(1)>=1):
                            numbouncy+=1      
                                #numbouncy21780=numbouncy
                                #print "numbouncy at 21780: " + str(numbouncy)
                    for num6 in digits:
                        booleans[5]=0
                        if(num6>num5):
                            booleans[4]=1
                        elif(num6<num5):
                            booleans[4]=-1
                        else:
                            booleans[4]=0
                        if(booleans.count(-1)>=1):
                            if(booleans.count(1)>=1):
                                #if(int(str(num)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6))<number):
                                numbouncy+=1
                        for num7 in digits:
                            if(num7>num6):
                                booleans[5]=1
                            elif(num7<num6):
                                booleans[5]=-1
                            else:
                                booleans[5]=0
                            if(booleans.count(-1)>=1):
                                if(booleans.count(1)>=1):
                                    if(num==1 and num2<6):
                                        if(num2==5 and num3==9):
                                            count+=1
                                        elif(num2==5 and num3==8 and num4>6):
                                            count+=1
                                        #elif(num2==5 and num3==8 and num4==7 and num5>0):
                                         #   count+=1
                                        #elif(num2==5 and num3==8 and num4==7 and num5==1 and num6>4):
                                         #   count+=1
                                        else:
                                            numbouncy+=1
                                     #   print("num: "  + str(num)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)+str(num7))
                                      #  numbouncy+=1
stop=time.clock()

print numbouncy
print count
print("ratio: " + str(float(numbouncy+1)/1587000.0))
print(float(numbouncy))
print stop-start


    
                                
                        
