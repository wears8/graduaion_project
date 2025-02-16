def count_standing_methods(N: int) -> int:
    """
    计算N个小朋友站成一排拍照的站位方法数。
    
    参数:
    N (int): 小朋友的数量
    
    返回:
    int: 站位方法数
    """
    if N <= 0:
        return 0
    elif N == 1:
        return 1
    else:
        return N * count_standing_methods(N - 1)