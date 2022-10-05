# coding problem scrumburger 
def Anagram(s,t):
    s=s.lower()
    t=t.lower()
    if len(s)!=len(t):
        print(0)
        return

    l=[];ll=[]
    for i in range(len(s)):
        l.append(ord(s[i]))
        ll.append(ord(t[i]))
    l.sort();ll.sort()
    if(l==ll):
        print(1)
        return
    else:
        print(0)
        return


def main():
    c=input("")
    d=input("")
    Anagram(c,d)

main()