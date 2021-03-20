import plotly.express as px
import pandas as pd 
import csv 
import plotly.graph_objects as go

df = pd.read_csv(r"C:\Users\91814\OneDrive\Desktop\Whitehat\Class 107\data.csv")
print(df.groupby("level")["attempt"].mean())

mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, x ='student_id', y ='level', size = 'attempt', color ='attempt')
fig.show()



