from collections import defaultdict

class ListNode:
    def __init__(self, DOC):
        self.DOC = DOC
        self.next = None

Seen = defaultdict(lambda: ListNode(0))
Found = defaultdict(int)

def clower(s):
    ans = ""
    for c in s:
        if c == ' ':
            ans += " "
        elif 97 <= ord(c) <= 123:
            ans += c
        else:
            ans += chr(ord(c) + 32)
    return ans

def AddTerm(first, val):
    Buffer = ListNode(val)
    if first is None:
        return Buffer
    else:
        temp = first
        while temp.next:
            temp = temp.next
        temp.next = Buffer
    return first

def Saw(s, D):
    ans = ""
    for c in s:
        if c == ' ':
            Seen[ans].next = AddTerm(Seen[ans].next, D)
            ans = ""
        else:
            ans += c
    Seen[ans].next = AddTerm(Seen[ans].next, D)

def Count(first):
    temp = first
    while temp:
        Found[temp.DOC] += 1
        temp = temp.next

def Find_Common(n):
    if n == 0:
        print("No Results are found :( ")
        return
    print("The Document is present in:", end=" ")
    for doc, count in Found.items():
        if count == n:
            print(f"DOC {doc} and", end=" ")

def Find_all(n):
    if n == 0:
        print("No Results are found :( ")
        return
    print("The Document is present in:", end=" ")
    for doc, count in Found.items():
        if count > 0:
            print(f"DOC {doc} and", end=" ")

if __name__=="__main__":
    D1 = "new home top forecast "
    D2 = "home sales rise in july "
    D3 = "increase in home sales july "
    D4 = "july new home sales "
    Saw(D1, 1)
    Saw(D2, 2)
    Saw(D3, 3)
    Saw(D4, 4)

    query = input("Enter Query: ")
    print("------------------------------------------")

    ans = ""
    flag = 0
    l = 0
    for c in query:
        if c == ' ':
            if ans == "and":
                ans = ""
                flag = 1
                continue
            print(ans)
            if Seen[ans].next:
                Count(Seen[ans].next)
                l += 1
            ans = ""
        else:
            ans += c

    if Seen[ans].next:
        print(ans)
        Count(Seen[ans].next)
        l += 1

    if flag == 1:
        Find_Common(l)
    else:
        Find_all(l)
