nums=[4,-5,10,12,65,-23]
doubled = []
for num in nums:
    doubled.append(num * 2)
    print(doubled)

    #
    nums=[4,-5,10,12,65,-23]
    doubled = [num *2 for num in nums]
    print (doubled)

    fruits = ['apple','banana', 'cherry','Kiwi','Mango']
    newlist=[x for x in fruits if 'a' in x]
    print(newlist)






#date and time code
    import datetime
    X = datetime.datetime.now()
    print(X)


