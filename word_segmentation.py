import io

# Read input file
#fin = io.open("input1.txt", mode='r', encoding='utf-8')
#text = fin.readlines()

# Read Vdic dataset
fin = io.open("VDic_uni.txt", mode='r', encoding='utf-8')
vdic_uni = fin.readlines()
#print(vdic_uni)

# Create a list vdic
vdic = []
for i in range(len(vdic_uni)):
    tab_index = vdic_uni[i].find('\t')
    vdic.append(vdic_uni[i][:tab_index])

# Split paragraph into sentences
#paragraphs = []
#for p in text:
#    paragraphs.append([])
#    paragraphs[-1] = p.split('.')

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

sentence = "Ngày chủ nhật bố mẹ vắng nhà"
print(lrmm(sentence))