#Creating a polygdn
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
Dy = list()
P = [(24970,19250),(23600,19250),(20740,22110),(22790,24160),(19395,27554)\
    ,(17345,25504),(15560,27289),(15560,30215),(16490,30215),(16490,31500)\
    ,(20670,31500),(20670,33700),(23370,33700),(23370,31150),(25785,31150)\
    ,(25785,41415),(16740,41415),(16740,39400),(10060,39400),(10060,41415)\
    ,(4315,41415),(4315,39400),(1300,39400),(1300,31300),(3545,31300)\
    ,(3545,34300),(6245,34300),(6245,29085),(4785,29085),(4785,26570)\
    ,(2085,26570),(2085,28615),(0,28615),(0,21110),(11925,21110),(12445,21630)\
    ,(16865,17210),(14600,14946),(16407,13139),(14498,11230),(12691,13036)\
    ,(9085,9430),(11430,7085),(11430,4800),(19590,4800),(19590,9250),(26255,9250)\
    ,(26255,7085),(32000,7085),(32000,9720),(36510,9720),(36510,15050)\
    ,(34330,15050),(34330,12850),(31430,12850),(31430,19250),(34330,19250)\
    ,(34330,17050),(37480,17050),(37480,23430),(34330,23430),(34330,26060)\
    ,(28385,26060),(28385,24260),(24970,24260),(24970,19250)]
P = [(0,0),(100,0),(100,10),(100,50),(90,50),(90,10),(80,10),(80,50),(70,50)\
     ,(70,10),(60,10),(60,50),(50,50),(50,10),(40,10),(40,50)\
     ,(30,50),(30,10),(20,10),(20,50),(10,50),(10,10),(0,10),(0,0)]
P = [(24970,19250),(23600,19250),(20740,22110),(22790,24160),(19395,27554),\
    (17345,25504),(15560,27289),(15560,30215),(11165,30215),(11165,27915),\
    (12435,27915),(15220,24415),(12445,21630),(16865,17210),(19650,19995),\
    (23600,16045),(24970,16045)]
P = [(8,8),(9,6),(11,8),(10,10),(9,12),(6,12),(5,16),(3,13),(0,13),(4,10)\
       ,(0,0),(5,0),(8,2),(6,6),(7,7)]
P = [(12,3),(8,8),(14,8),(9,11),(4,8),\
       (6,5),(2,8.5),(4,11),(0.5,11),(-2,7.5),(2,6),(-3,6),\
       (-2,3),(3,0),(4,2),(8,0),(14,0),(16,2),(15,8),(13,7)]
P = [(0,0),(100,0),(100,10),(100,50),(90,50),(90,10),(80,10),(80,50),(70,50)\
    ,(70,10),(60,10),(60,50),(50,50),(50,10),(40,10),(40,50)\
    ,(30,50),(30,10),(20,10),(20,50),(10,50),(10,10),(0,10)]
P = [(0,0),(4,0),(4,4),(0,4)]
P = [(10,10),(8,6),(7,8),(5,6),(4,7),(2,3)\
       ,(0,4),(0,2),(1,1),(6,0),(8,0),(10,2),(9,4)]
P = [(1,1),(2,2),(1,5),(4,3),(5,7),(5,5),(10,10),(10,-5),(6,-1),(3,-3)]
P = [(3,16),(4,13),(5,11),(6,10),(8,9),(7,7),(5,4),(6,2),(7,4),(7,0),\
       (4,0),(1,0),(1,1),(2,1),(3,3),(2,3),(2,6),(1,3),(0,3),(1,6)]
P = [(4,4),(8,4),(8,0),(14,-5),(20,0),(20,6),(15,6),(15,10),\
    (20,10),(20,14),(16,14),(16,16),(10,16),(10,14),(6,14),(6,16),(2,16)\
       ,(2,14),(0,14),(-5,7),(0,0),(2,-2),(4,0),(4,4)]
P = [(4000,4000),(8000,4000),(8000,0),(14000,-5000),(20000,0),(20000,6000),(15000,6000),(15000,10000),\
    (20000,10000),(20000,14000),(16000,14000),(16000,16000),(10000,16000),(10000,14000),(6000,14000),(6000,16000),(2000,16000),\
    (2000,14000),(0,14000),(-5000,7000),(0,0),(2000,-2000),(4000,0),(4000,4000)]
def Plot_Polygon(P):
    plt.title('Polygon')
    for i in range(len(P)):
        xlst.append(P[i][0])
        ylst.append(P[i][1])
    plt.fill(xlst,ylst,color = 'r')
    return  plt.show()
xlst = list()
ylst = list()
'''X = list()
Y = list()
while True:
    Vx = input("Enter the x coordinates:")
    if Vx == "done":break
    try: Vx = float(Vx)
    except: print("Invalid Input");continue
    X.append(Vx)
    Vy = input("Enter the y coordinates:")
    if Vy == "done":break
    try: Vy = float(Vy)
    except: print("Invalid Input");continue
    Y.append(Vy)
P = [(X[i],Y[i]) for i in range(0,len(X))]'''
# Plot_Polygon(P)

''' Grayscale Image and Binarizing the Image'''

image=Image.open('D:\Educational\A WPI Assignments and Materials\Motion Planning\Project\Robot-Motion-Planning-for-an-optimal-Watchman-Route\Colored Polygons\P10.png')
gray_image=image.convert('L')
gray_image_array=np.asarray(gray_image)

threshold = 200
gray_image = gray_image_array.copy()
gray_image[gray_image_array > threshold] = 0
gray_image[gray_image_array <= threshold] = 255


plt.imshow(gray_image,cmap='gray', vmin = 0, vmax = 255)
plt.show()