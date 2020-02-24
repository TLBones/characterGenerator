def modFind(stat):
    mod = 0
    if stat==30:
        mod=10
    elif stat>=28:
        mod=9
    elif stat>=26:
        mod=8
    elif stat>=24:
        mod=7
    elif stat>=22:
        mod=6
    elif stat>=20:
        mod=5
    elif stat>=18:
        mod=4
    elif stat>=16:
        mod=3
    elif stat>=14:
        mod=2
    elif stat>=12:
        mod=1
    elif stat>=10:
        mod=0
    elif stat>=8:
        mod=-1
    elif stat>=6:
        mod=-2
    elif stat>=4:
        mod=-3
    elif stat>=2:
        mod=-4
    elif stat>=1:
        mod=-5
        return mod
    return mod


    
