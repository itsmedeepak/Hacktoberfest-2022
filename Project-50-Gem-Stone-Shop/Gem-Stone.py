gems=("Emerald", "Ivory", "Jasper", "Ruby", "Garnet")
price=(1760, 2119, 1599, 3920, 3999)
total=0
n=int(input("Number different gems you want to buy: "))
for i in range(n):
    gem=str(input("Enter gem name: "))
    if(gem in gems):
        qty=int(input("Enter quantity: "))
        total+=price[gems.index(gem)]*qty
    else:
        print("Gem not found!")
        total=-1
        break
    print()

print("Total Bill:",total)

if(total>30000):
    print("\nDiscount Applied: 5%")
    total*=0.95
    print("Final Bill:",total)
