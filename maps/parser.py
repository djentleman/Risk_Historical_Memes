from PIL import Image

def parsePixel(pixTup):
    if (pixTup[0] == pixTup[1] and pixTup[0] == pixTup[2]):
        if pixTup[0] == 0:
            return "B" #border
        elif pixTup[0] == 255:
            return "L" #land
    return "O" # ocean
        

def main():
    im = Image.open("europebridges.png")

    xS = im.size[0]
    yS = im.size[1]

    pArr = []

    for i in range(xS):
        row = []
        for j in range(yS):
            row.append(parsePixel(im.getpixel((i, j))))
        pArr.append(row)


    out = "var mapArr = " + str(pArr)
    open("mapdata.js", "w+").write(out)
            
if __name__ == "__main__":
    main()
