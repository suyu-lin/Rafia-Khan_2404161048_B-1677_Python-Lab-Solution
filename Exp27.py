import pandas as pd
data_2d = [[1, "Azka"], [2, "Rafia"]]
print("DataFrame from 2D list:\n", pd.DataFrame(data_2d, columns=["ID", "Name"]))
print(f"From 2D List/List of Lists:\n{pd.DataFrame([[1, 'A'], [2, 'B']], columns=['ID', 'Val'])}")
print(f"From Dict of Lists:\n{pd.DataFrame({'ID': [1, 2], 'Val': ['A', 'B']})}")
print(f"From List of Tuples:\n{pd.DataFrame([(1, 'A'), (2, 'B')], columns=['ID', 'Val'])}")
print(f"From List of Dicts:\n{pd.DataFrame([{'ID': 1, 'Val': 'A'}, {'ID': 2, 'Val': 'B'}])}")