def check_world(i: int, corrected: str):
    global string
    global starts
    if i >= len(starts) - 1:
        if corrected in dic:
            string = corrected
        return string
    if starts[i + 1] - starts[i] > 1:
        check_world(i + 1, corrected + str(w[starts[i]]) + str(w[starts[i]]))
    check_world(i + 1, corrected + str(w[starts[i]]))
    return string


with open('words.txt', "r") as f:
    dic = set(f.read().split())
    print("Program starts. Type _exit_ to close.")
    while True:
        string = ""
        temp = str(input("Input word: "))
        if temp == "_exit_":
            break
        w = "  " + temp + "  "
        starts = [i for i, c in list(enumerate(w))[2:] if c != w[i - 1]]
        if check_world(0, "") == "":
            print("There is no such word as", w, "\n")
        else:
            print("There is similar word as", string, "\n")
