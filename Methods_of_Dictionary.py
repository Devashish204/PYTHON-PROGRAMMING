MyDict = {
    "fast" : "In a Quick Manner",
    "Harry" : "A Coder",
    "Marks" : [1,2,5],
    "Another Dict" : {'Dev':'Palyer'},
    1:2
}

#Dictionary Methods

#1 a.key()

print(list(MyDict.keys())) #prints the keys of the dictionary.

#2 a.values()

print(MyDict.values()) #print the values of keys from the dictionary.

#3 a.items()

print(MyDict.items()) #prints the (Key,values) for all contents of the dictionary.

#4 a.update()

print (MyDict)
updateDict = {
    "Reetam" : "Friend",
    "Prathamesh" : "Friend",
    "Parth" : "Friend",
    "Dev" : "Youtuber"
}

MyDict.update(updateDict) #updates the dictionary by adding key_value pair from updateDict.

#5 get()

print(MyDict.get("Dev")) #prints value asscociated with key "Dev".

#The difference between .get and [] syntax in dictionary?


print(MyDict.get("Dev2")) #returns none as Dev2 is not present in the dictionary.

print(MyDict["Harry2"]) #Throws an error as Dev2 is not present in the dictionary. 