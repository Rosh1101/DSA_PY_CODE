class Data:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link

    def get_data(self):
        return self.data
    def get_link(self):
        return self.link

   
    def set_link(self,link):
        self.link = link

data1 = Data(5)
data2 = Data(6)
print(data1.data)
print(data2.data)

data1.set_link(data2)
data2.set_link(data1)

for_Data_1 = data2.get_link().get_data()
for_data_2 = data1.get_link().get_data()
print(f"Data 1 says that the value of data2 is:{for_data_2}")
print(f"Data2 says that the value of Data1 is {for_Data_1}")

