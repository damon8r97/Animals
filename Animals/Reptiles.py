class Reptiles:
    def __init__(self):
        ''' Constructor for the Reptiles '''

        self.members = ['Lizard', 'Snake', 'Turtle']


    def printMembers(self):
        print('Printing members of the Reptiles class')
        for member in self.members:
            print('\t%s ' % member)
