from array_2D_traversal import array_traversal


def create_2d_array(size: [int, int]) -> list[list[int]]:
    """
    Creates a 2D array of the specified size

    Args:
        size ([int,int]): The size of the array to be created

    Returns:
        list[list[int]]: The created array
    """
    arr = []
    for i in range(size[0]):
        temp = input(
            f"Enter the elements of row {i+1} (CSV format): ").split(',')
        while len(temp) != size[1]:
            print(f"Please enter {size[1]} elements")
            temp = input(
                f"Enter the elements of row {i+1} (CSV format): ").split(',')
        row = list(map(int, temp))
        arr.append(row)
    return arr


if __name__ == '__main__':
    size = [int(x) for x in input(
        "Enter the size of the array (in CSV): ").split(',')]
    array = create_2d_array(size)
    array_traversal(array)
