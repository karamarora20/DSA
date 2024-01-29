def array_traversal(arr: list[list[int]]):
    """
    Traverses a 2D array

    Args:
        arr (list[list[int]]): The array to be traversed
    """
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()


if __name__ == '__main__':
    array = [[1, 2, 3, 4], [4, 5, 6, 5], [7, 8, 9, 8]]
    array_traversal(array)
