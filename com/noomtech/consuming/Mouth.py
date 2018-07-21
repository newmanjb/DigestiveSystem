from com.noomtech.building_blocks.BuildingBlocks import Producer
from threading import Thread
from com.noomtech.consumables.building_blocks import FoodState
from time import sleep


class Mouth(Producer) :

    """Accepts food, chews it and passes the chewed food onwards
    """

    
#todo -- add synchronization to multithreaded functionality

    
    def __init__(self):
        self.capactiy = 10
        self.beingChewed = []

    def start(self):
        self.alive = True
        swallowThread = Thread(target=self.swallow, daemon=False, name="Swallow Thread")
        swallowThread.start()

    def stop(self):
        self.alive = False

    def add(self, food):
        """Submit a unit of food to be chewed and swallowed"""

        if(len(self.beingChewed) == 10) :
            return food
        self.beingChewed.append(food)
        chewThread = Thread(target=self.chew,daemon=False,args=(food,))
        chewThread.start()

    def deliverProduce(self,transportableList):
        [print("Swallowing " + str(x)) for x in transportableList]
        self.receiver.receive(transportableList)

    def chew(self, food):
        food.chew()
        self.beingChewed.remove(food)
        #The food is now chewed so it can go to the front of the list
        self.beingChewed.insert(0,food)
        print("Chewed " + str(food))

    """Deliver any chewed food to the next stage"""
    def swallow(self):
        while self.alive:
            """All chewed food should be at the front of the list"""
            beingChewed = self.beingChewed
            transportableList = []
            for idx, food in enumerate(beingChewed):
                if food.state == FoodState.CHEWED:
                    transportableList.append(beingChewed.pop(idx))
                else :
                    break;

            if len(transportableList) > 0:
                self.deliverProduce(transportableList)

            sleep(2)
