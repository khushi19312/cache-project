from collections import deque
import math

pa=int(input("Enter size of MAIN MEMORY in power of 2 (EX: 2**x, enter x) : ")) # physical address
ci=int(input("Enter size of CACHE in power of 2 (EX: 2**y, enter y) : ")) # cache index
bi=int(input("Enter size of BLOCK in power of 2 (EX: 2**z, enter z) : ")) # bloch index 
if(ci>pa):
	print("Cache larger than Main Memory.\nERROR\nProgram terminated!!")
	exit()
elif(bi>pa):
	print("block size larger than Main Memory.\nERROR\nProgram terminated!!")
	exit()
elif(bi>ci):
	print("block size larger than Cache memory.\nERROR\nProgram terminated!!")
	exit()
ms=2**pa # main memory size
cs=2**ci # cache size
bs=2**bi # block size
cl=(int)(cs/bs) # cache lines
clindex=ci-bi
nb=(int)(ms/bs) # number of blocks
bindex=pa-bi
cache=[] #list of cache lines
#cachel={}

for i in range(0,cl):
	cache.append("-")
"""print(cs)
print(bs)
print(cl)
print(clindex)
print(nb)
print(bindex)"""

def printcachedm():

	print("\n"+"-"*160)
	print('TB'+" "*(pa-bi-clindex-2)+'\t|\t'+'CL\t|\t'+'\t\t\tBlock Offset')
	print("-"*160)
	for i in range(0,cl):
		print(cache[i]+" "*((pa-bi-clindex)-len(cache[i]))+"\t|\t",end="")
		c=format(i,'b')
		c='0'*(clindex-len(c))+c
		print(c,end="\t| ")
		if(cache[i]!='-'):
			for j in range(0,bs):
				d=format(j,'b')
				d='0'*(bi-len(d))+d
				print(d,end="\t ")
		print("\n"+"-"*160)

def printcachesam(si):
	print("\n"+"-"*160)
	print('TB'+" "*(pa-bi-si-2)+'\t|\t'+'SI\t|\t'+'\t\t\tBlock Offset')
	print("-"*160)
	for i in range(0,cl):
		print(cache[i]+" "*((pa-bi-si)-len(cache[i]))+"\t|\t",end="")
		c=(int)(i/2)
		c=format(c,'b')
		c='0'*(si-len(c))+c
		print(c,end="\t| ")
		if(cache[i]!='-'):
			for j in range(0,bs):
				d=format(j,'b')
				d='0'*(bi-len(d))+d
				print(d,end="\t ")
		print("\n"+"-"*160)

def printcacheam():
	print("\n"+"-"*160)
	print('CL\t|\t'+'TB'+" "*(pa-bi-2)+'\t|\t'+'\t\t\tBlock Offset')
	print("-"*160)
	for i in range(0,cl):
		c=format(i,'b')
		c='0'*(clindex-len(c))+c
		print(c,end="\t|\t")
		print(cache[i]+" "*((pa-bi)-len(cache[i]))+"\t| ",end="")
		if(cache[i]!='-'):
			for j in range(0,bs):
				d=format(j,'b')
				d='0'*(bi-len(d))+d
				print(d,end="\t ")
		print("\n"+"-"*160)




def directmapping():
	print("Choose from the options :")
	print("1. Write into the memory.")
	print("2. Read cache and see if address is in the cache.")
	print("3. exit")
	a=int(input("Enter choice : "))
	#print("\n\n\n")
	while(a!=3):
		if(a==1):
	
			add=input("Enter the address in hexadecimal : ")
			a=format(int(add,16),'b')
			if (pa-len(a))>=0:
				add='0'*(pa-len(a))+a
			else:
				t=len(a)-pa
				add=add[t:]
			data=input("Enter data : ")
			b=add[0:bindex]
			#bo=add[bindex:]
			#bo=int(bo,2)
			#print (bo)
			cacheline=b[bindex-clindex:]
			x=int(cacheline,2)
			#print(x)
			if cache[x]==b[0:bindex-clindex]:
				print("Memory and Cache updated")
			else:
				cache[x]=b[0:bindex-clindex]
			#cache[x][0]='011'
			#cache[x][bo]=data
			printcachedm()


		elif(a==2):

			add=input("Enter the address in hexadecimal: ")
			a=format(int(add,16),'b')
			add='0'*(pa-len(a))+a
			b=add[0:bindex]
			cacheline=b[bindex-clindex:]
			x=int(cacheline,2)
			c=cache[x]
			if(c==add[0:bindex-clindex]):
				print("HIT")
			else:
				print("MISS")
				print("Cache updated")
				cache[x]=b[0:bindex-clindex]
			printcachedm()

		a=int(input("\n\nEnter choice : "))

