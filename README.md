# Sales Analytics Dashboard

Welcome to the **Sales Analytics Dashboard**, an interactive Streamlit-based web application for visualizing and analyzing sales data. This dashboard provides insightful KPIs, advanced filtering options, and customizable visualizations to help businesses monitor their performance efficiently.

## 🌟 Features

### 1. **Dynamic Filters**
- Filter data by **Year**, **Retailer**, **Company**, and **Financial Month** using intuitive multi-select options.
- Option to **Select All** for holistic analysis.

### 2. **Key Performance Indicators (KPIs)**
- **Total Sales**: Aggregate sales amount.
- **Total Margin**: Cumulative profit margin.
- **Total Transactions**: Number of transactions.
- **Margin Percentage**: Profit margin percentage.

### 3. **Visualizations**
- **Month-on-Month Sales**: A dynamic line chart comparing sales across different financial years.
- **Retailer Revenue Analysis**: Bar chart visualizing the number of retailers contributing to different percentage revenue brackets.
- **Company Revenue Analysis**: Bar chart showing the number of companies contributing to various percentage revenue brackets.

## 🛠️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/sales-analytics-dashboard.git
   cd sales-analytics-dashboard
   ```

2. **Install Dependencies**
   Ensure you have Python 3.7+ installed. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Data**
   - Place your dataset (`data.csv`) in the root directory.
   - Ensure the dataset contains columns: `Date`, `Retailer`, `Company`, `Amount`, `Margin`, etc.

4. **Run the Dashboard**
   ```bash
   streamlit run main.py
   ```

5. **Access the Dashboard**
   Open the URL provided by Streamlit (e.g., `http://localhost:8501`) in your browser.

## 📊 Sample Dataset Structure
| Date       | Retailer     | Company     | Amount | Margin |  
|------------|--------------|-------------|--------|--------|  
| 2024-01-15 | Retailer A   | Company X   | 5000   | 500    |  
| 2024-02-10 | Retailer B   | Company Y   | 7000   | 700    |  

## 📈 Key Functionalities

### 1. **Time Features**
- Extract year, month, day, financial month, and financial year from the `Date` column for enhanced filtering.

### 2. **Revenue Analysis**
- **Retailer Revenue**: Highlights the top retailers contributing to specified revenue percentages.
- **Company Revenue**: Identifies the top companies driving revenue.

### 3. **Custom Metrics**
- Dynamic calculations for KPIs like `Margin Percentage` and real-time updates based on filters.

## 🤝 Contributing
Contributions are welcome! If you find a bug or have suggestions for improvements:
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request.

## 🚀 Live Demo
Check out the live demo: [Sales Analytics Dashboard](https://sales--analysis--dashboard.streamlit.app/)

---

🎉 **Thank you for visiting!** We hope this dashboard helps you unlock valuable insights from your sales data.
