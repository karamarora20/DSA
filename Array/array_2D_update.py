from array_2D_initialize import create_2d_array
from array_2D_traversal import array_traversal


def array_update(arr: list[list[int]], pos: [int, int], val: int):
    """
    Updates an element in the array at the specified position

    Args:
        arr (list[list[int]]): The array to perform the operation on
        pos ([int,int]): The position at which the element is to be updated
        val (int): The value to be updated
    """
    if arr == []:
        raise Exception("Array is empty")
    elif pos[0] >= len(arr) or pos[0] < -(len(arr)-1):
        raise Exception("Invalid Row position")
    elif pos[1] >= len(arr[0]) or pos[1] < -(len(arr[0])-1):
        raise Exception("Invalid Column position")
    else:
        arr[pos[0]][pos[1]] = val
        return arr


if __name__ == "__main__":
    size = tuple(
        map(int, input("Enter the size of the array (in CSV): ").split(',')))
    array = create_2d_array(size)
    array_traversal(array)
