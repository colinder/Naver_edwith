counts= dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

#.  counts[name] = counts.get(names, 0) + 1  이걸 4줄로 표현하면,
#.    if name not in counts :
#.        counts[name] = 1
#.    else :
#.        counts[name] = counts[name] + 1
#. print(counts)
