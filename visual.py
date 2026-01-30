
# plot histogram using plotly 
# order = df['company_type'].value_counts().index.tolist()
# top 5 company in the city

# import pandas as pd
# import plotly.express as px
# import os
# df=pd.read_csv("Ahmedabaad.csv")

# Convert ratings to numeric
# df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')

# # Sort by rating (descending)
# df_sorted = df.sort_values(by='ratings', ascending=False)

# # Fetch top 5 companies
# top_5 = df_sorted.head(5)

# # Force descending order on x-axis
# order = top_5['company name'].tolist()

# # Plot histogram
# fig = px.histogram(
#     top_5,
#     x='company name',
#     y='ratings',
#     category_orders={'company name': order},
#     title='Top 5 Companies by Rating',
#     labels={
#         'company name': 'Company Name',
#         'ratings': 'Ratings'
#     }
# )

# output_folder = "charts"
# os.makedirs(output_folder, exist_ok=True)

# fig.write_image(
#     f"{output_folder}/top_5_companies_by_rating.jpeg",
#     format="jpeg",
#     width=1200,
#     height=600,
#     scale=2
# )

# top 10 company types in the city

# vc = df['company_type'].value_counts()
# Take ONLY top 10
# top_10 = vc.head(10)

# Force order (descending)
# order = top_10.index.tolist()

# Plot
# fig = px.histogram(
#     df[df['company_type'].isin(order)],  # filter to top 10 only
#     x='company_type',
#     category_orders={'company_type': order},
#     title='Top 10 Company Types (Descending Order)'
# )
# output_folder = "charts"
# os.makedirs(output_folder, exist_ok=True)
# fig.write_image(
#     f"{output_folder}/top_10_companies_in_city.jpeg",
#     format="jpeg",
#     width=1200,
#     height=600,
#     scale=2
# )


 