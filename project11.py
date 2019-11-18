#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

class Sphere:
    
    def __init__(self , radius):
        self.radius = radius
        self.surfaceArea = (4/3) * math.pi * self.radius ** 3
        self.volume = 4 * math.pi * self.radius ** 2
        
    def getRadius(self):
        return self.radius
        
    def getSurfaceArea(self):
        return self.surfaceArea
        
    def getVolume(self):
        return self.volume
        
def main():
    
    radius = float(input("Enter the radius of your sphere: "))
    yourSphere = Sphere(radius)
    print("The surface area of your sphere is" , yourSphere.getSurfaceArea())
    print("The volume of your sphere is" , yourSphere.getVolume())
    
if __name__ == '__main__':
    main()


# In[ ]:




