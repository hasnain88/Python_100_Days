# Formula to Calculate EMI is: P X R X (1+R)^N/[(1+R^N-1)]
# P = Principal
# R = Rate of Interest
# N = Duration



def emi_calculator(principal, rate, time):
    r = rate/12/100
    emi = (principal * r * (1+r)**time) / (((1+r)**time)-1)
    return emi

print(emi_calculator(500000,8.75,240))