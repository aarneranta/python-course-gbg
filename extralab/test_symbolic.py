from symbolic import *

errors = 0

def tests(exp,expected):
    global errors
    try:
        received = eval(exp)
        if expected != received:
            print(exp, ":", "expected", expected, "received", received)
            errors += 1
    except:
        print(exp, ":", "failed")
        errors += 1

# normalize spacing: put space between all tokens
def unlex(s):
    return ' '.join(lex(s))
        
def print_errors(e,part):
    if e == 0:
        print("PART",part, "OK")
    elif e == 1:
        print(e, "ERROR IN PART", part)
    else:
        print(e, "ERRORS IN PART", part)

print("TESTING PART 1")

tests("deriv_polynom([1,2,3,4])", [2,6,12])

tests("mul(5,6).op", "*")
tests("sub(5,6).op", "-")
tests("pow(5,6).op", "^")

tests("var().op", "x")
tests("var().args", [])

tests("const(666).op", 666)
tests("const(666).args", [])

binom1 = sub(var(),const(1))
binom2 = mul(binom1,binom1)
binom3 = pow(binom1,const(3))
binom4 = pow(binom2,const(2))
binom5 = mul(binom4,binom1)
binom6 = mul(binom2,(mul(binom2,binom2)))

tests("show_exp_prefix(derivative(var()))", "1")
tests("show_exp_prefix(derivative(div(const(3),var())))", "(/ (- (* 0 x) (* 3 1)) (* x x))")
tests("show_exp_prefix(derivative(binom1))", "(- 1 0)")

tests("exp2polynom(binom1)",[-1,1])
tests("exp2polynom(binom2)",[1,-2,1])
tests("exp2polynom(binom3)",[-1,3,-3,1])
tests("exp2polynom(binom4)",[1,-4,6,-4,1])
tests("exp2polynom(binom5)",[-1, 5, -10, 10, -5, 1])
tests("exp2polynom(binom6)",[1, -6, 15, -20, 15, -6, 1])

tests("deriv_polynom(exp2polynom(binom6))", [-6, 30, -60, 60, -30, 6])
tests("exp2polynom(derivative(binom6))", [-6, 30, -60, 60, -30, 6])

print_errors(errors,1)
errors = 0

print("TESTING PART 2")

tests("show_exp_infix(0,add(var(),const(44)))","x + 44")
tests("show_exp_infix(0,add(const(2),mul(var(),const(3))))","2 + x * 3")
tests("show_exp_infix(0,mul(add(const(2),var()),const(3)))","(2 + x) * 3")
tests("show_exp_infix(0,binom4)","((x - 1) * (x - 1)) ^ 2")
tests("show_polynom([])","0")
tests("show_polynom([1,2])","1 + 2x")
tests("show_polynom([0,1])","x")
tests("unlex(show_polynom([0,0,-1]))", unlex("- x^2"))
tests("show_polynom([2,-3,5])","2 - 3x + 5x^2")
tests("show_polynom([-1, 5, -10, 10, -5, 0, -1])","-1 + 5x - 10x^2 + 10x^3 - 5x^4 - x^6")


print_errors(errors,2)






