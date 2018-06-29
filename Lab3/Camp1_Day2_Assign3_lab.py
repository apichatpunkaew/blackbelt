import json

def getNumberfromJsonFile():
    file = open("ListNumber.json", "r") 
    data = json.load(file)
    StrSequence = data["sequence"]
    TempSequence = StrSequence.split(",")
    TempSequence = [x.strip(' ') for x in TempSequence]
    return TempSequence

if __name__ == '__main__':
    EvenNumber = []
    NumberSequence = getNumberfromJsonFile()
    for i in range(len(NumberSequence)):
        ##print(NumberSequence[i])
        if(int(NumberSequence[i]) % 2 == 0):
            ##print (NumberSequence[i])
            EvenNumber.append(NumberSequence[i])
    ##print(EvenNumber)
    str1 = ', '.join(EvenNumber)
    print ("The even numbers are "+str1)
    
