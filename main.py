import pandas as pd
file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
df = pd.read_csv("path_to_your_file/data.csv")

print(df)