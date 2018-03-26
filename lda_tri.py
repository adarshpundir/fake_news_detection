def ngrams(s, n=2, i=0):
        while len(s[i:i+n]) == n:
            yield s[i:i+n]
            i += 1
	
file=open('/home/dead/Desktop/pr/dead.txt')
text=file.readline();

trigram = ngrams(text.split(), n=3)
print(list(trigram))
print()
