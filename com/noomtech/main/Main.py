from com.noomtech.consumables.foods import Meat, Vegetable
from com.noomtech.consuming.Mouth import Mouth
from time import sleep

"""Test to make sure that different foods can be chewed in different amounts of time"""

if __name__ == "__main__":

    meat1 = Meat()
    vegetable1 = Vegetable()
    meat2 = Meat()
    vegetable2 = Vegetable()
    meat3 = Meat()
    vegetable3 = Vegetable()
    meat4 = Meat()
    vegetable4 = Vegetable()
    meat5 = Meat()
    vegetable5 = Vegetable()
    meat6 = Meat()
    vegetable6 = Vegetable()

    mouth = Mouth();
    mouth.start()

    mouth.add(meat1)
    mouth.add(vegetable1)

    sleep(1)

    mouth.add(meat2)
    mouth.add(vegetable2)

    sleep(1)

    mouth.add(meat3)
    mouth.add(vegetable3)

    sleep(1)

    mouth.add(meat4)
    mouth.add(vegetable4)

    sleep(1)
