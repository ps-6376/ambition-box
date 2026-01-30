from flask import Flask,render_template,request,redirect
import pymysql as sql
import pandas as pd
import plotly.express as px
import os
import pandas as pd
from sqlalchemy import create_engine


app=Flask("__name__")
@app.route("/",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        uname=request.form.get("username")   
        password=request.form.get("password")
        cnf_pass=request.form.get("cnf_pass")
        print(uname)
        print(password)
        print(cnf_pass)
        if password==cnf_pass:   
           try:
               conn=sql.connect(user="root",password="",host="localhost",port=3306,database="ambi_box")
               cursor=conn.cursor()
               query="insert into data(username,password,cnf_pass) values(%s,%s,%s);"
               cursor.execute(query,(uname,password,cnf_pass))
           except sql.err.IntegrityError as e:
            #   check condition for duplicate entrys
                if e.args[0] == 1062: 
                    war="this usename already exist" 
                    return render_template("signup.html",war=war)
                else:
                    war=f"there is {e}"
                    return render_template("signup.html",war=war)
           except Exception as e:
               msg=f"there is {e}"
               return render_template("signup.html",msg=msg)
           else:
               print("connection is close")
               conn.commit()
               conn.close()
               return redirect("/login")
        else:
            msg="password and confirm password not match"
            return render_template("signup.html",msg=msg)
    return render_template("signup.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        print("yes methood is post in login")
        uname=request.form.get("uname")
        passw=request.form.get("password")
        try:
            conn=sql.connect(user="root",password="",host="localhost",port=3306,database="ambi_box")       
            cursor=conn.cursor()
            query="select username, password from data where username=%s AND password=%s;"
            cursor.execute(query,(uname,passw))
            print("username and pass is passed")
            user=cursor.fetchone()
            if user:
                cursor.close()
                conn.close() 
                # conn=sql.connect(user="root",password="",host="localhost",port=3306,database="filedata")       
                # cursor=conn.cursor()
                # q="select company_type from jaipur;"
                # cursor.execute(q)
                # com_types=cursor.fetchall()
                # print(com_types)
                return redirect("/home")
            
            else:
                msgg="invalid credentials"
                return render_template("login.html",msgg=msgg)
        except sql.Error as e:
            msg=f"there is {e}"
            return render_template("login.html",msg=msg) 
    return render_template("login.html")

@app.route("/home",methods=["GET","POST"])
def home():
    if request.method=="POST":
            location=request.form.get("location")
            rating=request.form.get("rating")
            company_type=request.form.get("company_type")
            table=request.form.get("table")
            visulization=request.form.get("visual")
            print(table)
            print(visulization)
            print(location)
            print(rating)
            ratings=float(rating[0:len(rating)-1])
            print(company_type)
            # Create SQLAlchemy engine
            engine = create_engine("mysql+mysqlconnector://root:""@localhost:3306/filedata")
            # Read table directly into DataFrame
            df = pd.read_sql(f"SELECT * FROM {location};", con=engine)
            print(df)
            if table:
                   print(df["ratings"])
                   print(df["company_type"])
                   data= df[(df["ratings"]>=ratings) & (df["company_type"]==company_type)]
                   print(data)
                   return render_template("table.html",d=data) 
            elif visulization:
                try:
                  # top 5 company in the city
                  df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')
                  #  Sort by rating (descending)
                  df_sorted = df.sort_values(by='ratings', ascending=False)
                  print(df_sorted)
                  #  Fetch top 5 companies based on rating
                  top_5 = df_sorted.head(5)
                  #  Force descending order on x-axis
                  order = top_5['company name'].tolist()
                  print(order)
                  #  Plot histogram
                  fig = px.histogram(
                  top_5,
                  x='company name',
                  y='ratings',
                  category_orders={'company name': order},
                  title=f'{location} Top 5 Companies by Rating',
                  labels={
                    'company name': 'Company Name',
                     'ratings': 'Ratings'
                   }
    
                   )
                  output_folder = "static\images"
                  os.makedirs(output_folder, exist_ok=True)

                  fig.write_image(
                    f"{output_folder}/image1.jpeg",
                       format="jpeg",
                       width=1200,
                       height=600,
                       scale=2
                    )
                    # top 10 company types in the city
                  vc = df['company_type'].value_counts()
                    # Take ONLY top 10
                  top_10 = vc.head(10)

                    # Force order (descending)
                  order = top_10.index.tolist()

                    # Plot
                  fig = px.histogram(
                        df[df['company_type'].isin(order)],  # filter to top 10 only
                        x='company_type',
                        category_orders={'company_type': order},
                        title=f'{location} Top 10 Company Types (Descending Order)'
                    )
                  output_folder = "static\images"
                #   os.makedirs(output_folder, exist_ok=True)

                  fig.write_image(
                     f"{output_folder}/image2.jpeg",
                        format="jpeg",
                        width=1100,
                        height=500,
                        scale=2
                  )
                except Exception as e:
                    print(e)
                else:    
                   return redirect("/visulization")  
            else:
                msg="please select the option to see the data"
                return render_template("home.html",mssg=msg)          
    return render_template("home.html")
@app.route("/table",methods=["GET","POST"])
def table():
    return render_template("table.html")
@app.route("/visulization",methods=["GET","POST"])
def visulization():
    return render_template("visulization.html")
app.run()

 