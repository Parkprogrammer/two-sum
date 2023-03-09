def twoSum(nums,target):
	returnlist=[]
	for i in range(0,len(nums)):
		for j in range(i+1,len(nums)):
			num=num[i]+num[j]
			if i==j:
				continue;
			if num==target:
				returnlist.append(i)
				returnlist.append(j)
				return returnlist
