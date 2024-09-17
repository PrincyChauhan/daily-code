import json
def getJSONDiff(json1,json2):
    dict1=json.loads(json1)
    print("dict1....",dict1)
    
    dict2=json.loads(json2)
    print("dict2....",dict2)
    
    common_key=set(dict1.keys()) & set(dict2.keys())
    print("common_key....",common_key)
    
    different_key=[]
    for key in common_key:
        if dict1[key]!=dict2[key]:
            different_key.append(key)
    different_key.sort()
    
    return different_key
json1 = '{"name":"Alice","age":30,"city":"New York"}'
json2 = '{"name":"Alice","age":25,"city":"San Francisco"}'


print(getJSONDiff(json1, json2))    