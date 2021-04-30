class Mammals:

    def get_mammals(self):
        return ['Tiger', 'Elephant', 'Wild Cat']


    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.get_mammals():
            print('\t%s ' % member)
