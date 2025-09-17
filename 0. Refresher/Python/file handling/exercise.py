

summation=0
with open("glycemia.csv", "r") as data:

	lst=[[]]
	lst1=[] #word list
	lst2=[] #avg list
	lst3=[]
	j=0
	
	for line in data:

		summation=0

		line = line.strip()
		lst1 = line.split(";")
		print(lst1)

		for i in range(1, len(lst1)):
			summation+=float(lst1[i])
			print(lst1[i])
		print("...")

		avg=summation/6
		lst.append(lst1)
		lst2.append(avg)
		#lst3.append(summation)

		lst[j].append(avg)
		j+=1

	print(lst2)
	#print(lst3)




with open("new_glycemia.csv", "a") as new_data:
	i=0
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			
			new_data.write(str(lst[i][j])+";")
		new_data.write("\n")






