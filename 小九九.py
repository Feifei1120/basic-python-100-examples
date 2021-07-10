#一行君,这个乘法表用其他语言至少七八行

print("\n".join([" ".join([f"{j}*{i}={i*j}" for j in range (1,i+1)]) for i in range (1,10)]))