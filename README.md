# 🧮 BCGX — Financial Data Analysis & Chatbot API

> **Author:** *Vaibhav Mohanty*  
> **Tools:** `Flask`, `Pandas`, `Python 3.x`

---

## 🧠 Abstract

This project combines **data analytics** and **API-based query handling** using `Flask` and `Pandas`.  
It computes year-over-year **growth metrics** for multiple companies — including:

- Revenue Growth (%)
- Net Income Growth (%)
- Assets Growth (%)
- Liabilities Growth (%)
- Cash Flow Growth (%)

All results are served through a **chat-based Flask API** for easy interaction.

---

## ⚙️ Methodology

### **Step 1: Data Loading**
Use Pandas to load your financial dataset.

```python
df = pd.read_csv('path_to_your_csv_file.csv')

```


Step 2: Data Cleaning

Check for missing or inconsistent values before performing calculations.
```python
print(df.isnull().sum())

# Drop rows with missing data (optional)
df.dropna(inplace=True)
```

✅ Explanation:

Ensures no null or invalid entries distort growth calculations.

Dropping rows maintains data integrity across yearly comparisons.

Step 3: Growth Calculations

Compute Year-over-Year (YoY) growth for multiple financial indicators.
```python
# Example: Total Revenue Growth
df['Revenue Growth (%)'] = df.groupby('Company')['Total Revenue'].pct_change() * 100

# Repeat for other metrics
df['Net Income Growth (%)'] = df.groupby('Company')['Net Income'].pct_change() * 100
df['Assets Growth (%)'] = df.groupby('Company')['Total Assets'].pct_change() * 100
df['Liabilities Growth (%)'] = df.groupby('Company')['Total Liabilities'].pct_change() * 100
df['Cash Flow Growth (%)'] = df.groupby('Company')['Operating Cash Flow'].pct_change() * 100
```

✅ Explanation:

.pct_change() computes percentage change year over year.

Multiplying by 100 converts values to a percentage format.


Step 4: Aggregation of Growth Metrics

Calculate company-wise average growth statistics.
```python
summary = df.groupby('Company')[[
    'Revenue Growth (%)',
    'Net Income Growth (%)',
    'Assets Growth (%)',
    'Liabilities Growth (%)',
    'Cash Flow Growth (%)'
]].mean().reset_index()

print(summary)

```
✅ Explanation:

Groups metrics by company and averages their growth trends.




Step 5: Exporting Processed Data

Save the processed dataset and summary results.

df.to_csv('updated_financial_data.csv', index=False)
summary.to_csv('summary_growth_statistics.csv', index=False)


✅ Explanation:

Saves both detailed and summarized results for later use or reporting.

Step 6: Building the Flask API

Create an API endpoint for querying analytical summaries.
```python

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get("query", "").lower()

    if "revenue" in query:
        response = summary[['Company', 'Revenue Growth (%)']].to_dict(orient='records')
    elif "net income" in query:
        response = summary[['Company', 'Net Income Growth (%)']].to_dict(orient='records')
    else:
        response = {"message": "Sorry, I didn't understand the query."}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```

✅ Explanation:

Handles POST requests to /chat.

Returns financial metrics based on the query keyword.

Step 7: Testing the API
Use Postman or curl to test your Flask endpoint.
```cmd
curl -X POST http://127.0.0.1:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"query": "show total revenue"}'
```
```json
Expected response:

{
  "Company A": 123456789,
  "Company B": 987654321
}
```

✅ Explanation:

Sends a query to the API and retrieves financial results in JSON format.

Step 8: Project Structure
📦 Financial-Data-Analyzer
│
├── app.py                     # Flask backend for chatbot API
├── BCGX_pynb.ipynb            # Jupyter notebook for data exploration
├── updated_financial_data.csv # Processed dataset output
├── requirements.txt           # Dependency file
└── README.md                  # Project documentation

Step 9: Installation Guide
1. Clone the Repository
git clone https://github.com/yourusername/financial-data-analyzer.git
cd financial-data-analyzer

2. Set Up Virtual Environment
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Flask App
python app.py


Then open your browser and go to:

http://127.0.0.1:5000

Step 10: Requirements File
Flask==3.0.3
pandas==2.2.3
numpy==1.26.4


Optional (for Jupyter Notebook support):

jupyterlab==4.2.5
ipykernel==6.29.5

Step 11: Example Notebook Output
```python 
print(df.head())

print("Average Growth Statistics:")
print(summary)

for company in df['Company'].unique():
    print(f"\n{company} Revenue Trend:")
    print(df[df['Company'] == company][['Year', 'Total Revenue']])
```

🧾 Output:

Displays company-wise financial growth.

Generates updated_financial_data.csv.

Prints detailed revenue trends for each company.

Step 12: Future Enhancements

Interactive dashboard using Plotly or Streamlit

NLP-powered query handling for flexible questions

Automated PDF report generation per company

👨‍💻 Author

Vaibhav Mohanty
Data Analyst | AI Developer | Machine Learning Enthusiast
