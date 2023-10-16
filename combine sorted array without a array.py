i = 0
j = 0
a = [3,6,8,15,21,23]
b =[2,14,17,25]

while i < len(a) and j < len(b):
    if b[j]<a[i]:
        a[i],b[j] = b[j], a[i]
        while j <len(b)-1:
            if b[j+1]<b[j]:
                b[j],b[j+1] = b[j+1], b[j]
                j+=1
            else:
                break
        i+=1
        j=0
    else:
        j+=1
a.extend(b)
print(a)





