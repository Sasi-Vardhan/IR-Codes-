D1 = "new home top forecast"
D2 = "home sales rise in july"
D3 = "increase in home sales july"
D4 = "july new home sales"

collection=[D1,D2,D3,D4]
Index={}
Buffer_seen={}
class Node:
    def __init__(self,data):
        self.DocId=data
        self.next=None
def Saw(string,Id):
    tokens=string.split(" ")
    for i in tokens:
        if i not in Index:
            c=Node(Id)
            Index[i]=c
        else:
            c=Index[i]
            while(c.next != None):
                c=c.next
            cs=Node(Id)
            c.next=cs
def Print(node):
    c=Index[node]
    print(node," : ",end=" ")
    while(c):
        print(c.DocId," - > " ,end=" ")
        c=c.next
    print()
def Process_Query(String):
  tokens=String.split(" ")
  L=["and","or","not"]
  for i in tokens:
      if(i not in L):
        Buffer_seen[i]=[]
        if i in Index:
          c=Index[i]
          while(c):
            Buffer_seen[i].append(c.DocId)
            c=c.next
      
def Common(string):
    length=len(Buffer_seen)
    ans={}
    for i in Buffer_seen.values():
        for j in i:
            if j in ans:
                ans[j]+=1
            else:
                ans[j]=1
    for i in ans.keys():
        if ans[i]==length:
            print("DocId :",i)

def All(query):
    ans={}
    for i in Buffer_seen.values():
        for j in i:
            if j in ans:
                ans[j]+=1
            else:
                ans[j]=1
    for i in ans.keys():
        if ans[i] > 0:
            print("DocId :",i)
            
def Minus(query):
    ans=list(Buffer_seen.values())
    res={}
    for i in ans[0]:
        if i in ans[1]:
            continue
        else:
            print("DocId :",i)
if(__name__=="__main__"):
    for i in range(len(collection)):
        Saw(collection[i],i+1)
    # for i in Index.keys():
    #     Print(i)
    #     print()
    Buffer_seen.clear()
    query=input("Enter Your Query []")
    Process_Query(query)
    print("The query is : ",query,"\n")
    query=query.lower()
    
    q=query.split(" ")
    if "and" in q:
        Common(query)
    elif "or" in q:
        All(query)
    elif "not" in q:
        Minus(query)
    else:
        All(query)
