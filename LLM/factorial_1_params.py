def factorial_1(N):
    """
    计算N个小朋友站成一排的站位方法数。
    
    参数:
    N (int): 小朋友的数量
    
    返回:
    int: 站位方法数
    """
    if N == 0 or N == 1:
        return 1
    else:
        return N * factorial_1(N - 1)