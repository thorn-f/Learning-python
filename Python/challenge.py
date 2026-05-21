print("Hello world hello")

def wordnum():
    text = "Hello world hello"
    hellonum = text.lower().count("hello")
    worldnum = text.lower().count("world")
    print("The number of times 'hello' appears is:", hellonum)
    print("The number of times 'world' appears is:", worldnum)


wordnum()