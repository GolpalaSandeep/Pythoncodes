D={'spam':8,'eggs':2}
F={'food':{'ham':1,'egg':{'hig':32,'pig':56}}}
print (D['spam'])
print(F['food']['egg']['pig'])
F=dict(name='Bob',age=40)
print(F)
keyslist=[1,2,3,4]
valslist=["me","you","he","she"]
M=dict(zip(keyslist,valslist))
print(M)
print(D.items())
G=D.copy()
print(G)
print(D.get('run',100))