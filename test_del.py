def longestprefix(a,b):

    leng= min(len(a),len(b))
    print leng

    for i in range(leng):

        if a[i] != b[i]:

            return i

    return leng

x= "Nilgoon"
y="Nilgo"
print longestprefix(x,y)