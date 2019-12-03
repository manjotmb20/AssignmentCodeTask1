# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/welcome.ipynb
"""

def chords(n):
  mod=10**9+7
  if n==0 or n==1:
    return 1
  nchord=[0]*(n+1)  
  nchord[0]=1
  nchord[1]=1
  for i in range(2,n+1):
    nchord[i]=0
    for j in range(0,i):
      nchord[i]=(nchord[i]+nchord[j]*nchord[i-j-1])
  return nchord[n]%mod   


print("Enter the number of chords")
A=int(input())
c=chords(A)
print(c)

