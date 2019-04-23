

def f(x):
    '''阶乘
    
    Arguments:
        x {int or str} -- 传进来的值
    
    Returns:
        int -- x二次方的值
    '''

    if isinstance(x, str):
        x = int(x)
    return x**2
