# Program: ZbrozekP1.py
# Programmer: Mike Zbrozek 
# MZbrozek1@cnm.edu
# Date: 31 Aug 2023
# Purpose: Provides use the capability to calculate 
# the volume of a pyramid 

import math

# Epic Logo 
print("""    
          ,/`.  Pyramid
        ,'/ __`.
      ,'_/_  _ _`.  Surface area
    ,'__/_ ___ _  `.      &
  ,'_  /___ __ _ __ `.   volume calculator
 '-.._/___...-"-.-..__`. """)

# Get the base length from the user
base = float(input("How many FEET wide is the base of your magnificent pyramid?"))
# Get the Height from the user
height = float(input("How many FEET tall is the height of your magnificent pyramid?"))
# Calculate base area 
base_area = round(base**2, 3)
# Calculate the volume of the pyramid
volume = round((base_area * (height/3)), 3)
# Calculate the slant height of the pyramid
slant_height = round(math.sqrt((height**2)+((base_area/2)**2)), 3)
# Calculate the surface are of all 4 sides
area_pyramid = round((slant_height * (base_area/2) * 4), 3)
# Output this to the user
print ("\n""YOUR PYRAMIDE is", base, "feet wide", "by", height, "feet tall", "\n"""" 
          ,/`.           |
        ,'/ __`.         |
      ,'_/_  _ _`.       | H
    ,'__/_ ___ _  `.     | 
  ,'_  /___ __ _ __ `.   |
 '-.._/___...-"-.-..__`. |
       
              W        
      -------------------           
       """ )
print('The volume of your magnificent pyramid is:\n', volume, "cubicFeet")
print('The surface are of all 4 sides of your magnificent pyramid is:\n', area_pyramid, "sqfeet")
