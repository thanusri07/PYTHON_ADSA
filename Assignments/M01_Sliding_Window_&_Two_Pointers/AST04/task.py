def pairInSortedRotated(arr, target):
    n = len(arr)
    if n < 2:
        return False
    smallest = 0
    for i in range(1, n):
        if arr[i] < arr[smallest]:
            smallest = i
    left = smallest
    right = (smallest - 1 + n) % n
    while left != right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        if current_sum < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n
    return False
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    print(pairInSortedRotated(arr, target))