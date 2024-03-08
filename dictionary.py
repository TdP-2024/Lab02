import re
class Dictionary:
    def __init__(self, dict={}):
        self._dict = dict


    def addWord(self,key_value):
        if len(key_value) == 2:
            if key_value[0] not in self._dict:
                self._dict[key_value[0]] = key_value[1]
            else:
                prevVal = self._dict.get(key_value[0])
                if isinstance(prevVal, str):
                    currentVal = []
                    currentVal.append(prevVal)
                else:  currentVal = self._dict.get(key_value[0])
                print(currentVal)
                self._dict[key_value[0]] = [*currentVal, key_value[1]]
                print(self._dict[key_value[0]])



    def translate(self, key):
        return self._dict[key]

    def translateWordWildCard(self, wildCard):
        # Replace "?" with "." to use regex
        wildCard = wildCard.replace("?", ".")
        print(wildCard)
        matchCounter = 0
        sb = []

        for w in self._dict.keys():
            # Use regex matching for "alienWord" with the modified wild card
            if re.search(wildCard,w):
                matchCounter += 1
                sb.append(self._dict.get(w))

        # Return concatenated translations if there are matches
        if matchCounter != 0:
            return sb
        else:
            return None

    def loadDictionary(self):
        file_path = 'dictionary.txt'

        with open(file_path, 'r') as file:
            for line in file:
                key_value = line.strip().split()
                if len(key_value) == 2:
                    self._dict[key_value[0]] = key_value[1]
        # print(self._dict)

    def printAll(self):
        for key, value in self._dict.items():
            # Assuming getAlienWord and getTranslations are methods to access object properties
            alienWord = key
            translations = value
            print(f"Alien Word: {alienWord}, Translations: {translations}\n")

