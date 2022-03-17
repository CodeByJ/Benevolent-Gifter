# python3

import pandas as pd

class TheBenevolentGifter:

    def __init__(self, list_file):
        self.list_file = list_file
        self.list_data = pd.DataFrame()  

    def import_list(self):
        self.list_data = pd.read_csv (self.list_file)

    def view_list(self):
        print(self.list_data)

    # add GC to end of csv file
    def add_gc(self, first_name:str, last_name:str, age:int, location:str, status:str):
        self.list_data.loc[len(self.list_data.index)] = [first_name, last_name, age, location, status] 
        self.list_data.to_csv(self.list_file, mode='w', index=False, header=True)

    # remove GC by row  #
    def remove_gc(self, index:int):
        self.list_data.drop(index,inplace=True)
        self.list_data.to_csv(self.list_file, mode='w', index=False, header=True)
        self.import_list()

    # modify GC by row #. 
    def modify_gc(self, index:int, new_data:str):
        if new_data[0]:
            self.list_data.at[index,'First Name']= new_data[0]
        if new_data[1]:
            self.list_data.at[index,'Last Name']= new_data[1]
        if new_data[2]:
            self.list_data.at[index,'Age']= int(new_data[2])
        if new_data[3]:
            self.list_data.at[index,'Location']= new_data[3]
        if new_data[4]:
            self.list_data.at[index,'Good or Bad']= new_data[4]
        
        self.list_data.to_csv(self.list_file, mode='w', index=False, header=True)

