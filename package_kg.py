print("Type a product kg")
kg_count=0
productkg = float(input())

while productkg<=20:
    print("enter with one more product")
    if productkg>20:
        break
    elif productkg<20:
        print (productkg)
        kg_new = float(input())
        if kg_new <20:
            print(productkg+kg_new)
        else:
            print("kg exceeded")
            break