def array_search(arr: list, val: int):
    """
    Searches for an element in the array and returns its position

    Args:
        arr (list): The array to perform the operation on
        element (int): The element to be searched

    Returns:
        int: The position of the element in the array
    """
    if arr == []:
        print("Array is empty")
    else:
        pos = []
        for i in range(len(arr)):
            if arr[i] == val:
                pos.append(i)
        return pos


if __name__ == '__main__':
    arr = [int(x) for x in input("Enter the array elements: ")]
    val = int(input("Enter the value to be searched: "))
    print(array_search(arr, val))
