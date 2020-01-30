
import sys
from os import environ
from os import getcwd
import string

sys.path.append(environ["PYTHON_MODULE_PATH"])


import CompuCellSetup


sim,simthread = CompuCellSetup.getCoreSimulationObjects()
        
# add extra attributes here
        
CompuCellSetup.initializeSimulationObjects(sim,simthread)
# Definitions of additional Python-managed fields go here

#Add Python steppables here
steppableRegistry=CompuCellSetup.getSteppableRegistry()
        
from FructiferoSteppables import FructiferoSteppable
steppableInstance=FructiferoSteppable(sim,_frequency=1)
steppableRegistry.registerSteppable(steppableInstance)

from FructiferoSteppables import HandleOutputDataSteppable
steppableInstance=HandleOutputDataSteppable(sim,_frequency=2000)
steppableRegistry.registerSteppable(steppableInstance)

from FructiferoSteppables import NeighborDataSteppable
steppableInstance=NeighborDataSteppable(sim,_frequency=2000)
steppableRegistry.registerSteppable(steppableInstance)

CompuCellSetup.mainLoop(sim,simthread,steppableRegistry)
        