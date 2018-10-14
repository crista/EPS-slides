VOID = lambda x: x
# or, for debugging
def VOID(_):
    raise Exception('VOID cannot be called')

# Booleans and conditionals
IF = lambda c: lambda t: lambda f: c(t)(f)
TRUE  = lambda t: lambda f: t
FALSE = lambda t: lambda f: f
print (IF (TRUE) ("true") ("false"))
print (IF (FALSE) ("true") ("false"))

# Numbers and arithmetic
ZERO  = lambda f: lambda x: x 
ONE   = lambda f: lambda x: f(x)
TWO   = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR  = lambda f: lambda x: f(f(f(f(x))))
FIVE  = lambda f: lambda x: f(f(f(f(f(x)))))
SIX   = lambda f: lambda x: f(f(f(f(f(f(x))))))
# Helpers
def numeral(n):
    return lambda f: lambda x: x if n==0 else f(numeral(n-1)(f)(x))
npy  = lambda c: c(lambda x: x+1)(0)


SUCC = lambda n: lambda f: lambda x: f(n(f)(x))
ADD  = lambda n: lambda m: lambda f: lambda x: n(f)(m(f)(x))
MUL  = lambda n: lambda m: lambda f: lambda x: m(n(f))(x)
# Examples
print (npy(ZERO))
print (npy(SUCC(ZERO)))
print (npy(SUCC(SUCC(ZERO))))
ONE = SUCC(ZERO)
TWO = SUCC(ONE)
FOUR = ADD(TWO)(TWO)
SIXTEEN = MUL(FOUR)(FOUR)
print (npy(FOUR))
print (npy(SIXTEEN))


# Pairs and lists (data structures)
PAIR  = lambda a: lambda b: lambda f: f(a)(b)
LEFT  = lambda p: p(lambda a: lambda b: a)
RIGHT = lambda p: p(lambda a: lambda b: b)
# Examples
print (LEFT (PAIR ("left") ("right")))
print (RIGHT (PAIR ("left") ("right")))

NIL   = lambda onnil: lambda onlist: onnil(VOID)
CONS  = (lambda hd: lambda tl: lambda onnil: lambda onlist: onlist(hd)(tl))
CONSP = lambda l: l (lambda hd: lambda tl: TRUE) (lambda void: FALSE)
NILP  = lambda list: list (lambda x: TRUE) (lambda hd: lambda tl: FALSE)
HEAD  = lambda list: list (VOID) (lambda hd: lambda tl: hd)
TAIL  = lambda list: list (VOID) (lambda hd: lambda tl: tl)
# Examples
print (IF (NILP(NIL)) ("nil") ("not nil"))
print (IF (NILP(CONS(10)(20))) ("nil") ("not nil"))
print (IF (CONSP(CONS(10)(20))) (lambda x: "cons") (lambda x: "nil"))
print (HEAD (CONS ("head") ("tail")))
print (TAIL (CONS ("head") ("tail")))


# Combinators and recursion
U = lambda f: f(f)
test = lambda x: "called"
U(test)
# Omega = U(U)  # Stack over-flow from infinite loop

# Example
fact = U(lambda f: lambda n: 1 if n <= 0 else n*(U(f))(n-1))
print (fact(5))

# Y combinator
# Y(F) = x   such that   x = F(x)
# Y(F) = x   such that   x = F(Y(F))
# Y(F) = F(Y(F))
# Y = lambda F: F(Y(F))  # works for call-by-name

Y = lambda F: F(lambda x: Y(F)(x))

fact = Y(lambda f: lambda n: 1 if n <= 0 else n * f(n-1))

print (fact(6))


Y = U(lambda h: lambda F: F(lambda x: U(h)(F)(x)))
fact = Y(lambda f: lambda n: 1 if n <= 0 else n * f(n-1))
print (fact(7))


Y = (lambda h: lambda F: F(lambda x: h(h)(F)(x)))(lambda h: lambda F: F(lambda x: h(h)(F)(x)))
fact = Y(lambda f: lambda n: 1 if n <= 0 else n * f(n-1))
print (fact(8))

# fact(5) in pur lambda calculus
R1 = (((lambda f: (((f)((lambda f: ((lambda z: (((f)(((f)(((f)(((f)(((f)(z)))))))))))))))))))((((((lambda y: ((lambda F: (((F)((lambda x: (((((((y)(y)))(F)))(x)))))))))))((lambda y: ((lambda F: (((F)((lambda x: (((((((y)(y)))(F)))(x)))))))))))))((lambda f: ((lambda n: ((((((((((((lambda n: (((((n)((lambda _: ((lambda t: ((lambda f: (((f)((lambda void: (void)))))))))))))((lambda t: ((lambda f: (((t)((lambda void: (void)))))))))))))((((((lambda n: ((lambda m: (((((m)((lambda n: ((lambda f: ((lambda z: (((((((n)((lambda g: ((lambda h: (((h)(((g)(f)))))))))))((lambda u: (z)))))((lambda u: (u)))))))))))))(n)))))))(n)))((lambda f: ((lambda z: (z)))))))))((lambda _: ((((lambda n: (((((n)((lambda _: ((lambda t: ((lambda f: (((f)((lambda void: (void)))))))))))))((lambda t: ((lambda f: (((t)((lambda void: (void)))))))))))))((((((lambda n: ((lambda m: (((((m)((lambda n: ((lambda f: ((lambda z: (((((((n)((lambda g: ((lambda h: (((h)(((g)(f)))))))))))((lambda u: (z)))))((lambda u: (u)))))))))))))(n)))))))((lambda f: ((lambda z: (z)))))))(n)))))))))((lambda _: ((lambda t: ((lambda f: (((f)((lambda void: (void)))))))))))))((lambda _: ((lambda f: ((lambda z: (((f)(z)))))))))))((lambda _: ((((((lambda n: ((lambda m: ((lambda f: ((lambda z: (((((m)(((n)(f)))))(z)))))))))))(n)))(((f)((((((lambda n: ((lambda m: (((((m)((lambda n: ((lambda f: ((lambda z: (((((((n)((lambda g: ((lambda h: (((h)(((g)(f)))))))))))((lambda u: (z)))))((lambda u: (u)))))))))))))(n)))))))(n)))((lambda f: ((lambda z: (((f)(z))))))))))))))))))))))))

print (npy(R1))
