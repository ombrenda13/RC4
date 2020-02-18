#!/usr/bin/env python
# coding: utf-8

# In[12]:
S=list(range(256)) 
key=input() #llave 
plaintext=input() #texto a cifrar
len_text=len(plaintext)#tamaño del texto a cifrar
mod_key=len(key) #tamaño de la llave
llave=list(key) #string de llave convertido en lista
text=list(plaintext)# string de texto a cifrar convertido en lista

for i in range (0,mod_key):
    llave[i]=ord(llave[i]) #convertir los caracteres de la llave en valores ASCII
    
for i in range (0,256):
    S.append(i) 

j=0

# Key-scheduling algorithm (KSA)
for i in range (0,256):
    j=(j + S[i] + llave[i%mod_key])%256 
    tempo=S[i]
    S[i]=S[j]
    S[j]=tempo

i=0
j=0
encripted=[]
string=""
#Pseudo-random generation algorithm (PRGA)
for h in range(0,len_text):
    i=(i+1)%256
    j=(j+S[i])%256
    tempo=S[i]
    S[i]=S[j]
    S[j]=tempo
    k=S[(S[i]+S[j])%256]^ord(text[h]) #XOR 
    encripted.append(format(k, '02x'))#convertir k en hex 
    #print(format(k, '02x'))
string=string.join(encripted)
print(string.upper())    


