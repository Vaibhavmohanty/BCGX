{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b6aa79c-9bdf-4991-beb0-8b8588a998d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "\n",
    "df = pd.read_csv('path_to_your_csv_file.csv')\n",
    "\n",
    "print(df.head())\n",
    "\n",
    "df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue'].pct_change() * 100\n",
    "df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income'].pct_change() * 100\n",
    "df['Assets Growth (%)'] = df.groupby(['Company'])['Total Assets'].pct_change() * 100\n",
    "df['Liabilities Growth (%)'] = df.groupby(['Company'])['Total Liabilities'].pct_change() * 100\n",
    "df['Cash Flow Growth (%)'] = df.groupby(['Company'])['Cash Flow from Operating Activities'].pct_change() * 100\n",
    "\n",
    "summary = df.groupby('Company')[['Revenue Growth (%)', 'Net Income Growth (%)',\n",
    "                                 'Assets Growth (%)', 'Liabilities Growth (%)',\n",
    "                                 'Cash Flow Growth (%)']].mean()\n",
    "\n",
    "print(\"Average Growth Statistics:\")\n",
    "print(summary)\n",
    "\n",
    "for company in df['Company'].unique():\n",
    "    print(f\"\\n{company} Revenue Trend:\")\n",
    "    print(df[df['Company'] == company][['Year', 'Total Revenue']])\n",
    "\n",
    "df.to_csv('updated_financial_data.csv', index=False)\n",
    "\n",
    "print(\"\\nAnalysis Complete. The data has been processed, and results saved to 'updated_financial_data.csv'.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
