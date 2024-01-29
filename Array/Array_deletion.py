def arr_delete(arr: list, pos: int = -1):
    """
    Args:
        arr (list): The array to perform the operation on
        pos (int, optional): the position from which to be deleted. Default=-1.
    """
    if arr == []:
        print("Array is empty")
    else:
        new_arr = arr[0:pos]
        new_arr.extend(arr[pos+1:])
        return new_arr


if __name__ == '__main__':
    arr = [int(x) for x in input("Enter the array elements: ")]
    pos = int(input("Enter the position to be deleted: "))
    print(arr_delete(arr, pos))
