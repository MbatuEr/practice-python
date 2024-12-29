from array_utils import Array


if __name__ == "__main__":
    # Dutch national flag problem.
    obj = Array()
    nums = [3, 5, 2, 1, 7, 3]
    pivot = 3
    obj.DutchNationalFlag(pivot, nums)

    for num in nums:
        print(num, end=' ')
    print("\n----------------------------------------------")

    # Add Binary.
    s1 = "101"
    s2 = "110"

    result_string = obj.AddBinary(s1,s2)
    for i in result_string:
        print(i, end=' ')
    print("\n----------------------------------------------")

    num1 = [1, 2, 3]
    num2 = [9, 8, 7]
    multiplied = obj.Multiply(num1, num2)
    # for i in multiplied:
    #     print(i, end=' ')
    print("Result:", multiplied)
    print("\n----------------------------------------------")




