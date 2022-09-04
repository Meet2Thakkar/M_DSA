hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0
    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

def getPrime(n):
    if n % 2 == 0:
        n += 1

    while not checkPrime(n):
        n += 2

    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key, data):
    index = hashFunction(key)
    hashTable[index] = 0


insertData(123, 'apple')
insertData(423, 'banana')
insertData(333, 'lichi')
#insertData(453, 'pomogranate')
#insertData(469, 'watermelon')
#insertData(523, 'mango')
#insertData(553, 'sitafal')
#insertData(243, 'rasberry')
#insertData(823, 'guava')
#insertData(723, 'pineapple')

print(hashTable)