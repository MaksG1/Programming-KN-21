def insertion_sort(arr, ascending=True):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        if ascending:
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

        else:
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1

        arr[j + 1] = key

    return arr

if __name__ == "__main__":

    list1 = [5, 2, 9, 1, 5, 6]
    list2 = [3, 7, 4, 8, 1, 2]

    sorted_list1 = insertion_sort(list1.copy(), ascending=True)
    print("Список 1 (за зростанням):", sorted_list1)

    sorted_list2 = insertion_sort(list2.copy(), ascending=False)
    print("Список 2 (за спаданням):", sorted_list2)