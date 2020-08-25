# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # 牛顿迭代
    a = float(input())
    e = 0.0001
    t = a
    while abs(t*t*t - a) > e:
        # x(i+1) = x(i) - f(xi)/f(xi)'
        t = t - ( t*t*t - a )* 1.0 / (3 * t*t)
    print("%.1f" %t)