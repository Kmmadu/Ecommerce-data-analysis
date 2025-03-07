# E-commerce Data Analysis & Forecasting

## Overview
This project involves web scraping, analyzing, and forecasting data on the largest Internet companies by revenue and market capitalization. The dataset is extracted from Wikipedia and processed for insights into industry trends.

## Dataset
The dataset includes information on major e-commerce companies, such as:
- **Company Name**
- **Revenue (in USD billions)**
- **Financial Year**
- **Employees**
- **Market Capitalization**
- **Headquarters Location**
- **Founded Year**
- **Industry**

## Project Workflow
1. **Web Scraping:** Extract data from Wikipedia using BeautifulSoup.
2. **Data Cleaning:** Process and structure the dataset using Pandas.
3. **Exploratory Data Analysis (EDA):** Identify key insights and trends.
4. **Forecasting:** Use machine learning models to predict revenue growth.
5. **Visualization:** Present findings through Streamlit and Power BI dashboards.

## Tech Stack
- **Python** (for data processing & analysis)
- **BeautifulSoup** (for web scraping)
- **Pandas & NumPy** (for data manipulation)
- **Matplotlib & Seaborn** (for visualization)
- **Scikit-learn** (for predictive modeling)
- **Streamlit** (for interactive dashboards)
- **Power BI** (for business intelligence visualization)

## Installation
To set up the project locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/Kmmadu/ecommerce-data-analysis.git
   cd ecommerce-data-analysis
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the scraping script:
   ```bash
   python src/scraper.py
   ```
5. Start the Streamlit dashboard:
   ```bash
   streamlit run dashboards/app.py
   ```

## Usage
- Run the scraper to fetch and update the dataset.
- Perform EDA to understand industry trends.
- Use ML models to forecast revenue growth.
- Deploy dashboards for interactive insights.

## Contributing
Feel free to fork this repository and make improvements. Contributions are welcome!

## License
This project is licensed under the MIT License.

---
