def rsteff(fun, x_0, err, mit):
    hx = []
    hf = []
    v = fun(x_0)

    for it in range(mit):
        x_k = x_0 - (v**2)/(fun(x_0 + fun(x_0)) - fun(x_0))
        v = fun(x_k)
        hx.append(x_k)
        hf.append(v)
        if abs(v) < err or (abs(x_0 - x_k) / abs(x_k)) < err:
            print("salimos")
            break
        x_0 = x_k

    return hx, hf
