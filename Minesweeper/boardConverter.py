import pickle
import numpy as np
from PIL import Image
from screenshot import *
from cellColors import pixelCoordinate
from cellColors import cellTypes
import sys

colors = pickle.load(open("colors.p", "rb"))
errors = 0


def getCode(rgb, column, row):
    for code in cellTypes:
        sum = 0
        for i in range(0, 3):
            sum += abs(rgb[i] - colors[code][i])
        if sum < 25:
            if int(code) > 10:
                return int(code[0])
            else:
                return int(code)

    global errors
    errors += 1
    cellScreenshot('errors-'+str(errors)+'.png', column, row)
    sys.exit("FINISHED - Couldn't determine detected number. ")


def getBoardArray():
    moveMouseAway()
    screenshot()

    # time.sleep(1)
    board = Image.open("board.png")
    boardRGB = board.convert("RGB")

    result = []

    for row in range(numRows):
        arr = []
        for column in range(numColumns):
            xCoordinate = boardXCoord(column) + pixelCoordinate[0]
            yCoordinate = boardYCoord(row) + pixelCoordinate[1]

            pixelValue = boardRGB.getpixel((xCoordinate, yCoordinate))
            arr.append(getCode(pixelValue, column, row))

        result.append(arr)

    print("\n")
    # print(np.array(result))
    board.close()

    return np.array(result)


# getBoardArray()
