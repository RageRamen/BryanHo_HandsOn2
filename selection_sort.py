array = [4, 5, 3, 2, 1]

print('Start: ' + str(array))

for i in range(len(array)):
    min_index = i

    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j

    array[min_index], array[i] = array[i], array[min_index]

    print('Iteration ' + str(i+1) + ': ' + str(array))
