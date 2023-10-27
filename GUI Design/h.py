names = ['Saqlain', 'Ali', 'Hassan', 'Talha', 'Ali']

# Step 1: Sort the array
names.sort()

# Step 2: Perform a binary search to find all occurrences of 'Ali'
def binary_search(array, target):
    start = 0
    end = len(array) - 1
    occurrences = []

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            occurrences.append(mid)
            # Check for other occurrences to the left and right
            left = mid - 1
            right = mid + 1
            while left >= 0 and array[left] == target:
                occurrences.append(left)
                left -= 1
            while right < len(array) and array[right] == target:
                occurrences.append(right)
                right += 1
            return occurrences
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return occurrences  # Element not found

# Find all occurrences of 'Ali'
occurrences = binary_search(names, 'Ali')

# Print the indices of 'Ali' in the sorted array
print(occurrences)

print(names)
