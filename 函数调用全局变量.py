#函数调用全局变量

discount_rate = 0.9
discount = discount_rate #这个时候其实他们两个的id是一样的，命名discount即等于discount_rate的时候，等于告诉计算机，去找discount_rate

def price_calculator(price):
    global discount_rate #声明使用全局变量
    price_paid = price * discount_rate #注意这里price paid是局部变量
    return price_paid
print(price_calculator(price = 100))