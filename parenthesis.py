n = 3

def paranthesis(n,parenth="(", total1=1, total2=0):
        if total1==total2==n:
            print(parenth)
        parenth1 = parenth + "("
        total3 = total1 +1
        if total2<=total3 and total3<=n:
            paranthesis(n, parenth1,total3,total2)
        parenth2  = parenth + ")"
        total4 = total2+1
        if total4<=total1 and total1<=n:
            paranthesis(n, parenth2,total1,total4)

paranthesis(n)  