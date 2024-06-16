browser= (input("Enter the browser name:"))
browser = browser.lower()
match browser:
    case "chrome":
        print("execute the code of chrome browser")
    case "firefox":
        print("execute the code of firefox browser")

    case "safari":
        print("execute the code of safari browser")

    case "opera":
        print("execute the code of opera browser")

    case _:
        print("no idea")