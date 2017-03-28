import re
f = open("cipher.txt","r")
s = f.read()
arr = s.split(",")
print(arr)
arr[-1]="73"
print(79^103)
print(len(arr))
pattern = re.compile(" the ")
for index in range(0,len(arr)):
    arr[index]=int(arr[index])
for firstLetter in xrange(97,123):
    print firstLetter
    for secondLetter in xrange(97,123):
        for thirdLetter in xrange(97,123):
            code = chr(firstLetter) + chr(secondLetter) + chr(thirdLetter)
            decoded=""
            count=0
            for num in range(0,len(arr)-2,3):
                decoded+=chr(arr[num]^ord(code[0]))
                decoded+=chr(arr[num+1]^ord(code[1]))
                decoded+=chr(arr[num+2]^ord(code[2]))
            decoded+=chr(arr[num+3]^ord(code[0]))
            if(re.search(pattern,decoded)):
                answer=decoded
                answerCode=code
                print decoded
                print "code: " + code
byteCount=0
for letter in answer:
    print(ord(letter))
    byteCount+=ord(letter)
print byteCount

arr2=[1,2,3,4,5,6,7,8,9,10,11,]
for index in range(0,len(arr2)-3,3):
    print(arr2[index])
    print(arr2[index+1])
    print(arr2[index+2])
