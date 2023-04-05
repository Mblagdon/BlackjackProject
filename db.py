# a module to read and write the money
# add exception handling into main program
def readMoney():
    with open("money.txt", "r") as file:
        money = float(file.read().strip())
    return money

def writeMoney(money):
    with open("money.txt", "w") as file:
        file.write("{:.2f}".format(money))
