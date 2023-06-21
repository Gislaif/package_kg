package_count=0
package_weight=0

items=int(input("Type how many items you would like to ship: "))
for item_number in range(1, items +1):
    print("what is the weight of this item?: ")
    item_weight = int(input())
    if item_weight==0:
        break
    if item_weight>0 and item_weight<=20:
        package_weight=package_weight+item_weight
        if package_weight>=20:
            print("The package is full")
            print("Creating a new package")
            package_count = package_count+1
            package_weight= item_weight
if package_weight>0 and package_weight<=20:
    package_count = package_count + 1
    package_weight = item_weight
    print("total package count:")
    print(package_count)
    print("Kg per package")
    print(item_weight+package_weight)
