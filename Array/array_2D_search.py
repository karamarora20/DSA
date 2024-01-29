from Array_search import array_search
from array_2D_initialize import create_2d_array


def array_2d_search(arr: list[list[int]], val: int):
    pos = []
    for row in range(len(arr)):
        cols = array_search(arr[row], val)
        for col in cols:
            pos.append((row, col))
    return pos


if __name__ == '__main__':
    size = tuple(
        map(int, input("Enter the size of the array (in CSV): ").split(',')))
    array = create_2d_array(size)
    val = int(input("Enter the value to be searched: "))
    pos = array_2d_search(array, val)
    if pos == []:
        raise Exception("Element not found")
    print(f"Element found at position(s): {pos}")
