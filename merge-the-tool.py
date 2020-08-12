#problem here -> https://www.hackerrank.com/challenges/merge-the-tools

def merge_the_tools(string, k):
 for i in range(0, len(string), k):
    s = ""
    for j in string[i : i + k]:
        if j in s:
            continue
        else:
            s += j          
    print(s)
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    
