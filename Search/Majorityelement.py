def majorityElement( arr):
        count = 0
        candidate = None

        for num in arr:
            if count == 0:
                candidate = num
            print(num)
            count += (1 if num == candidate else -1)

        if arr.count(candidate) > len(arr) // 2:
            return candidate
        return -1
                 


result=majorityElement([3, 1, 3, 3, 2])
print(result)                    