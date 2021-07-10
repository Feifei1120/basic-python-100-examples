import string
import random

code = " ".join((random.sample((string.digits+string.ascii_lowercase+string.ascii_uppercase),8)))
#上面这行代码做了个A-Z大小写以及零到九的随机混合，随机8个
print("你的验证码为： ", code)
current_name=input("请输入姓名： ")
current_code=input("请输入验证码： ")
if current_code==code:
    print("验证通过！")
else:
    print("验证失败！")
