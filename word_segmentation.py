#import io

# Read Vdic dataset
with open("VDic_uni.txt", mode='r', encoding='utf-8') as fin:
    vdic_uni = fin.readlines()

# Create a list vdic
vdic = []
for i in range(len(vdic_uni)):
    tab_index = vdic_uni[i].find('\t')
    vdic.append(vdic_uni[i][:tab_index])

# Read input file
with open("input.txt", mode='r', encoding='utf-8') as fin:
    passage = fin.readlines()

# Split paragraph into sentences
paragraphs = [] # contain sentences
for p in passage:
    paragraphs.append([])
    paragraphs[-1] = p.split('.')
    for i in range(len(paragraphs[-1])):
        paragraphs[-1][i] = paragraphs[-1][i].strip() # Remove leading and trailing whitespaces
    if paragraphs[-1][-1] == '': # Enter character which was already stripped
        paragraphs[-1].pop()

for pr in paragraphs:
    print(pr)

def lrmm(sentence):
    chwx = sentence.split(' ')
    words = []
    i = 0
    while i < len(chwx):
        word_found = False
        for c in [3, 2, 1]: # The number of chwx of a word
            if i + c - 1 < len(chwx):
                if c > 1:
                    temp_word = ' '.join(chwx[i:i+c])
                    if temp_word in vdic:
                        word_found = True
                        words.append('_'.join(chwx[i:i+c]))
                        i += c 
                        break
                elif c == 1:
                    if chwx[i] in vdic:
                        word_found = True
                        words.append(chwx[i])
                        i += c
                        break
        if word_found == False:
            words.append(chwx[i])
            i += 1
    return words

sentence = "Em bước sang ngang đợi chờ một điều diệu kì"
print(lrmm(sentence))