
from algoritms import *

array = ['abc', 'xyz', 'pqr', 'Lmn', 'def', 'ghi', 'jkl', 'Stu', 'vwx']

array2 = [
    'realme 9i (Prism Blue, 64 GB)',
    'realme 9i (Prism Black, 64 GB)',
    'realme 9i (Prism Blue, 128 GB)',
    'realme 9i (Prism Black, 128 GB)',
    'realme 9i (Prism Blue, 128 GB)',
    'POCO C31 (Shadow Gray, 64 GB)',
    'REDMI 9i Sport (Metallic Blue, 64 GB)',
    'REDMI 9i Sport (Coral Green, 64 GB)',
    
    'MOTOROLA e40 (Carbon Gray, 64 GB)',
    'POCO C31 (Royal Blue, 64 GB)',
    'POCO C31 (Royal Blue, 32 GB)',
    'REDMI 10 (Caribbean Green, 64 GB)',
    'REDMI 10 (Midnight Black, 64 GB)',
    'REDMI 9i Sport (Carbon Black, 64 GB)',
    'MOTOROLA e40 (Pink Clay, 64 GB)',
    'POCO M4 Pro 5G (Cool Blue, 64 GB)',
    'MOTOROLA g52 (Charcoal Grey, 128 GB)',
    'MOTOROLA G32 (Mineral Gray, 64 GB)',
    'POCO M4 Pro 5G (Cool Blue, 128 GB)',
    'MOTOROLA g52 (Metallic White, 128 GB)',
    'realme 9 (Sunburst Gold, 128 GB)',
    'realme 9 (Meteor Black, 128 GB)',
    'realme 9 (Meteor Black, 128 GB)',
    'vivo T1X (Gravity Black, 64 GB)',
    'APPLE iPhone 13 (Midnight, 128 GB)'
]

# cycle_sort(array2)

arr = ['Saqlain', 'Ali', 'Hassan', 'Taha', 'Nasir', 'Ahsan', 'Zain', 'Zohaib', 'Zu', 'Zuhaib', 'Tayyab']

selection_sort(arr)
print(arr)

x  = binary_search(arr, 0, len(arr)-1, 'Taha')
print(x)
if x != -1:
    print(arr[x])
    print("Found")
else:
    print("Not Found")

# for i in array2:
#     print(i)