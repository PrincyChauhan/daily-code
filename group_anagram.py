strs = ["eat","tea","tan","ate","nat","bat"]

from collections import defaultdict
anagrams=defaultdict(list)

for s in strs:
    sorted_s = ''.join(sorted(s))
    print(sorted_s,"---------sorted_s----------")
    
    anagrams[sorted_s].append(s)
    print(anagrams,"---------anagrams----------")
    
print(list(anagrams.values()))    