# python3 
from tbg import *

tbg = TheBenevolentGifter('SampleData - Benevolent Gifter - Sheet1.csv')
#test importing list of GCs
tbg.import_list()

#view the entire list
print("Viewing list after importing")
tbg.view_list()
print("\n")

#test adding GCs to the list
tbg.add_gc('Tony','Stark',48,'New York','Good')
print("Viewing list after adding Tony Stark")
tbg.view_list()
print("\n")

#test removing GCs to the list
tbg.remove_gc(1)
print("Viewing list after removing Jane Doe")
tbg.view_list()
print("\n")

#test modifying GCs
tbg.modify_gc(2,['Kate','Smith',24,'Alabama','Bad'])
print("Viewing list after modifying index 2 to Kate Smith")
tbg.view_list()
print("\n")