# E-commerce Data Analysis & Visualization  

## Overview  
This project focuses on analyzing and visualizing data on the largest Internet companies by revenue and market capitalization. The dataset is extracted from Wikipedia and processed to uncover industry trends.  

## Dataset  
The dataset includes information on major Internet companies, such as:  
- **Company Name**  
- **Revenue (in USD billions)**  
- **Market Capitalization**  
- **Employees**  
- **Headquarters Location**  
- **Founded Year**  
- **Industry**  

## Project Workflow  
1. **Web Scraping:** Extract data from Wikipedia using BeautifulSoup.  
2. **Data Cleaning:** Process and structure the dataset using Pandas.  
3. **Exploratory Data Analysis (EDA):** Identify key insights and trends.  
4. **Visualization:** Present findings through a Streamlit interactive dashboard.  

## Tech Stack  
- **Python** (for data processing & analysis)  
- **BeautifulSoup** (for web scraping)  
- **Pandas & NumPy** (for data manipulation)  
- **Matplotlib & Seaborn** (for visualization)  
- **Streamlit** (for interactive dashboards)  

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
   python src/scrape_data.py
   ```
5. Start the Streamlit dashboard:
   ```bash
   streamlit run src/streamlit_internet_companies.py
   ```

## Usage
- Scrape and update the dataset from Wikipedia.
- Perform exploratory data analysis (EDA).
- View insights interactively using the Streamlit dashboard.


## Contributing
Contributions are welcome! Feel free to fork this repository and submit improvements.

## License
This project is licensed under the MIT License.

---
