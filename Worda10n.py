# this solutions is wrong.Check'ads sdssds'.

def abbreviate(s):
    word = [-1]
    abb = ''
    for i in range(len(s)):
        if s[i].upper() == s[i].lower():
            word.append(i)
    if word == [-1]:
        return s[0]+str(len(s)-2)+s[len(s)-1]
    for i in range(1,len(word)):
        if word[i] - word[i-1] == 1:
            abb += s[word[i]]
        elif  word[i] - word[i-1] < 5 and word[i] - word[i-1] > 1:
            abb += s[(word[i-1]+1):(word[i]+1)] 
        else :
            abb += s[word[i-1]+1]
            abb += str(word[i] - word[i-1] - 3)
            abb += s[word[i]-1]    
            abb += s[word[i]] 
    return abb
