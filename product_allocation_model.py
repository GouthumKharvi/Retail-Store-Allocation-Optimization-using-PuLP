
import pulp
import pandas as pd

# Load your dataframe here (adjust path)
df = pd.read_csv(r'C:\Users\Gouthum\Downloads\Retail Projects\retail_data.csv')

# Create the model
model = pulp.LpProblem("Product_Allocation", pulp.LpMinimize)

# Create variables for each product-city combination
variables = {(prod, city): pulp.LpVariable(f"x_{prod}_{city}", lowBound=0, cat='Integer')
             for prod, city in zip(df['products'], df['City'])}

# Add demand constraints per city
for store in df['City'].unique():
    demand = df[df['City'] == store]['products'].count()
    model += pulp.lpSum([
        variables[(prod, store)]
        for prod in df[df['City'] == store]['products']
        if (prod, store) in variables
    ]) >= demand, f"Demand_Constraint_{store}"

# Save or solve model here as needed
