

def mergesort(unsorted_array):

	if (len(unsorted_array) == 1):
		return unsorted_array

	sortArray1 = mergesort(unsorted_array[:(int)(len(unsorted_array)/2)])
	sortArray2 = mergesort(unsorted_array[(int)(len(unsorted_array)/2):])

	return merge(sortArray1, sortArray2)


def merge(sorted_arr1, sorted_arr2):
	output = list()
	i = 0
	j = 0
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
			j+=1

	return output




str_in = input("Type in your array: ")
print(mergesort(str_in))





