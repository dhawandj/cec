# PYTHON LAB PROGRAM 4
# 4) AIM: Discuss different collections like list, tuple and dictionaries
# a) Write a python program to implement insertion sort and merge sort using lists

def insertion_sort(arr):
        for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and key < arr[j]:
                        arr[j + 1] = arr[j]
                        j -= 1
                        arr[j + 1] = key

        return arr
#second method
def merge_sort(arr):
        if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]
                merge_sort(left_half)
                merge_sort(right_half)
                i = j = k = 0
                while i < len(left_half) and j < len(right_half):
                        if left_half[i] < right_half[j]:
                                        arr[k] = left_half[i]
                                        i += 1
                        else:
                                arr[k] = right_half[j]
                                j += 1
                        k += 1
                                
                while i < len(left_half):
                        arr[k] = left_half[i]
                        i += 1
                        k += 1

                while j < len(right_half):
                        arr[k] = right_half[j]
                        j += 1
                        k += 1
                return arr
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = insertion_sort(my_list)
print("Sorted list using Insertion sort:",sorted_list)
sorted_list = merge_sort(my_list)
print("Sorted list using Merge sort:",sorted_list)


# Output:
# Sorted list using Insertion sort: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
# Sorted list using Merge sort: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]