print("Hello{0[0]} and {0[1]}".format(('foo', 'bin')))
print('*',"abcde".center(6),'*',sep="")
print(min(max(False, -3, -4),2,7))
x=10
print(type(x))

x= 20
X=30
print(x,X)

l1 = [1,2,3,[4,5]]
l2 = l1
l1[-1][0] = 6
print(l2)

for i in range(5):
    print(i)

#swap without temp

a = 10; b = 20
a,b =b,a

print("a=", a, "b=", b)

#Given 2 arrays
# Find pairs which have minimum difference
a=[10,23,12,41]; b = [34,56,12,8]
result = []
def min_index(lst):
    m = lst[0]; j= 0 ; index = 0
    while( j < len(lst)):
        if (lst[j] < m):
            lst[j],m = m, lst[j]
            index = j
        j= j+1
    return index
for el in a:
    diff = []
    for ch in b:
        diff.append(abs(el-ch))
    m_index = min_index(diff)
    result.append((el,b[m_index]))
print("result:", result)


strg = "shalini"
count = 0
for ch in strg:
    count = count+1
print(count)

#find maximum of 3 numbers without max/sort functions
