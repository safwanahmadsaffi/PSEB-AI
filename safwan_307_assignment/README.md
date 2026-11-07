# Safwan — Training ID 307 | Sunday Project

This ZIP contains the runnable notebook and all required CSV inputs/outputs for the Data Quality, Insights & CSV Operations assignment.

## Files
- `Safwan_307_Assignment.ipynb` — executed notebook with clearly marked Part A and Part B.
- `sales_raw.csv` — original input.
- `cleaned_sales.csv` — cleaned Part A output.
- `sales_updated.csv` — Part B output, including the 5% tax and Books price adjustment.
- `revenue_by_region.png`, `revenue_by_category.png` — labeled Part A charts.

## Run
Place the notebook and CSV files in the same folder, then run all cells in Jupyter or upload the files to Google Colab. Dependencies: Python 3, pandas, and matplotlib. All paths are relative.

## Cleaning notes and results
The source contained 21 records. One repeated transaction ID was removed; one invalid date and one negative-quantity transaction were excluded. Missing/invalid quantity and unit prices were filled with category medians; missing region is labeled `Unknown`; text was trimmed and standardized. The unusual $10,000 stationery price was retained and flagged as an outlier rather than removed without evidence. The cleaned data has 18 rows and total calculated revenue of $14,775. North and Stationery have the highest grouped revenues, chiefly due to that flagged record.

Part B increases Books unit prices by 10%, recalculates revenue and 5% tax, removes the first transaction ID in the cleaned dataset (1001), and demonstrates adding then dropping `review_status`.

## GitHub repository
Repository URL was not supplied. Add your own public/private repository link here before submitting: https://github.com/safwanahmadsaffi/PSEB-AI/tree/main/safwan_307_assignment.
