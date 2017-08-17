numbersW = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbersW2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
numbersW3 = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
# numbersW4 = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion"]

def convert(first):
    written = ""
    print(first,"is ", end='')
    if first[0] == '-' and int(first) != 0:
        written += "negative"
        first = first[1:]

    # sets = (len(first)-1)/3 + 1
    hanging = len(first) % 3
    if hanging == 0:
        written += numbersW[int(first[0])] + "hundred"
        hanging = 3
    if hanging != 1:
        if first[hanging - 2] == '1':
            written += numbersW2[int(first[hanging - 1])]
        else:
            written += numbersW3[int(first[hanging - 2])] + numbersW[int(first[hanging - 1])]
    else:
        written += numbersW[int(first[0])]
    if (first == '0'):
        written = "zero"
    second = len(written)
    if int(first) != second:
        # print(written, "", end='')
        print(second)
        convert(str(second))
    else:
        print("cosmic")

while True:
    inp = "abc"
    while not ((inp[0] == '-' and inp[1:].isdigit()) or inp.isdigit()):
        inp = input("Enter a number: ")
        if inp == "":
            inp = "abc"
        if inp[0] == '+':
            inp = inp[1:]
        if (inp[0] == '-' and inp[1:].isdigit()) or inp.isdigit():
            if abs(int(inp)) > 999:
                inp = "abc"
    convert(inp)