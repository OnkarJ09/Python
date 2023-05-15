import pandas as pd
pd.options.display.max_rows = 9999

mydataset = {
    'cars':['BMW','Volvo','Lambo','RR'],
    'passings':[2,3,6,1]
}

a = 1,2,5,45,5
#myvar = pd.Series(a)
myvar = pd.DataFrame(mydataset)
print(myvar)


print(pd.__version__)

print(myvar.loc[0])

df = pd.read_csv('data.csv')
print(df.to_string)
#print(df)


print(pd.options.display.max_rows)