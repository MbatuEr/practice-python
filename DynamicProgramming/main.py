from dp import Dp

if __name__ == "__main__":
    dp = Dp()
    # Climbing stairs
    stairs_length = 4
    min_step_top_down = dp.climbing_stairs_top_down(stairs_length)
    print("Min step:", min_step_top_down)
    print("-" * 60)
    
    min_step_bottom_up = dp.climbing_stairs_bottom_up(stairs_length)
    print("Min step:", min_step_bottom_up)
    print("-" * 60)
    
    # Coin combination
    input_coins = [1, 2, 3, 4, 5, 6] 
    target = 13
    coin_combination = dp.min_coin_combination_top_down(input_coins, target)
    print("The number of coins to reach the target value:", coin_combination)
    print("-" * 60)
    
    coin_bottom_up = dp.min_coin_combination_bottom_up(input_coins, target)
    print("The number of coins to reach the target value:", coin_bottom_up)
    print("-" * 60)
    
    # Matrix pathways
    m, n = 3, 3
    matrix = dp.matrix_pathways(m, n)
    print("Number of different pathways to complete the matrix::", matrix)
    print("-" * 60)
    
    # Max profit
    Input_houses = [200, 300, 200, 50, 250, 300]
    max_gain = dp.neighbor_burglary(Input_houses)
    print("Max amount of money can be stolen:", max_gain)
    print("-" * 60)
    
    # Most common characters
    s1, s2 = "acabac", "aebab"
    lcs = dp.longest_common_subsequence(s1, s2)
    print("Number of common characters:", lcs)
    print("-" * 60)
    
    # Largest palindrome
    Input_s = "abccbababc"
    output_s = dp.largest_palindrome_in_a_string(Input_s)
    print("Largest palindrome in the string:", output_s)
    print("-" * 60)
    
    # Max sum of a subarray
    Input_nums = [3, 1, -6, 2, -1, 4, -9]
    output_num = dp.maximum_subarray_sum(Input_nums)
    print("Max sum of a subarray:", output_num)
    print("-" * 60)
    
    # Max value with capacity
    cap = 7
    weights = [5, 3, 4, 1] 
    values = [70, 50, 40, 10]
    best_knapstack = dp.knapsack(cap, weights, values)
    print("The best combination of goods:", best_knapstack)
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
    print("Area of largest square with value 1:", largest_square)
    print("-" * 60)
    