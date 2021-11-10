import math
no=int(input())
root=math.sqrt(no)
if int(root+0.5)**2==no:
    print(no,'is perfect number')
else:
    print('not a perfect number')