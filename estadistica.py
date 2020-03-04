import matplotlib.pyplot as plt
import math
import pandas as pd

class Stats():
    def __init__(self, data, isGroup = False):
        if not isGroup:
            self.data = data
            self.average = sum(data)/len(data)
            self.variance = (1/len(data))*sum([(x - self.average)**2 for x in self.data])
            self.sample_variance = (1/(len(data)-1))*sum([(x - self.average)**2 for x in self.data])
            self.deviation = self.variance**(1/2)
            
            
            #TODO
        else:
            self.data = data
            self.data_dict = {}
            self.k = len(self.data.keys())
            self.n = sum([x for x in self.data.values()])
            self.classes_range = list(self.data.keys())
            self.classes = [self.get_first_nums(x) for x in self.data.keys() ]
            self.classes.append(self.get_last_nums(list(self.data.keys())[-1]))
            
            
            
            
            
            for i in range(self.k):
                self.data_dict[self.classes_range[i]] = {}
                
                self.data_dict[self.classes_range[i]]["abs_simple"] = list(self.data.values())[i] 
                self.data_dict[self.classes_range[i]]["abs_cumulative"] = self.data_dict[self.classes_range[i]]["abs_cumulative"] + self.data_dict[self.classes_range[i]]["abs_simple"] # Takes the previous class absolute cumulative and adds the amount of the current class  
                self.data_dict[self.classes_range[i]]["rel_simple"] = self.data_dict[self.classes_range[i]]["abs_simple"]/len(self.n)
                self.data_dict[self.classes_range[i]]["rel_cumulative"] = self.data_dict[self.classes_range[i]]["rel_cumulative"] + self.data_dictself.classes_range[i]["rel_simple"]
                
                
                
                
                
            print(self.classes)
            self.calc_grouped()
            
    def get_first_nums(self, string):
        x = ""
        for char in string:
            if char.isdigit():
                x+=char
            else:
                break
        return int(x) 
    def get_last_nums(self, string):
        x = ""
        for char in string[::-1]:
            if char.isdigit():
                x=char+x
            else:
                break
        return int(x) 
                
            
            
    def calc_grouped(self):
        self.midpoint = [ (self.classes[i] + self.classes[i+1])/2 for i in range(self.k)]
        
        
       
        
        
        self.average = 1/self.n * sum([self.midpoint[i] *  self.data[self.classes_range[i]]["abs_simple"] for i in range(self.k)  ])
        
        #List comprehension of the variance formula for grouped data
        
        self.variance = 1/self.n * (sum([ ( ( (  self.midpoint[i]  - self.average)) **2) * self.data[self.classes_range[i]]["abs_simple"]  for i in range(self.k)]))
        self.sample_variance = 1/(self.n-1) * (sum([ ( ( (  self.midpoint[i]  - self.average)) **2) * self.data[self.classes_range[i]]["abs_simple"]  for i in range(self.k)]))
        self.deviation = self.variance**(1/2)
        
        
        
    def toGroup(self):
        self.k = round(1 + 3.322*math.log(len(self.data), 10))
        self.max = max(self.data)
        self.min = min(self.data)
        self.n = len(self.data)
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
                #Dont know why i didnt use a variable for this, but okay
                self.data_dict[f"{(self.min+i*self.amplitude)}-{self.min+(i+1)*self.amplitude}"]["range"] = [x for x in self.data if self.min+i*self.amplitude < x <= self.min+(i+1)*self.amplitude ] #Creates a list with all the values within the class range
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
        
        
       
        self.data_notgrouped = self.data 
        self.data = self.data_dict
        self.calc_grouped()
        
    def percentile(self, p):
        for i in range(len(self.classes_range)-1):
            print(self.data[self.classes_range[i]]["rel_cumulative"])
            if self.data[self.classes_range[i]]["rel_cumulative"] < p < self.data[self.classes_range[i+1]]["rel_cumulative"]:
                class_n = i
                break
        print(class_n)
        a = self.classes[class_n] + self.amplitude*(p)
    def graph(self, g_type):
        if g_type == "hist":
            plt.hist(self.data_notgrouped, self.k, density=1)

            plt.show()
        elif g_type == "bar":
            abs_vars = []
            for value in self.data.values():
                abs_vars.append(value["abs_simple"])
            
            plt.bar(self.classes_range, abs_vars)
            plt.show()
        elif g_type == "pie":
            rel_vars = []
            for value in self.data.values():
                rel_vars.append(value["rel_simple"])
            
            plt.pie(rel_vars, labels=self.classes_range, autopct='%1.1f%%')
            plt.show()
        elif g_type == "line":
            abs_vars = []
            for value in self.data.values():
                abs_vars.append(value["abs_simple"])
            
            plt.plot(self.classes_range, abs_vars, '-o')
            plt.show()
        elif g_type == "cumu_line":
            abs_vars = []
            for value in self.data.values():
                abs_vars.append(value["abs_cumulative"])
            
            plt.plot(self.classes_range, abs_vars, '-o')
            plt.show()
            
        
        
            
            
        
            
            
#stats = Stats(list(range(100)))
stats = Stats([83,51,66,61,82,65,54,56,92,60,65,87,68,64,51,70,75,66,74,68,44,55,78,69,98,67,82,77,79,62,38,88,76,99,84,47,60,42,66,74,91,71,83,80,68,65,51,56,73,55])
#stats = Stats([x for x in range(100)])
#stats = Stats({"2-10":5,"10-18":3,"18-26":12,"26-32":5}, isGroup = True)

print(stats.variance, "variance")
stats.toGroup()
print("\n\n\n\n")
print("-------------")
print(stats.data)
print("-------------")
print("\n\n\n\n")
print(stats.k)
print(stats.data_dict)
print(stats.variance, "variance")
print(stats.deviation)
print(stats.amplitude)     
#stats.percentile(0.75)   
print(stats.classes)

stats.graph("bar")

stats.graph("hist")
df = pd.DataFrame(stats.data)
df.to_excel("output.xlsx") 
