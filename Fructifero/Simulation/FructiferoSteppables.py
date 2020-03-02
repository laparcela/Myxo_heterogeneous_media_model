
from PySteppables import *
import CompuCell
import sys

import numpy as np
import numpy.random as rng



class FructiferoSteppable(SteppableBasePy):

#######################################################################
# Create Random Particles/Cells 
# Modified Julio Belmonte code

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        # any code in the start function runs before MCS=0

        number_of_medium2 = 23   
        height_of_medium2 = 24      
        width_of_medium2 = 24        
        self.seed_medium2(number_of_medium2,height_of_medium2,width_of_medium2)               
                
        number_of_vegetativas = 700
        
        height_of_vegetativas = 12
        
        self.seed_vegetativas(number_of_vegetativas,height_of_vegetativas)        
              
##To create Random Particles ###        
#     def seed_medium2(self,N,H,W):       
            
#         to_be_created = N         
#         while to_be_created > 0: #still have cells to be created
#             x = rng.randint(0,self.dim.x)#using numpy.random.randint to get an
#             #                               integer in range [0,max x)
#             y = rng.randint(0,self.dim.y)            
#             existing_cell_at_point = self.cellField[x, y, 0]#grabing the cell in the point            
#             if not existing_cell_at_point: #there is no cell there
#                 #I'm going to see if there's free space                 
#                 free_pixels_y = []          
#                 if y+H<self.dim.y:
#                     for check_y in range(y-H,y+H):
#                         existing_cell_at_point_2_y = self.cellField[x, check_y, 0]                        
#                         if not existing_cell_at_point_2_y:
#                             free_pixels_y.append(check_y)                                           
                
#                 free_pixels_x = []                
#                 if x+W<self.dim.x:
#                     for check_x in range(x-W,x+W):
#                         existing_cell_at_point_2_x = self.cellField[check_x, y, 0]
#                         if not existing_cell_at_point_2_y:
#                             free_pixels_y.append(check_y)
#                             if not existing_cell_at_point_2_x:
#                                 free_pixels_x.append(check_x)
                    
#                     if len(free_pixels_y) == H:
#                         if len(free_pixels_x) == W:                                              
#                             to_be_created -=1#we are creating a cell, reducing the counter                           
#                             free_pixels_y = np.array(free_pixels_y)
#                             free_pixels_x = np.array(free_pixels_x)                            
#                             print"creating medium2 at\n x=",free_pixels_x,'\n y=',free_pixels_y                           
#                             new_medium2 = self.newCell(self.MEDIUM2)                                    
#                             self.cellField[np.amin(free_pixels_x):np.amax(free_pixels_x),
#                                         np.amin(free_pixels_y):np.amax(free_pixels_y), 
#                                         0] = new_medium2
                    
#                     elif len(free_pixels_y) > H:
#                         if len (free_pixels_x) > W:
#                             to_be_created -=1#we are creating a cell, reducing the counter                          
#                             free_pixels_y = free_pixels_y[:H] #cuts the list down to the lenght
#                             #                             of the cell
#                             free_pixels_x = free_pixels_x[:W]                           
#                             free_pixels_y = np.array(free_pixels_y)
#                             free_pixels_x = np.array(free_pixels_x)                         
#                             print"creating medium2 at\n x=",free_pixels_x,'\n y=',free_pixels_y                           
#                             new_medium2 = self.newCell(self.MEDIUM2)                            
#                             self.cellField[np.amin(free_pixels_x):np.amax(free_pixels_x),
#                                         np.amin(free_pixels_y):np.amax(free_pixels_y), 
#                                         0] = new_medium2  
    

