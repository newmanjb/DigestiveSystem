from com.noomtech.building_blocks import Receiver, Producer
from com.noomtech.consumables.building_blocks import FoodState
from time import sleep
from threading import Thread

class Stomach(Receiver,Producer):

    """Represents the stomach.  Receives food and breaks it down before passing it on to the next stage"""


    def __init__(self):
        self.capacity = 300;
        #holds the food
        self.content = []

    def start(self):
        self.isAlive = True

    def stop(self):
        self.isAlive = False

    def receive(self, transportableList):
        if len(self.content == self.capacity) :
            #throw the food back up if we've eaten too much
            raise PukeError(transportableList)

        for food in transportableList:
            self.content.append(food)
            Thread(target=self.digest,daemon=False,name="Digest Thread",kwargs=food).start()

    def deliverProduce(self,transportable):
        pass

    def digest(self, food):
        food.digest()
        #move newly broken-down food to the front of the list
        self.content.insert(0, self.content.remove(food))

    def passDigestedFoodForward(self):

        #passes all broken down food to the next stage

        while self.isAlive :
            content = self.content
            brokenDownFood = []
            for idx, food in enumerate(content):
                if food.state == FoodState.BROKEN_DOWN:
                    brokenDownFood.append(content.pop(idx))
                elif len(brokenDownFood) > 0:
                    self.deliverProduce(brokenDownFood)
                    break

            sleep(2)

class PukeError(Exception):
    """Raised when the stomach needs to regurgitate food"""
    def __init__(self,puke):
        self.message = "Heeuuuuurrrgggghhhhhhhhh!";
        self.puke = puke