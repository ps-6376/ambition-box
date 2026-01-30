# import pandas as pd
# preproceesing of  city data


# df=pd.read_csv("gurgoan.csv",encoding="latin-1" )
# df.columns= df.columns.str.strip() //clean white space from columns name

# # data=df[df.duplicated(subset=df.loc[0:,"company name"], keep=False)]
# # df["company name"]=df["company name"].drop_duplicates(keep='first')delete the duplicate rows

# # print(df["details"])
# # df[["company_type","location"]]=df["details"].str.split("|",expand=True) split the details column into company_type,location,other_loc
# # df[["location","other_loc"]]=df["location"].str.split("+",expand=True)
# # df.drop(["other details","details"],axis=1,inplace=True) drop details and other details

# # data=df[df["other_loc"].isna()==True]find nulll data in other_loc
# # d=df[df["location"].isna()==True]find nulll data in location
# # df.drop(data.index,inplace=True) drop null data
# # df.drop(d.index,inplace=True)
# df["ratings"]=df["ratings"].astype(float) convert ratings to float type
# print(df)
# save the data
# df.to_csv("gurgoan.csv")










import pandas as pd
from sqlalchemy import create_engine
# lis=["jaipur.csv","gurgoan.csv"]

# for i in lis:
#     df = pd.read_csv(i)
#     if "Unnamed: 0" in df.columns:
#         df.drop(columns=["Unnamed: 0"], inplace=True)
#         print("data")
#     if "Unnamed: 0.1" in df.columns:
#         df.drop(columns=["Unnamed: 0.1"], inplace=True)
#         print("data")
#     if "Unnamed: 0.2" in df.columns:
#         df.drop(columns=["Unnamed: 0.2"], inplace=True)
#         print("data")
#     if "Unnamed: 0.3" in df.columns:
#         df.drop(columns=["Unnamed: 0.3"], inplace=True)
#         print("data")
#     else:
#         print(df)
#         df.to_csv(i)
#         print("succefulll")

lis=["jaipur","gurgoan"]
for i in lis:
    df= pd.read_csv(f"{i}.csv")
    engine =  create_engine(
    "mysql+mysqlconnector://root:""@localhost:3306/filedata"
    )
    df.to_sql(
    name=i,
    con=engine,
    if_exists="append",
    index=False
    )






# lis=["lucknow.csv","new delhi.csv","chennai.csv","pune.csv","Banglore.csv","indore.csv","Ahmedabaad.csv","hyderabaad.csv","noida.csv","Mumbai.csv","navimumbai.csv"]
# for i in lis:
#     df = pd.read_csv(i)
#     if "Unnamed: 0" in df.columns:
#         df.drop(columns=["Unnamed: 0"], inplace=True)
#         print("data")
#     if "Unnamed: 0.1" in df.columns:
#         df.drop(columns=["Unnamed: 0.1"], inplace=True)
#         print("data")
#     if "Unnamed: 0.2" in df.columns:
#         df.drop(columns=["Unnamed: 0.2"], inplace=True)
#         print("data")
#     if "Unnamed: 0.3" in df.columns:
#         df.drop(columns=["Unnamed: 0.3"], inplace=True)
#         print("data")
#     if "Unnamed: 0.4" in df.columns:
#         df.drop(columns=["Unnamed: 0.4"], inplace=True)
#         print("data")
#     if "Unnamed: 0.5" in df.columns:
#         df.drop(columns=["Unnamed: 0.5"], inplace=True)
#         print("data")
#     if "Unnamed: 0.6" in df.columns:
#         df.drop(columns=["Unnamed: 0.6"], inplace=True)
#         print("data")
#     else:
#         print(df)
#         df.to_csv(i)
#         print("succefulll")
# lis=["kolkata","lucknow","new delhi","chennai","pune","indore","Ahmedabaad","hyderabaad","noida","Mumbai","navimumbai"]
# for i in lis:
#     df= pd.read_csv(f"{i}.csv")
#     engine =  create_engine(
#     "mysql+mysqlconnector://root:""@localhost:3306/filedata"
#     )
#     df.to_sql(
#     name=i,
#     con=engine,
#     if_exists="append",
#     index=False
#     )

#     print("CSV data stored successfully in MySQL")

# Here we use a column with categorical data
    # print(i)
    # df=pd.read_csv(i)
    # df["company_type"]=df["company_type"].str.strip()
    # print(df["company_type"]

# data= df[(df[" ratings"]>=3) & (df["company_type"]=="Banking ")]
# print(data) 



# index=data.index.values
# for i in data.index:
#     for j in data:
#        print(data.loc[i,j])
       

