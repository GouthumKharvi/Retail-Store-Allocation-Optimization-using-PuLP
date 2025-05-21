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

---

## License

MIT License
