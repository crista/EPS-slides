import math

def hypotenuse(x, y): 
    h = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) 
    return h, "x=" + str(x) + ";y=" + str(y) + "h=" + str(h) 

# Problem:
pow(hypotenuse(6, 16), 4);

def hypotenuse(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

#((float, float) -> float) -> ((float, float) -> (float, string))
def makeTraceable_f_f(f):
    def traceable_f_f(x,y):
        h=f(x,y)
        return h, str(f) + " was called, result=" + str(h) + "\n"
    return traceable_f_f

# Now let's make one of these! And call it
aTraceableHypo = makeTraceable_f_f(hypotenuse)
aTraceableHypo(3,4)

# But this still doesn't work:
pow(aTraceableHypo(3,4), 2)

#(((float, float) -> (float, string)), float) -> 
#          (((float, float) -> (float, string)) -> (float, string))
def makeTraceable_f_s_f(f, p):
    def traceable_f_s_f(t_f_f):
        r = f(t_f_f[0], p)
        return r, t_f_f[1] + str(f)+" was called, result="+str(r) + "\n"
    return traceable_f_s_f

# Now let's make one of these!
aTraceablePowOf2=makeTraceable_f_s_f(pow, 2)

(result,message)=aTraceablePowOf2(aTraceableHypo(3,4))
print result
print message

# Let's "bind" them externally instead
# (t, (t->t')) -> t'
def bind(t, f):
    return f(t)

(r, m) = bind(aTraceableHypo(3,4), aTraceablePowOf2)
