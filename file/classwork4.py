# 4
f = open('/home/azim/python/texxt.txt', 'r')
t_words=[]
a = f.read()
a = a.split()
for i in a:
    if "t" in i.lower():
        t_words.append(i)
print(t_words)