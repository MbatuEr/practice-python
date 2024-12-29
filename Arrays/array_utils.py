class Array:
    # Sorts a vector around a pivot.
    def DutchNationalFlag(self, pivot, nums):
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] < pivot:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == pivot:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums
    
    # Adds two binary numbers represented as strings
    def AddBinary(self, s1, s2):
        result = []
        carry = 0
        i, j = len(s1) - 1, len(s2) - 1

        while i >= 0 or j >= 0 or carry > 0:
            total = carry
            if i >= 0:
                total += int(s1[i])
                i -= 1
            if j >= 0:
                total += int(s2[j])
                j -= 1
            
            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))
    
    def Multiply(self, v1, v2):
        n = len(v1)
        m = len(v2)
        sign = -1 if (v1[0] < 0) ^ (v2[0] < 0) else 1
        v1[0], v2[0] = abs(v1[0]), abs(v2[0])

        result = [0] * (n + m)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                product = v1[i] * v2[j]
                sum_ = product + result[i + j + 1]  
                result[i + j + 1] = sum_ % 10       
                result[i + j] += sum_ // 10         

        while len(result) > 1 and result[0] == 0:
            result.pop(0)

        result[0] *= sign
        return result
