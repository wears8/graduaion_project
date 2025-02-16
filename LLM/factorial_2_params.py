def factorial_2(N):
    if N < 2:
        return 0
    # 将两个小朋友视为一个整体，那么总共有 (N - 1) 个“小朋友”
    # 这 (N - 1) 个“小朋友”有 (N - 1)! 种排列方式
    # 两个小朋友在整体内部有 2! 种排列方式
    # 所以总的方法数为 (N - 1)! * 2!
    
    # 计算 (N - 1)!
    factorial_n_minus_1 = 1
    for i in range(1, N):
        factorial_n_minus_1 *= i
    
    # 计算 2!
    factorial_2 = 2
    
    # 总方法数
    total_methods = factorial_n_minus_1 * factorial_2
    
    return total_methods