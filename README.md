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
import pandas as pd  # Import the pandas library
# Load the CSV file into a  named 'cars'
cars = pd.read_csv("cars.csv")
# Concatenate the first 5 and last 5 rows
p1 = pd.concat([cars.head(), cars.tail()])
# Display the result
print(p1)

```Output```

                Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  \
0           Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1   
1       Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1   
2          Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1   
3      Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0   
4   Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0   
27       Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.90   1   1   
28     Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.50   0   1   
29       Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.50   0   1   
30      Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.60   0   1   
31         Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.60   1   1   

    gear  carb  
0      4     4  
1      4     4  
2      4     1  
3      3     1  
4      3     2  
27     5     2  
28     5     4  
29     5     6  
30     5     8  
31     4     2  
```

