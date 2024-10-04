try:
    value = int(input("please give me a number: "))
    print(f"{value} fele az {value/2}")
except:
    print("this is not working")


try:
    value = int(input("I need a number: "))
    print(f"{value} reciproka {1/value}")
except ValueError:
    print("this is not working")
except ZeroDivisionError:
    print("Did you try osztani with 0???")
except:
    print("I don't know what happened")


#talking abaout debugging and breakpoints