# Importing classes from animals package
from Animals import Mammals
from Animals import Birds
from Animals import Reptiles


# Creating an object of mammals
myMammal = Mammals()
myMammal.printMembers()

# Creating an object of Birds
myBird = Birds()
myBird.printMembers()

#Creating reptile object
myReptile = Reptiles()
myReptile.printMembers()

#checking to see if we can append to list
test1 = Mammals()
test1.members.append("Lion")

test1.printMembers()
