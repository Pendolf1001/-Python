import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
robot=[ True if i=='robot' else False for i in data ['whoAmI'] ]
human=[ True if i=='human' else False for i in data ['whoAmI'] ]
res=pd.DataFrame({'robot':robot,'human':human})
print(res)