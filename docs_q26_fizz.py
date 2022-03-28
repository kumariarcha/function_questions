def fizzbuzz():
    i=1
    while i<=100:
        if i%3==0:
            print("fizz")
        if i%5==0:
            print("buzz")
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        else:
            print(i)
        i=i+1
fizzbuzz()