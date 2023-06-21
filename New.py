package_count=0
package_weight=0

for item_number in range(4):
    print("weight of an item")
    item_weight = int(input())
    if item_weight==0:
        break
    if item_weight>0 and item_weight<=20:
        package_weight=package_weight+item_weight
        if package_weight>20:
            package_count = package_count+1
            package_weight= item_weight
if package_weight>0 and package_weight<=20:
    package_count = package_count + 1
    package_weight = item_weight
print("total package count:")
print(package_count)
print("Kg per package")
print(item_weight+package_weight)
