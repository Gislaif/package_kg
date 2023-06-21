package_count=0
package_weight=0
total_weight=0
package_number=0
max_unused_capacity=0

items=int(input("Type how many items you would like to ship: "))
for item_number in range(1, items +1):
    print("what is the weight of this item?: ")
    item_weight = int(input())
    if item_weight==0:
        break
    if item_weight>0 and item_weight<=10:
        package_weight=package_weight+item_weight
        total_weight=item_weight+total_weight
        if package_weight>20:
            print("The package is full")
            print("Creating a new package")
            unused_capacity=20-package_weight+item_weight
            print("unused capacity of this package is: ", unused_capacity)
            package_count = package_count + 1
            if unused_capacity>max_unused_capacity:
                max_unused_capacity=unused_capacity
                package_number=package_count
            package_weight= item_weight
    else:
        print("Item weight is not correct")
        continue
if package_weight>0 and package_weight<=20:
    unused_capacity = 20 - package_weight
    print("unused capacity of this package is: ", unused_capacity)
    package_count = package_count + 1
    if unused_capacity > max_unused_capacity:
        max_unused_capacity = unused_capacity
        package_number = package_count
    package_weight = item_weight
    print("total package count:")
    print(package_count)
    print("Total weight of packages")
    print(total_weight)
    print("Total unused capacity")
    print(20*package_count-total_weight)
    print("Package is the most used capacity:" , package_number)
    print("The most unused capacity in package: ", max_unused_capacity)