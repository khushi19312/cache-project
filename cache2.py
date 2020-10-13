import math

pa=int(input("Enter size of MAIN MEMORY in power of 2 (EX: 2**x, enter x) : ")) # physical address
ci=int(input("Enter size of CACHE L2 (L1 is L2/2) in power of 2 (EX: 2**y, enter y) : ")) # cache index
bi=int(input("Enter size of BLOCK in power of 2 (EX: 2**z, enter z) : ")) # bloch index 
if(ci>pa):
	print("Cache L2 larger than Main Memory.\nERROR\nProgram terminated!!")
	exit()
elif(bi>pa):
	print("block size larger than Main Memory.\nERROR\nProgram terminated!!")
	exit()
elif(bi>(ci-1)):
	print("block size larger than Cache L1 memory.\nERROR\nProgram terminated!!")
	exit()
elif(bi>ci):
	print("block size larger than Cache L2 memory.\nERROR\nProgram terminated!!")
	exit()
ms=2**pa # main memory size
cs2=2**ci # cache size
cs1=(2**ci)/2
bs=2**bi # block size
cl2=(int)(cs2/bs) # cache lines
cl1=(int)(cs1/bs) # cache lines
clindex2=ci-bi
clindex1=ci-bi-1
nb=(int)(ms/bs) # number of blocks
bindex=pa-bi
cache1=[] #list of cache lines
cache2=[] #list of cache lines
#cachel={}

for i in range(0,cl1):
	cache1.append("-")

for i in range(0,cl2):
	cache2.append("-")

def printcache(cache, clindex,cl):

	print("\n"+"-"*150)
	print('TB'+" "*(pa-bi-clindex-2)+'\t|\t'+'CL\t|\t'+'\t\t\tBlock Offset')
	print("-"*150)
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
		print("\n"+"-"*150)


def mapping():
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
			cacheline1=b[bindex-clindex1:]
			x1=int(cacheline1,2)
			cacheline2=b[bindex-clindex2:]
			x2=int(cacheline2,2)
			#print(x)
			if cache1[x1]==b[0:bindex-clindex1] and cache2[x2]==b[0:bindex-clindex2]:
				print("Cache L1, Cache L2 and Memory updated")
			elif cache1[x1]==b[0:bindex-clindex1]:
				cache2[x2]=b[0:bindex-clindex2]
				print("Cache L1, Cache L2 and Memory updated")
			elif cache2[x2]==b[0:bindex-clindex2]:
				cache1[x1]=b[0:bindex-clindex1]
				print("Cache L1, Cache L2 and Memory updated")
			else:
				cache2[x2]=b[0:bindex-clindex2]
				cache1[x1]=b[0:bindex-clindex1]
				print("Cache L1, Cache L2 and Memory updated")
			
			print("\n\tCACHE L1")
			printcache(cache1, clindex1, cl1)
			print("\n\tCACHE L2")
			printcache(cache2, clindex2, cl2)


		elif(a==2):

			add=input("Enter the address in hexadecimal: ")
			a=format(int(add,16),'b')
			add='0'*(pa-len(a))+a
			b=add[0:bindex]
			cacheline1=b[bindex-clindex1:]
			x1=int(cacheline1,2)
			cacheline2=b[bindex-clindex2:]
			x2=int(cacheline2,2)
			if(cache1[x1]==add[0:bindex-clindex1]):
				print("HIT IN CACHE L1")
			elif(cache2[x2]==add[0:bindex-clindex2]):
				print("MISS IN CACHE L1")
				print("HIT IN CACHE L2, CACHE L1 UPDATED")
				cache1[x1]=add[0:bindex-clindex1]
			else:
				print("MISS IN BOTH CACHE L1 AND CACHE L2")
				cache1[x1]=add[0:bindex-clindex1]
				cache2[x2]==add[0:bindex-clindex2]
				print("CACHE L2 UPDATED AND THEN CACHE L1 UPDATED")

			print("\n\tCACHE L1")
			printcache(cache1, clindex1, cl1)
			print("\n\tCACHE L2")
			printcache(cache2, clindex2, cl2)


		a=int(input("\n\nEnter choice : "))


mapping()