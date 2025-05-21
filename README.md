# Retail Store Allocation Optimization using PuLP

This project solves a supply chain optimization problem using **Linear Programming (LP)** with the **PuLP** library in Python. It aims to allocate inventory from warehouses to retail stores in an optimal way that minimizes shipping costs while meeting demand.

--- 

## Problem Statement

A company wants to distribute different products from multiple warehouses to various stores. Each warehouse has limited stock, each store has demand, and each product has a shipping cost from each warehouse to each store. The goal is to determine the optimal distribution plan.

---

## Dataset

The dataset includes:
- `Demand.csv`: Demand of products at each store.
- `Supply.csv`: Inventory available at each warehouse.
- `ShippingCost.csv`: Cost of shipping from each warehouse to each store.

---

## Technologies Used

- Python 3.x
- PuLP (Linear Programming)
- Pandas
- Jupyter Notebook

---

## Project Structure

retail-pulp-optimization/
│
├── data/
│ ├── Demand.csv
│ ├── Supply.csv
│ └── ShippingCost.csv
│
├── pulp_optimization.ipynb
└── README.md


---

## How to Run

1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Run `pulp_optimization.ipynb` notebook.

---

## Solution Steps

1. Load and explore the data.
2. Define LP problem: Minimize cost, subject to constraints.
3. Create decision variables.
4. Add supply and demand constraints.
5. Solve using `pulp.LpProblem`.
6. Output the optimized allocation.

---

## Results

The output includes the optimal allocation plan and total minimized shipping cost.






# Retail Supply Optimization using Gurobi & PySpark

This project tackles a retail supply chain optimization problem using **Gurobi Optimizer** integrated with **PySpark** for distributed processing. The objective is to find the best product allocation plan from multiple warehouses to multiple stores while minimizing total shipping cost.

---

## Problem Statement

A retailer has a network of warehouses and stores. Each warehouse has a limited supply, and each store has a demand for products. The cost to ship each product from warehouse to store is provided. The goal is to minimize overall shipping cost under supply and demand constraints.

---

## Dataset

Same dataset as in Project 1:
- `Demand.csv`
- `Supply.csv`
- `ShippingCost.csv`

---

## Technologies Used

- Python 3.x
- Gurobi Optimizer
- PySpark (Spark DataFrames)
- Pandas
- Jupyter Notebook

---

## Project Structure
retail-gurobi-pyspark-optimization/
│
├── data/
│ ├── Demand.csv
│ ├── Supply.csv
│ └── ShippingCost.csv
│
├── gurobi_pyspark_optimization.ipynb
└── README.md


---

## How to Run

1. Clone this repo.
2. Install Gurobi and get a license: https://www.gurobi.com/downloads/
3. Install Spark and dependencies:


pip install pyspark
pip install gurobipy


4. Run the notebook: `gurobi_pyspark_optimization.ipynb`

---

## Solution Steps

1. Load data using PySpark.
2. Convert Spark DataFrames to dictionaries.
3. Initialize Gurobi model.
4. Define decision variables and constraints.
5. Solve the optimization problem.
6. Output the optimal shipping plan.

---

## Results

- Displays product allocation for each warehouse-store pair.
- Shows minimized total shipping cost.

---

## License

MIT License

