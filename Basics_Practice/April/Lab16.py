browser =  str(input("Enter code executed\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print(" chrome code executed!")
    case "firefox":
        print(" firefox code executed!!")
    case _:
        print(" No browser found !!")