def associativemapping():
	print("Choose from the options :")
	print("1. Write into the memory.")
	print("2. Read cache and see if address is in the cache.")
	print("3. exit")
	a=int(input("Enter choice : "))
	#print("\n\n\n")
	q = deque()
	while(a!=3):
		
		if(a==1):
			flag=0
			add=input("Enter the address in hexadecimal : ")
			a=format(int(add,16),'b')
			if (pa-len(a))>=0:
				add='0'*(pa-len(a))+a
			else:
				t=len(a)-pa
				add=add[t:]
			data=input("Enter data : ")
			b=add[0:bindex]
			 
			for i in range(0,cl):
				if(cache[i]==b):
					print("Memory and Cache updated")
					flag=1
					break
			if flag==0:
				for i in range(0,cl):
					if(cache[i]=='-'):
						cache[i]=b
						q.append(i)
						flag=1
						break

			if(flag==0):
				x=q.popleft()
				cache[x]=b
				q.append(x)
			printcacheam()


		elif(a==2):

			add=input("Enter the address in hexadecimal : ")
			a=format(int(add,16),'b')
			add='0'*(pa-len(a))+a
			b=add[0:bindex]
			flag=0
			f=0
			for i in range(0,cl):
				if(cache[i]==b):
					print("HIT")
					flag=1
					break
			if flag==0:
				print("MISS")
				print("Cache updated")
				for i in range(0,cl):
					if(cache[i]=="-"):
						cache[i]=b
						q.append(i)
						f=1
						break
				if(f==0):
					x=q.popleft()
					cache[x]=b
					q.append(x)
			printcacheam()

		a=int(input("\n\nEnter choice : "))

def setassociativemapping():
	k=int(input("Enter k-way division for set-associative cache (k) : "))
	if(k>cl):
		print("lines per set greater than number of cache lines.\nERROR\nProgram terminated!!")
		exit()
	s=(int)(cl/k)
	#print(s)
	si=(int)(math.log(s,2))
	#print(si)
	print("Choose from the options :")
	print("1. Write into the memory.")
	print("2. Read cache and see if address is in the cache.")
	print("3. exit")
	a=int(input("Enter choice : "))
	#print("\n\n\n")
	while(a!=3):
		if(a==1):
	
			add=input("Enter the address in hexadecimal : ")
			a=format(int(add,16),'b')
			if (pa-len(a))>=0:
				add='0'*(pa-len(a))+a
			else:
				t=len(a)-pa
				add=add[t:]
			data=input("Enter data : ")
			b=add[0:pa-bi]
			#print(b)
			set=b[pa-bi-si:]#required set
			#print(set)
			x=int(set,2)
			x=x*k
			#print(x)
			flag=0
			for i in range(x,x+k):
				if(cache[i]==b[0:pa-bi-si]):
					print("Memory and Cache updated")
					flag=1
					break
			if flag==0:	
				for i in range(x,x+k):
					if(cache[i]=="-"):
						cache[i]=b[0:pa-bi-si]
						flag=1
						break
			if(flag==0):
				cache[x]=b[0:pa-bi-si]
			printcachesam(si)


		elif(a==2):

			add=input("Enter the address in hexadecimal : ")
			a=format(int(add,16),'b')
			add='0'*(pa-len(a))+a
			b=add[0:pa-bi]
			set=b[pa-bi-si:]#required set
			x=int(set,2)
			x=x*k
			flag=0
			f=0
			for i in range(x,x+k):
				if(cache[i]==add[0:pa-bi-si]):
					print("HIT")
					flag=1
					break
			if flag==0:
				print("MISS")
				print("Cache updated")
				for i in range(x,x+k):
					if(cache[i]=="-"):
						cache[i]=b[0:pa-bi-si]
						f=1
						break
				if(f==0):
					cache[x]=b[0:pa-bi-si]
			printcachesam(si)

		a=int(input("\n\nEnter choice : "))
		
print("Choose from :")
print("1. Direct mapping")
print("2. Associative mapping")
print("3. Set-Associative mapping")
y=int(input("Enter choice : "))

if y==1:
	print("\n\t\t\t\tDIRECT MAPPING")
	directmapping()
if y==2:
	print("\n\t\t\t\tASSOCIATIVE MAPPING")
	associativemapping()
if y==3:
	print("\n\t\t\t\tSET-ASSOCIATIVE MAPPING")
	setassociativemapping()