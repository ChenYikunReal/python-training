import pandas as pd
import pandas_profiling

# https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
data = pd.read_csv('titanic.csv')

profile = data.profile_report(title='Titanic Dataset')
profile.to_file(output_file='titanic_report.html')
