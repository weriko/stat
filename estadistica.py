import matplotlib.pyplot as plt
import math

class Stats():
    def __init__(self, data, isGroup = False):
        self.data = data
        self.average = sum(data)/len(data)
        self.variance = (1/len(data))*sum([(x - self.average)**2 for x in self.data])
        self.sample_variance = (1/(len(data)-1))*sum([(x - self.average)**2 for x in self.data])
        self.deviation = self.variance**(1/2)
    def toGroup(self):
        self.k = round(1 + 3.322*math.log(len(self.data), 10))
        self.max = max(self.data)
        self.min = min(self.data)
        self.data_range = self.max - self.min
        
        self.amplitude = math.ceil(self.data_range/self.k)
        self.data_dict = {}
        self.classes = []
        self.classes_range = []
        
        for i in range(self.k):
            if i:
                self.classes.append((self.min+i*self.amplitude))
                self.classes_range.append(f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}")
                self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"] = {}
                self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["range"] = [x for x in self.data if self.min+i*self.amplitude < x <= self.min+(i+1)*self.amplitude ]
                self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["abs_simple"] = len(self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["range"])
                self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["abs_cumulative"] = self.data_dict[f"{(self.min+(i-1)*self.amplitude)}-{self.min+(i)*self.amplitude}"]["abs_cumulative"] + self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["abs_simple"] # Takes the previous class absolute cumulative and adds the amount of the current class  
                self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["rel_simple"] = self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["abs_simple"]/len(self.data)
                self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["rel_cumulative"] = self.data_dict[f"{(self.min+(i-1)*self.amplitude)}-{self.min+(i)*self.amplitude}"]["rel_cumulative"] + self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["rel_simple"]
                
                
            else:
                #First class has some small differences
                self.classes.append((self.min+i*self.amplitude))
                self.classes_range.append(f"{self.min+i*self.amplitude}-{self.min+(i+1)*self.amplitude}")
                self.data_dict[f"{self.min+i*self.amplitude}-{self.min+(i+1)*self.amplitude}"] = {}
                self.data_dict[f"{self.min+i*self.amplitude}-{self.min+(i+1)*self.amplitude}"]["range"] = [x for x in self.data if x <= self.min+(i+1)*self.amplitude ]
                self.data_dict[f"{self.min+i*self.amplitude}-{self.min+(i+1)*self.amplitude}"]["abs_simple"] = len(self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["range"])
                self.data_dict[f"{self.min+i*self.amplitude}-{self.min+(i+1)*self.amplitude}"]["abs_cumulative"] = len(self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["range"]) #The cumulative frequency for the first one is just the amount of objects in the class
                self.data_dict[f"{self.min+i*self.amplitude}-{self.min+(i+1)*self.amplitude}"]["rel_simple"] = self.data_dict[f"{self.min+i*self.amplitude}-{self.min+(i+1)*self.amplitude}"]["abs_simple"]/len(self.data)
                self.data_dict[f"{self.min+i*self.amplitude}-{self.min+(i+1)*self.amplitude}"]["rel_cumulative"] = self.data_dict[f"{self.min+i*self.amplitude}-{self.min+(i+1)*self.amplitude}"]["abs_simple"]/len(self.data)
                
        self.classes.append(self.max+1)   
    def percentile(self, p):
        for i in range(len(self.classes_range)-1):
            print(self.data_dict[self.classes_range[i]]["rel_cumulative"])
            if self.data_dict[self.classes_range[i]]["rel_cumulative"] < p < self.data_dict[self.classes_range[i+1]]["rel_cumulative"]:
                class_n = i
                break
        print(class_n)
        a = self.classes[class_n] + self.amplitude*(p)
            
            
            
        
            
            
#stats = Stats(list(range(100)))
stats = Stats([83,51,66,61,82,65,54,56,92,60,65,87,68,64,51,70,75,66,74,68,44,55,78,69,98,67,82,77,79,62,38,88,76,99,84,47,60,42,66,74,91,71,83,80,68,65,51,56,73,55])
stats.toGroup()
print(stats.k)
print(stats.data_dict)
print(stats.variance)
print(stats.deviation)
print(stats.amplitude)     
stats.percentile(0.75)   
print(stats.classes)