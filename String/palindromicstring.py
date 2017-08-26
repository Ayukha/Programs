# cook your dish here
2
def check_palin(word):
    for i in range(len(word)//2):
        if word[i] != word[-1*(i+1)]:
            return False
    return True

def all_palindromes(Word):

    left,right=0,len(Word)
    j=right
    results=[]

    while left < right-1:
        temp = Word[left:j]
        j-=1

        if check_palin(temp):
            results.append(temp)

        if j<left+2:
            left+=1
            j=right

    return list(set(results))

def main():
    res=[]
    for i in range(int(input())):
        word1=input()
        if all_palindromes(word1):
            res.append("YES")
        else:
            res.append("NO")
    for j in range(len(res)):
        print(res[j])

main()