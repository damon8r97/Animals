class Reptiles:

    def get_Reptiles(self):
        return ['Lizard', 'Snake', 'Turtle']


    def printMembers(self):
        print('Printing members of the Reptiles class')
        for member in self.MEMBERS:
            print('\t%s ' % member)
