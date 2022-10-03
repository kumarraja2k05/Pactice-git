print("Hello World!!")
arr=[5,4,8,1]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print(arr) 

var="Hello {}"
w="World"
val=var.format(w)
print(val)


set1={5,77,77,9,12,45,14}
set2={5,77,9,121,12,41,74}
print(set1.intersection(set2))

sum=sum(set1)
print(sum,sum/len(set1))

li=["Pooja","Pratima","Prerna","Alefia","Shresta"]
res=[name for name in li if name.startswith("P")]
print(res)

dic={"Raja":2,"Mehul":1,"Shankar":8,"Bhawana":4}
print(dic)
dic["Sourav"]=5
dic["Shankar"]=3
print("After changes: ",dic)

s=1,2
print(type(s),s)

per=("Raja","rajeev","sahil")
f1,_,f2=per
print(f1,f2)