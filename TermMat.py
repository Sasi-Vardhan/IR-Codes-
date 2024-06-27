#Term-Based Matrix Retrieval 

D1 = "new home top forecast"
D2 = "home sales rise in july"
D3 = "increase in home sales july"
D4 = "july new home sales"

collection=[D1,D2,D3,D4]
#TokenNiZation and Booleans to DocID

tokens=[]
for i in collection:
    tokens.extend(i.split(" "))

Term_Based_Matrix={}

for i in tokens:
    Term_Based_Matrix[i]=[]
    for k in collection:
        if i in k:
            Term_Based_Matrix[i].append(1)
        else:
            Term_Based_Matrix[i].append(0)
def Common(query):
    ans=[]
    process=[]
    query_tokens=query.split(" ")
    total=len(query_tokens)-1
    for i in query_tokens:
        if i != "and":
            process.append(Term_Based_Matrix[i])
    freq={}
    freq[0]=1
    print(process,freq[0])
    for j in range(len(process[0])):
            freq[j]=0
    for i in range(len(process)):
        for j in range(len(process[0])):
            
            if process[i][j]==1:
                if freq[j]==0:
                    freq[j]=1
                else:
                    freq[j]+=1
    print("The retreived Documents are : ")
    for i in freq.keys():
        if freq[i]==total:
            print("DOC'ID' ",i+1)
def All(query):
    ans=[]
    process=[]
    query_tokens=query.split(" ")
    if "or" in query:
        total=len(query_tokens)-1
    else:
        total=len(query_tokens)
    for i in query_tokens:
        if i != "or":
            process.append(Term_Based_Matrix[i])
    freq={}
    freq[0]=1
    for j in range(len(process[0])):
            freq[j]=0
    for i in range(len(process)):
        for j in range(len(process[0])):
            
            if process[i][j]==1:
                if freq[j]==0:
                    freq[j]=1
                else:
                    freq[j]+=1
    print("The retreived Documents are : ")
    for i in freq.keys():
        if freq[i] > 0:
            print("DOC'ID' ",i+1)
def Minus(query):
    ans=[]
    process=[]
    query_tokens=query.split(" ")
    if "not" in query:
        total=len(query_tokens)-1
    else:
        total=len(query_tokens)
    for i in query_tokens:
        if i != "not":
            process.append(Term_Based_Matrix[i])
    freq={}
    k=0
    for i in process[0]:
        if i==1:
            freq[k]=1
        else:
            freq[k]=0
        k+=1
    for i in range(1,len(process)):
        for j in range(len(process[0])):
            
            if process[i][j]==1:
                freq[i]-=1
    print("The retreived Documents are : ")
    for i in freq.keys():
        if freq[i] == 0:
            print("DOC'ID' ",i+1)
if(__name__=="__main__"):

    query="sales not july"
    print("The query is : ",query,"\n")
    query=query.lower()
    
    if "and" in query:
        Common(query)
    elif "or" in query:
        All(query)
    elif "not" in query:
        Minus(query)
    else:
        All(query)
