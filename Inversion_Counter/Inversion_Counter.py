import time

def countinversions(unsorted_array):

	if (len(unsorted_array) == 1):
		return (0, unsorted_array)

	(inversions1, sortArray1) = countinversions(unsorted_array[:(int)(len(unsorted_array)/2)])

	(inversions2, sortArray2) = countinversions(unsorted_array[(int)(len(unsorted_array)/2):])

	(inversions3, sortedFinal) = countInversions(sortArray1, sortArray2)

	return (inversions1 + inversions2 + inversions3, sortedFinal)



def countInversions(sorted_arr1, sorted_arr2):
	output = list()
	i = 0
	j = 0
	inversions = 0
	while (i < len(sorted_arr1) or j < len(sorted_arr2)):
		#Check for i out of bounds
		if (i >= len(sorted_arr1)):
			#just add k
			output.append(sorted_arr2[j])
			j += 1
			continue

		if (j >= len(sorted_arr2)):
			output.append(sorted_arr1[i])
			
			i+=1
			continue

		if (sorted_arr1[i] < sorted_arr2[j]):
			output.append(sorted_arr1[i])
			i+=1
		else:

			output.append(sorted_arr2[j])
			
			inversions += (len(sorted_arr1) - i)

			#print(inversions)

			#for val in sorted_arr1[i:]: 
			#	print('[' + str(val) + ',' + str(sorted_arr2[j]) + ']')



			j+=1
			



	return (inversions, output)




str_in = input("Type in your array file: ")
print("reading from " + (str_in))
infile = open(str_in, 'r')
contents = infile.read()
arr = contents.split('\n')
arr = arr[:-1]
arr_int = [int(n) for n in arr]
t0 = time.time()
(invers, final) = countinversions(arr_int)
end = time.time() - t0
print (invers) 
print(end)
outfile = open((str_in+"_result"), 'w')
outfile.write("\n".join([str(s) for s in final]))




