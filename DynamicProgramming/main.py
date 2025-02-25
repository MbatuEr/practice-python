from dp import Dp

if __name__ == "__main__":
    dp = Dp()
    # Climbing stairs
    a = 4
    b = dp.climbing_stairs_top_down(a)
    print("Result: ", b)
    print("-" * 60)
    
    bu = 5
    ub = dp.climbing_stairs_top_down(bu)
    print("Result: ", ub)
    print("-" * 60)
    
    # Coin combination
    input_coins = [1, 2, 3, 4, 5, 6] 
    target = 13
    res = dp.min_coin_combination_top_down(input_coins, target)
    print("Result: ", res)
    print("-" * 60)
    
    res_bu = dp.min_coin_combination_bottom_up(input_coins, target)
    print("Result: ", res_bu)
    print("-" * 60)
    
    # Matrix pathways
    m, n = 3, 3
    matrix = dp.matrix_pathways(m, n)
    print("Result: ", matrix)
    print("-" * 60)
    
    # Max profit
    Input_houses = [200, 300, 200, 50, 250, 300]
    max_gain = dp.neighbour_burglary(Input_houses)
    print("Result: ", max_gain)
    print("-" * 60)
    
    # Most common characters
    s1, s2 = "acabac", "aebab"
    lcs = dp.longest_common_subsequence(s1, s2)
    print("Result: ", lcs)
    print("-" * 60)
    
    # Largest palindrome
    Input_s = "abccbababc"
    output_s = dp.longest_palindrome_in_a_string(Input_s)
    print("Result: ", output_s)
    print("-" * 60)
    
    # Max sum of a subarray
    Input_nums = [3, 1, -6, 2, -1, 4, -9]
    output_num = dp.maximum_subarray_sum(Input_nums)
    print("Result: ", output_num)
    print("-" * 60)
    
    # Max value with capacity
    cap = 7
    weights = [5, 3, 4, 1] 
    values = [70, 50, 40, 10]
    best_knapstack = dp.knapsack(cap, weights, values)
    print("Result: ", best_knapstack)
    print("-" * 60)
    
    # Largest square
    square_matrix = [
        [1, 0, 1, 1, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1]
    ]
    largest_square = dp.largest_square_in_a_matrix(square_matrix)
    print("Result: ", largest_square)
    print("-" * 60)
    