array = [4, 5, 3, 2, 1]

print('Start: ' + str(array))

for i in range(len(array)):
    for j in range(len(array) - (i + 1)):
        if array[j] > array[j + 1]:
            array[j], array[j+1] = array[j + 1], array[j]

    print('Iteration ' + str(i+1) + ': ' + str(array))
