class Birds:

    def get_birds(self):
        return ['Sparrow', 'Robin', 'Duck']


    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.MEMBERS:
           print('\t%s ' % member)
