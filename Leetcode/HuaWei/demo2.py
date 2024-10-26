
from decimal import Decimal
def fun(str):
    lines=str.split(" ")
    wei_words=0
    for word in lines:
        wei_words=wei_words+len(word)
    weight_entir0=Decimal(wei_words/len(lines))
    weight_entir="{:.2f}".format(weight_entir0)
    print(weight_entir)
    return weight_entir
if __name__ == "__main__":
    str="demo demo"
    print(fun(str))