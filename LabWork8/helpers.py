def check_error(arr1, arr2, epsilon):
    if len(arr1) != len(arr2):
        raise ValueError('Довжини масивів не співпадають')

    for i in range(len(arr1)):
        if abs(arr1[i] - arr2[i]) > epsilon:
            return False

    return True