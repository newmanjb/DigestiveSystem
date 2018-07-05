from com.noomtech.consumables.foods import Meat, Vegetable

"""Test to make sure that different foods can be chewed in different amounts of time"""

if __name__ == "__main__":

    meat = Meat()
    vegetable = Vegetable()

    print(meat.state)
    print(vegetable.state)
    meat.chew()
    vegetable.chew()
    print(meat.state)
    print(vegetable.state)