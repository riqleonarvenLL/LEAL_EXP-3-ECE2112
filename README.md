# 🚗 Riqleon Arven King M. LEAL
# 🔬 Experiment 3 - Python Data Analysis

# 📘 I. Intended Learning Outcomes:
1. 🧠 To identify the codes and functions incorporated in the Pandas library
2. 🛠️ To be able to apply and use the different codes and functions in creating a Python program using the Pandas library

# 📋 II. Instructions:
📝 Write a Python script/code in the Jupyter Notebook to do the given problems. 
📤 You may submit your Jupyter notebook in the dedicated submission bin.

📂 For this programming assignment, download the following file and save it to your default user folder:
🔗 http://bit.ly/Cars_file

---

### 🚀 PROBLEM 1: Save your file as `Surname_Pandas-P1.py`

Using knowledge obtained from the experiment and demonstrations:

#### ✅ a. Load the corresponding `.csv` file into a data frame named `cars` using pandas
#### ✅ b. Display the first five and last five rows of the resulting `cars` DataFrame

🔧 Sample Code:

```python
import pandas as pd  # 🐼 Importing pandas

# 📥 Load the CSV file
cars = pd.read_csv("Cars.csv")  # Make sure the CSV file is in the correct directory

# 👀 Display the first 5 rows
print("📌 First 5 rows of the dataset:")
print(cars.head())

# 🔚 Display the last 5 rows
print("\n📌 Last 5 rows of the dataset:")
print(cars.tail())
