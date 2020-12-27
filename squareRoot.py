def squareRoot(n, g):
    v = g * g
    c = 0
    while g != 0 and abs(v-n) > 0.000000001:
        for t in range(0, abs(v-n) != 0.000000001):
            g = (g + (n/g))/2
            v = g * g
            c += 1
            print('-'*30)
            print(f'  Path       Value(v)      Hint(g)          Damp ')
            print(f'  {c}        {v:2f}        {g:2f}         {abs(v-n):2f}')
        if abs(v-n) != 0.000000001:
            continue
        else:
            break
    print('The value met the convergence criteria.')
    print(f'The square root of {n} is {g:5f} after {c} paths of Heron method')

squareRoot(25, 4)