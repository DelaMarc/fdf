import sfml as sf
import sys
import check as ch

def file_open(elem):
    fd = open(elem, 'r')
    line = fd.readlines()
    tab1 = []

    for i in line:
        tab = i.split( )
        tab1.append(tab)
    return (tab1)

def rely(tab, img, a):
    for x in range(0, len(tab) - 1):
        vector1 = sf.Vector2(tab[x][0], tab[x][1])
        vector2 = sf.Vector2(tab[x + 1][0], tab[x + 1][1])
        draw(img, vector1, vector2, tab[x][2])
    for y in range(0, len(tab)):
        vector1 = sf.Vector2(tab[y][0], tab[y][1])
        vector2 = sf.Vector2(tab[y - a][0], tab[y - a][1])
        draw(img, vector1, vector2, tab[y][2])

def draw(img, v1, v2, z):
    x = v1.x
    y = v2.y

    while x < v2.x:
        y = v1.y + ((v2.y - v1.y) * (x - v1.x) / (v2.x - v1.x))
        if int(z) > 0:
            img[x, y] = sf.Color.GREEN
        elif int(z) == 0:
            img[x, y] = sf.Color.RED
        x = x + 0.1

def iso_points(tab, ylen, x_high, img):
    y = 0
    z = 0
    cte1 = 0.7
    cte2 = 0.7
    tab2 = []

    for i in tab:
        y = y + 1 * int(ylen / len(tab)) * cte1
        x = 0
        for z in i:
            Z = z
            x = x + 1 * int(x_high / len(i)) * cte1
            x_iso = cte1 * x - cte2 * y + (x_high / 2)
            y_iso = - int(z) + (cte1 / 2) * x + (cte2 / 2) * y + (ylen / 4)
            tab2.append([x_iso, y_iso, Z])
    a = len(tab[0])
    rely(tab2, img, a)
    return (tab2)

def main(path):
    if len(sys.argv) != 2:
        print("Error argument")
        return (-1)
    a = file_open(sys.argv[1])
    if ch.check(a) == 1:
        print("corrupted file")
        return (-1)
    img = sf.Image.create(800, 800, sf.Color.BLACK)
    w = sf.RenderWindow(sf.VideoMode(800, 800), "fdf")
    b = iso_points(a, 800, 800, img)
    texture = sf.Texture.from_image(img)
    sprite = sf.Sprite(texture)
    while w.is_open:
        for event in w.events:
            if type(event) is sf.CloseEvent:
                w.close()
            if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
                w.close()
        w.clear(sf.Color.BLACK)
        w.draw(sprite)
        w.display()

main(sys.argv)
