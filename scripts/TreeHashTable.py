import csv
from collections import defaultdict
MAX_CHILDREN = 6
CSV_COLUMNS = ['Parent', 'Child 1', 'Child 2',	'Child 3', 'Child 4', 'Child 5', 'Child 6']
HASH_OUTPUT_COLUMNS = ['ID', 'Name']
IMAGE_PARSING_COLUMNS = ['Word Name', 'Icon File Name'];

def CSVtoHash(newHash):

    if newHash == 1:
        filename = 'Tree.csv'
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            hash = {}
            i = 0
            for row in reader:
                hash[i] = row[CSV_COLUMNS[0]]
                childIds = getChildIds(i)
                # print (childIds, " >>> ", i)
                for j in range(MAX_CHILDREN):
                    hash[childIds[j]] = row[CSV_COLUMNS[j + 1]]
                i = i + 1
    elif newHash == 2:
        filename = 'ImageParsing.csv'
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            hash = {}
            for row in reader:
                hash[row[IMAGE_PARSING_COLUMNS[0]]] = row[IMAGE_PARSING_COLUMNS[1]]
    else:
        filename = 'Hash.csv'
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            hash = {}
            for row in reader:
               # print(row)
                hash[row[HASH_OUTPUT_COLUMNS[0]]] = row[HASH_OUTPUT_COLUMNS[1]]
    return hash

def HashtoCSV(filename, hash):
    writer = csv.writer(open(filename, "w"))
    writer.writerow(HASH_OUTPUT_COLUMNS)
    for key, val in hash.items():
        writer.writerow([key, val])
    return

def getChildIds(parentId):
    childIds = [None] * MAX_CHILDREN # empty list
    relativeChildId = 1 + parentId * MAX_CHILDREN
    for i in range(MAX_CHILDREN):
        childIds[i] = relativeChildId + i # offset
    return childIds

def getChildNames(parentId, hash):
    names = [None] * MAX_CHILDREN # empty list
    childIds = getChildIds(parentId)
    for i in range(MAX_CHILDREN):
        names[i] = hash[childIds[i]]
    return names

def getUniqueWords(hash):
    words = {}
    i = 0
    for key, val in hash.items():
        words[val] = "" # nothing
    return words

def main():

    hash = CSVtoHash(1)
    HashtoCSV("Hash.csv", hash)
    words = getUniqueWords(hash)
    HashtoCSV("Unique_Words.csv", words)
    images = CSVtoHash(2)
    return

if __name__ == '__main__':
    main()

print('one giant red bean')
