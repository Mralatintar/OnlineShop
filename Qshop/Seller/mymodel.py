import random
def add_az():
    num=[]
    xdd=[]
    ppd=[]
    for n in range(0,10):
        num.append(str(n))
    for i in range(65,90):
        xdd.append(chr(i))
    for j in range(97,122):
        ppd.append(chr(j))
    xpp=num+xdd+ppd
    jpp="".join(xpp)
    valid_code = "".join([random.choice(jpp) for i in range(6)])
    return valid_code