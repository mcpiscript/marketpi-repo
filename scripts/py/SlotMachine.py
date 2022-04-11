## Slot machine
## Created by - tcoy
## 3/6/13
## You have rights to modify this but give credit to tcoy

import minecraft as minecraft
import random
import time

mc = minecraft.Minecraft.create()
plrpos = mc.player.getTilePos()


def play():

    ##slot machine graphics------------------------------------------
    bidlist = []
    for x in xrange(
        10
    ):  ##Generate 10 random ids that will be used for the block graphics
        rand = random.randint(1, 3)
        bid = 0

        if rand == 1:
            bid = 41
        if rand == 2:
            bid = 42
        if rand == 3:
            bid = 57

        bidlist.append(bid)  ##Add the id to the list

    for x in xrange(
        3
    ):  ##Begin to place blocks with a random id -- Read up on lists if you do not know what append or pop does
        mc.setBlocks(
            plrpos.x,
            plrpos.y + 1,
            plrpos.z - 1,
            plrpos.x,
            plrpos.y + 1,
            plrpos.z - 1,
            float(bidlist.pop(0)),
        )
        time.sleep(0.5)
        mc.setBlocks(
            plrpos.x - 2,
            plrpos.y + 1,
            plrpos.z - 1,
            plrpos.x - 2,
            plrpos.y + 1,
            plrpos.z - 1,
            float(bidlist.pop(0)),
        )
        time.sleep(0.5)
        mc.setBlocks(
            plrpos.x + 2,
            plrpos.y + 1,
            plrpos.z - 1,
            plrpos.x + 2,
            plrpos.y + 1,
            plrpos.z - 1,
            float(bidlist.pop(0)),
        )
        time.sleep(0.5)
    ##---------------------------------------------------------------

    bidlist = []  ##Clear the list
    for x in xrange(3):  ##Generate the 3 actual block ids that will count towards score
        bid = 0
        rand = random.randint(1, 3)
        if rand == 1:
            bid = 41
        if rand == 2:
            bid = 42
        if rand == 3:
            bid = 57

        bidlist.append(bid)  ##Add new values to the list

    ##Get score from ids
    score = 0

    if (
        bidlist.count(42) == 2
    ):  ##list.count(x) returns how many 'x' values are in the list
        score += 50
    elif bidlist.count(42) == 3:
        score += 100

    if bidlist.count(41) == 2:
        score += 100
    elif bidlist.count(41) == 3:
        score += 200

    if bidlist.count(57) == 2:
        score += 150
    elif bidlist.count(57) == 3:
        score += 300

    ##Draw the end scores
    mc.setBlocks(
        plrpos.x,
        plrpos.y + 1,
        plrpos.z - 1,
        plrpos.x,
        plrpos.y + 1,
        plrpos.z - 1,
        float(bidlist.pop(0)),
    )
    time.sleep(0.5)
    mc.setBlocks(
        plrpos.x - 2,
        plrpos.y + 1,
        plrpos.z - 1,
        plrpos.x - 2,
        plrpos.y + 1,
        plrpos.z - 1,
        float(bidlist.pop(0)),
    )
    time.sleep(0.5)
    mc.setBlocks(
        plrpos.x + 2,
        plrpos.y + 1,
        plrpos.z - 1,
        plrpos.x + 2,
        plrpos.y + 1,
        plrpos.z - 1,
        float(bidlist.pop(0)),
    )
    time.sleep(0.5)

    if score == 300:
        mc.postToChat("Score - 300 Jackpot!")
    elif score == 150:
        mc.postToChat("Score - 150!")
    elif score == 200:
        mc.postToChat("Score - 200!")
    elif score == 100:
        mc.postToChat("Score - 100!")
    elif score == 50:
        mc.postToChat("Score - 50!")
    elif score == 0:
        mc.postToChat("Score - 0 Bankrupt!")
    print(score)


def waitForPlay():
    while True:  ##Waits for a gold block to be placed at the end of the machine
        if mc.getBlock(plrpos.x + 4, plrpos.y + 1, plrpos.z - 1) == 41:
            mc.setBlock(
                plrpos.x + 4, plrpos.y + 1, plrpos.z - 1, 0
            )  ##Once found, remove the gold block
            play()  ##Start the game code
            break
    waitForPlay()  ##After the play has been made, break the loop and rerun the function to repeat


def buildModel():
    mc.setBlocks(
        plrpos.x + 3,
        plrpos.y + 2,
        plrpos.z - 1,
        plrpos.x - 3,
        plrpos.y,
        plrpos.z - 1,
        1,
    )
    mc.setBlocks(
        plrpos.x, plrpos.y + 1, plrpos.z - 1, plrpos.x, plrpos.y + 1, plrpos.z - 3, 0
    )
    mc.setBlocks(
        plrpos.x - 2,
        plrpos.y + 1,
        plrpos.z - 1,
        plrpos.x - 2,
        plrpos.y + 1,
        plrpos.z - 1,
        0,
    )
    mc.setBlocks(
        plrpos.x + 2,
        plrpos.y + 1,
        plrpos.z - 1,
        plrpos.x + 2,
        plrpos.y + 1,
        plrpos.z - 1,
        0,
    )


def init():
    mc.setBlocks(
        plrpos.x + 5, plrpos.y, plrpos.z - 5, plrpos.x - 5, plrpos.y, plrpos.z + 5, 0
    )
    buildModel()


init()
waitForPlay()
