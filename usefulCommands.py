from __future__ import division
import math as m
import random
from Helper import color

def Calc(calc,sender):
    calc = calc.lower()
    lbs = calc.count('(')
    rbs = calc.count(')')
    if lbs > 0 and rbs > 0:
        c=0
        for i in calc:
            if i == '(':
                c+=1
            elif i == ')':
                c-=1
            if c<0:
                return None
        if c>0:
            return None
    
    wlist = '0123456789*+-/^|&~.,() '
    calc = calc.replace('[pi]',''.join(['(',str(m.pi),')']))
    calc = calc.replace('[e]',''.join(['(',str(m.e),')']))
    calc = calc.replace('abs(','fabs(')
    calc = calc.replace('deg(','degrees(')
    calc = calc.replace('rad(','radians(')
    calc = calc.replace('rand()','random()')
    calc = calc.replace('^','**')
    calc = calc.replace(' xor ','^')
    calc = calc.replace(' and ','&')
    calc = calc.replace(' or ','|')
    calc = calc.replace('not ','~')

    funcs = ['cos','sin','tan','acos','asin','atan','sqrt','acosh','asinh','atanh','cosh','sinh','tanh','ceil','floor','fabs','gamma','lgamma','degrees','radians','log']
    calc2=calc
    for j in funcs:
        i=j+'('
        calc = calc.replace(i,'(')
        calc2= calc2.replace(i,'m.'+i)

    rfuncs = ['random','randint','uniform','randrange']
    for j in rfuncs:
        i=j+'('
        calc = calc.replace(i,'(')
        calc2= calc2.replace(i,'random.'+i)
    
    for i in calc:
        if not i in wlist:
            sender.sendMessage(''.join(["The character ",i," is not allowed! Allowed characters: ",wlist]))
            return ValueError

    try:
        q = eval(calc2)
    except:
        return None
    return q

@hook.command("calc", description="Calculate things!")
def onCommandCalc(sender,args):
    if len(args)==0:
        sender.sendMessage('This function requires an expression to calculate!')
        return False
    c=Calc(' '.join(args),sender)

    if c==None:
        sender.sendMessage('Invalid expression!')
        return False
    elif c==ValueError:
        return False
    a = list(' '.join(args))
    n = '0123456789.'
    c = 7
    i = 2
    while i < len(a):
        j=a[i:i+1]
        if c==7 and (j in n):
            a = ''.join([a[:i],color(3),a[i:]])
            i+=2
            c=3
        if c==3 and not (j in n):
            a = ''.join([a[:i],color(7),a[i:]])
            i+=2
            c=7
        i+=1
    sender.sendMessage(''.join([color('7'),''.join(a),color('f')," = ",color('e'),str(c)]))
    return True 
