def arr_update(arr: list, pos: int, val: int):
    """
    Updates an element in the array at the specified position

    Args:
        arr (list): The array to perform the operation on
        pos (int): The position at which the element is to be updated
        val (int): The value to be updated
    """
    if arr == []:
        raise Exception("Array is empty")
    elif pos >= len(arr) or pos < -(len(arr)-1):
        raise Exception("Invalid position")
    else:
        arr[pos] = val
        return arr