#### To create Random Cells #####    
    def seed_vegetativas(self,N,H):
         
        to_be_created = N
        
        while to_be_created > 0: #still have cells to be created
            x = rng.randint(0,self.dim.x)#using numpy.random.randint to get an
            #                               integer in range [0,max x)
            y = rng.randint(0,self.dim.y)
            
            existing_cell_at_point = self.cellField[x, y, 0]#grabing the cell in the point
            
            if not existing_cell_at_point: #there is no cell there
                #I'm going to see if there's free space 
                free_pixels = []
                if y+H<self.dim.y:
                    for check_y in range(y-H,y+H):
                        existing_cell_at_point_2 = self.cellField[x, check_y, 0]
                        if not existing_cell_at_point_2:
                            free_pixels.append(check_y)
                            
                    if len(free_pixels) == H:
                        
                        
                        
                        to_be_created -=1#we are creating a cell, reducing the counter
                        
                        free_pixels = np.array(free_pixels)
                        
                        print"creating vegetativa at\n x=",x,'\n y=',free_pixels
                        
                        new_vegetativa = self.newCell(self.VEGETATIVAS)
                        
                        
                        self.cellField[x, 
                                    np.amin(free_pixels):np.amax(free_pixels), 
                                    0] = new_vegetativa
                    elif len(free_pixels) > H:
                        
                        to_be_created -=1#we are creating a cell, reducing the counter
                        
                        free_pixels = free_pixels[:H] #cuts the list down to the lenght
                        #                             of the cell
                        
                        free_pixels = np.array(free_pixels) 
                        
                        print"creating vegetativa at\n x=",x,'\n y=',free_pixels
                        
                        new_vegetativa = self.newCell(self.VEGETATIVAS)
                        
                        self.cellField[x, 
                                    np.amin(free_pixels):np.amax(free_pixels), 
                                    0] = new_vegetativa
                                                                                           
    def step(self,mcs):        
        #type here the code that will run every _frequency MCS
        pass
    def finish(self):
        # Finish Function gets called after the last MCS
        pass

#######################################################################
# Output Data : Number and size of aggregates
# Modified Juan Arias code
 
class HandleOutputDataSteppable(SteppableBasePy):
	def __init__(self,_simulator,_frequency = 1):
		SteppableBasePy.__init__(self,_simulator,_frequency)
	def start(self):
		### Initialize file information...
		file_name = "output_data_"+ str(time.time()) + ".txt"
                path_to_file = "/Users/Paty Pozo/CC3DWorkspace/46x16_1000MCS"
		self.output_data = open(path_to_file + file_name, "w")
		
		### Cell attributes to extract
                for cell in self.cellListByType(self.VEGETATIVAS):
                    self.attributes_to_extract = ['id', 'xCOM', 'yCOM']
                    
		### Cell neighbordhood
		### This variable is True is you want to print the cell-to-cell neighbors. It is false otherwise.
		    self.cell_neighborhood = True

	def step(self, mcs):
		### Cell atributes
		for attribute in self.attributes_to_extract:
			self.output_data.write("MCS" + str(mcs)+ "\tCELL_ATTRIBUTE\t" + attribute + ":\t")
			for cell in self.cellListByType(self.VEGETATIVAS):
				cellattr = getattr(cell, attribute)
				self.output_data.write(" " + str(cellattr))
			self.output_data.write("\n")

                ### Cell interactions
		if(self.cell_neighborhood):
                        self.output_data.write("MCS" + str(mcs)+ "\tCELL_INTERACTION\tCELL_NEIGHBORS:\t")
			for cell in self.cellListByType(self.VEGETATIVAS):
				for neighbor , commonSurfaceArea in self.getCellNeighborDataList(cell):
					if neighbor:
                                            if neighbor.id > cell.id:
						self.output_data.write(" " + str(cell.id) + "-" + str(neighbor.id))
			self.output_data.write("\n")

		
		self.output_data.write("MCS" + str(mcs)+ "\tREPORT\n")
        def finish(self):
		self.output_data.close()                               
                             
#######################################################################
# Output Data : Number of aggregate cells

class NeighborDataSteppable(SteppableBasePy):               
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        # any code in the start function runs before MCS=0
        pass
    def step(self,mcs):        
        #type here the code that will run every _frequency MCS
        for cell in self.cellList:
            print "cell.id=",cell.id
    def finish(self):
        # Finish Function gets called after the last MCS
        pass

    #No. of Neighboors       
    def step (self,mcs):
        fileName= 'Output'+str(mcs)+'.txt'
        try:
            fileHandle, fullFileName = self.openFileInSimulationOutputDirectory(fileName, "w")
        except IOError:
            print "Could not open file ", fileName, " for writing. "
            return
        for cell in self.cellListByType(self.VEGETATIVAS):
            neighborList = self.getCellNeighborDataList(cell)       
            print >>fileHandle, neighborList.neighborCountByType()
            

                