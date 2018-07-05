from com.noomtech.consumables.building_blocks.BuildingBlocks import Food

"""The different types of food"""

class Meat(Food) :

    def __init__(self):
        Food.__init__(self)
        self.chewTime = 7
        self.digestTime = 9

    def preDigest(self):
        pass

    def postDigest(self):
        pass

class Vegetable(Food):

    def __init__(self):
        Food.__init__(self)
        self.chewTime = 3
        self.digestTime = 5

    def preDigest(self):
        pass

    def postDigest(self):
        pass