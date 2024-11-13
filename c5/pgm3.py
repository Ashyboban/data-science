print("23mca030:GEORGE SCARIA")
def gen_ngrams(text,wordsToCombine):
    words=text.split()
    output=[]
    for i in range(len(words)-wordsToCombine+1):
        output.append(words[i:i+wordsToCombine])
    return output
x=gen_ngrams(text='Jimmy Mcnulty,the prodigal Son',wordsToCombine=3)
print(x)
