def login(u,p):
    if(u=='admin' and p == 1234):
        l=print('login Correcto')
    else:
        l=print('login incorrecto')
    return l

login('admin',1234)