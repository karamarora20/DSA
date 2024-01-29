def arr_insert(arr: list, pos: int, val: int):
    """
    Inserts an element in the array at the specified position

    Args:
        arr (list): The array to perform the operation on
        pos (int): The position at which the element is to be inserted
        element (int): The element to be inserted
    """
    if arr == []:
        print("Array is empty")
    else:
        new_arr = arr[0:pos]
        new_arr.append(val)
        new_arr.extend(arr[pos:])
        return new_arr


if __name__ == '__main__':
    arr = [int(x) for x in input("Enter the array elements: ")]
    pos = int(input("Enter the position to be inserted: "))
    val = int(input("Enter the value to be inserted: "))
    print(arr_insert(arr, pos, val))
