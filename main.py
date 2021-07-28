import pandas as pd
import plotly.express as pl
import numpy as np

df = pd.read_csv("./data.csv")

x = df.groupby(["student_id","level"],as_index=False)['attempt'].mean()

 
scp = pl.scatter(x,x="student_id",y="level",size="attempt",color="attempt")

scp.show()