# Reference: https://connor-mccartney.github.io/cryptography/small-roots/corrupt-key-2-picoMini

def coppersmith(f, bounds, m=1, t=1):
    n = f.nvariables()
    N = f.base_ring().cardinality()
    leading = 1 / f.coefficients().pop(0)
    f = f.map_coefficients(lambda x: x * leading)
    f = f.change_ring(ZZ)
    x = f.parent().objgens()[1]

    g = []
    monomials = []
    Xmul = []
    for ii in IIter(m, n):
        k = ii[0]
        g_tmp = f^k * N^max(t-k, 0)
        monomial = x[0]^k
        Xmul_tmp = bounds[0]^k
        for j in range(1, n):
            g_tmp *= x[j]^ii[j]
            monomial *= x[j]^ii[j]
            Xmul_tmp *= bounds[j]^ii[j]
        g.append(g_tmp)
        monomials.append(monomial)
        Xmul.append(Xmul_tmp)

    B = Matrix(ZZ, len(g), len(g))
    for i in range(B.nrows()):
        for j in range(i + 1):
            if j == 0:
                B[i,j] = g[i].constant_coefficient()
            else:
                v = g[i].monomial_coefficient(monomials[j])
                B[i,j] = v * Xmul[j]

    print("LLL...")
    B = B.LLL()
    print("LLL finished")

    ###############################################

    print("polynomial reconstruction...")

    h = []
    for i in range(B.nrows()):
        h_tmp = 0
        for j in range(B.ncols()):
            if j == 0:
                h_tmp += B[i, j]
            else:
                assert B[i,j] % Xmul[j] == 0
                v = ZZ(B[i,j] // Xmul[j])
                h_tmp += v * monomials[j]
        h.append(h_tmp)

    x_ = [ var(f'x{i}') for i in range(n) ]
    for ii in Combinations(range(len(h)), k=n):
        f = symbolic_expression([ h[i](x) for i in ii ]).function(x_)
        jac = jacobian(f, x_)
        v = vector([ t // 2 for t in bounds ])
        for _ in range(200):
            kwargs = {f'x{i}': v[i] for i in range(n)}
            tmp = v - jac(**kwargs).inverse() * f(**kwargs)
            v = vector((numerical_approx(d, prec=200) for d in tmp))
        v = [ int(_.round()) for _ in v ]
        if h[0](v) == 0:
            return v

    return []