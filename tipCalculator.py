a=float(input("what is total amount of the bill ? $"))
b=float(input("what is percentage of the tip you want to give ? "))
c=int(input("how many are there to split the bill ?"))

bill=a+a*(b/100)
# perHead=round(bill/c,2)

# format function
perHead="{:.2f}".format(bill/c)
print(f"bill per person is : ${perHead}")

# what is total amount of the bill ? $150
# what is percentage of the tip you want to give ? 12
# how many are there to split the bill ?5
# bill per person is : $33.60