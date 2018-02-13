    '''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import numpy as np
value=input()


N,M=value.split(" ")
N=int(N)
M=int(M)


a=np.empty([N,M],dtype='int')
b=np.empty([M,N],dtype='int')

for i in range(0,N):
    value=input()
    value=value.split(" ")
    for j in range(0,M):
        a[i][j]=value[j]

for i in range(0,N):
    for j in range(0,M):
        b[j][i]=a[i][j]

value = ''

for i in range(0,M):
    for j in range(0,N):
        value=value+str(b[i][j])+" "
    value=value+"\n"    
        
print (value) 
