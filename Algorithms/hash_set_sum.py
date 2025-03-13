def twoSum(arr, target):
    s = set()
    for num in arr:
        complement = target - num
        if complement in s:
            return True
        s.add(num)
    return False


arr = [0, -1, 2, 3, 1]
target = 6


if twoSum(arr, target):
    print("true")
else:
    print("false")
