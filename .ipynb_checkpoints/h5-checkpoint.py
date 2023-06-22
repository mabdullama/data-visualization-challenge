{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Pymaceuticals Inc.\n",
    "---\n",
    "\n",
    "### Analysis\n",
    "\n",
    "- Add your analysis here.\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mouse ID</th>\n",
       "      <th>Timepoint</th>\n",
       "      <th>Tumor Volume (mm3)</th>\n",
       "      <th>Metastatic Sites</th>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age_months</th>\n",
       "      <th>Weight (g)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>b128</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Capomulin</td>\n",
       "      <td>Female</td>\n",
       "      <td>9</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>f932</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Male</td>\n",
       "      <td>15</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>g107</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Female</td>\n",
       "      <td>2</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>a457</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Female</td>\n",
       "      <td>11</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>c819</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mouse ID  Timepoint  Tumor Volume (mm3)  Metastatic Sites Drug Regimen  \\\n",
       "0     b128          0                45.0                 0    Capomulin   \n",
       "1     f932          0                45.0                 0     Ketapril   \n",
       "2     g107          0                45.0                 0     Ketapril   \n",
       "3     a457          0                45.0                 0     Ketapril   \n",
       "4     c819          0                45.0                 0     Ketapril   \n",
       "\n",
       "      Sex  Age_months  Weight (g)  \n",
       "0  Female           9          22  \n",
       "1    Male          15          29  \n",
       "2  Female           2          29  \n",
       "3  Female          11          30  \n",
       "4    Male          21          25  "
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import scipy.stats as st\n",
    "\n",
    "# Study data files\n",
    "mouse_metadata_path = \"data/Mouse_metadata.csv\"\n",
    "study_results_path = \"data/Study_results.csv\"\n",
    "\n",
    "# Read the mouse data and the study results\n",
    "mouse_metadata = pd.read_csv(mouse_metadata_path)\n",
    "study_results = pd.read_csv(study_results_path)\n",
    "\n",
    "# Combine the data into a single DataFrame\n",
    "combined_data = pd.merge(study_results, mouse_metadata, on='Mouse ID', how='left')\n",
    "\n",
    "# Display the data table for preview\n",
    "combined_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "249"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Checking the number of mice.\n",
    "combined_data['Mouse ID'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Our data should be uniquely identified by Mouse ID and Timepoint\n",
    "# Get the duplicate mice by ID number that shows up for Mouse ID and Timepoint. \n",
    "\n",
    "# Find duplicate rows based on Mouse ID and Timepoint\n",
    "duplicate_mice = combined_data[combined_data.duplicated(['Mouse ID', 'Timepoint'], keep=False)]\n",
    "\n",
    "# Get the list of duplicate Mouse IDs\n",
    "duplicate_mouse_ids = duplicate_mice['Mouse ID'].unique()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mouse ID</th>\n",
       "      <th>Timepoint</th>\n",
       "      <th>Tumor Volume (mm3)</th>\n",
       "      <th>Metastatic Sites</th>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age_months</th>\n",
       "      <th>Weight (g)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>107</th>\n",
       "      <td>g989</td>\n",
       "      <td>0</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>137</th>\n",
       "      <td>g989</td>\n",
       "      <td>0</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>329</th>\n",
       "      <td>g989</td>\n",
       "      <td>5</td>\n",
       "      <td>48.786801</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>360</th>\n",
       "      <td>g989</td>\n",
       "      <td>5</td>\n",
       "      <td>47.570392</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>620</th>\n",
       "      <td>g989</td>\n",
       "      <td>10</td>\n",
       "      <td>51.745156</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>681</th>\n",
       "      <td>g989</td>\n",
       "      <td>10</td>\n",
       "      <td>49.880528</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>815</th>\n",
       "      <td>g989</td>\n",
       "      <td>15</td>\n",
       "      <td>51.325852</td>\n",
       "      <td>1</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>869</th>\n",
       "      <td>g989</td>\n",
       "      <td>15</td>\n",
       "      <td>53.442020</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>950</th>\n",
       "      <td>g989</td>\n",
       "      <td>20</td>\n",
       "      <td>55.326122</td>\n",
       "      <td>1</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1111</th>\n",
       "      <td>g989</td>\n",
       "      <td>20</td>\n",
       "      <td>54.657650</td>\n",
       "      <td>1</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1195</th>\n",
       "      <td>g989</td>\n",
       "      <td>25</td>\n",
       "      <td>56.045564</td>\n",
       "      <td>1</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1380</th>\n",
       "      <td>g989</td>\n",
       "      <td>30</td>\n",
       "      <td>59.082294</td>\n",
       "      <td>1</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1592</th>\n",
       "      <td>g989</td>\n",
       "      <td>35</td>\n",
       "      <td>62.570880</td>\n",
       "      <td>2</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Mouse ID  Timepoint  Tumor Volume (mm3)  Metastatic Sites Drug Regimen  \\\n",
       "107      g989          0           45.000000                 0     Propriva   \n",
       "137      g989          0           45.000000                 0     Propriva   \n",
       "329      g989          5           48.786801                 0     Propriva   \n",
       "360      g989          5           47.570392                 0     Propriva   \n",
       "620      g989         10           51.745156                 0     Propriva   \n",
       "681      g989         10           49.880528                 0     Propriva   \n",
       "815      g989         15           51.325852                 1     Propriva   \n",
       "869      g989         15           53.442020                 0     Propriva   \n",
       "950      g989         20           55.326122                 1     Propriva   \n",
       "1111     g989         20           54.657650                 1     Propriva   \n",
       "1195     g989         25           56.045564                 1     Propriva   \n",
       "1380     g989         30           59.082294                 1     Propriva   \n",
       "1592     g989         35           62.570880                 2     Propriva   \n",
       "\n",
       "         Sex  Age_months  Weight (g)  \n",
       "107   Female          21          26  \n",
       "137   Female          21          26  \n",
       "329   Female          21          26  \n",
       "360   Female          21          26  \n",
       "620   Female          21          26  \n",
       "681   Female          21          26  \n",
       "815   Female          21          26  \n",
       "869   Female          21          26  \n",
       "950   Female          21          26  \n",
       "1111  Female          21          26  \n",
       "1195  Female          21          26  \n",
       "1380  Female          21          26  \n",
       "1592  Female          21          26  "
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Optional: Get all the data for the duplicate mouse ID.\n",
    "\n",
    "# Filter the merged DataFrame for duplicate Mouse IDs\n",
    "duplicate_data = combined_data[combined_data['Mouse ID'].isin(duplicate_mouse_ids)]\n",
    "\n",
    "duplicate_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mouse ID</th>\n",
       "      <th>Timepoint</th>\n",
       "      <th>Tumor Volume (mm3)</th>\n",
       "      <th>Metastatic Sites</th>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age_months</th>\n",
       "      <th>Weight (g)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>b128</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Capomulin</td>\n",
       "      <td>Female</td>\n",
       "      <td>9</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>f932</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Male</td>\n",
       "      <td>15</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>g107</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Female</td>\n",
       "      <td>2</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>a457</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Female</td>\n",
       "      <td>11</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>c819</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mouse ID  Timepoint  Tumor Volume (mm3)  Metastatic Sites Drug Regimen  \\\n",
       "0     b128          0                45.0                 0    Capomulin   \n",
       "1     f932          0                45.0                 0     Ketapril   \n",
       "2     g107          0                45.0                 0     Ketapril   \n",
       "3     a457          0                45.0                 0     Ketapril   \n",
       "4     c819          0                45.0                 0     Ketapril   \n",
       "\n",
       "      Sex  Age_months  Weight (g)  \n",
       "0  Female           9          22  \n",
       "1    Male          15          29  \n",
       "2  Female           2          29  \n",
       "3  Female          11          30  \n",
       "4    Male          21          25  "
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a clean DataFrame by dropping the duplicate mouse by its ID.\n",
    "cleaned_data = combined_data.drop_duplicates(subset=['Mouse ID'])\n",
    "\n",
    "cleaned_data .head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "249"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Checking the number of mice in the clean DataFrame.\n",
    "cleaned_data['Mouse ID'].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Summary Statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mean Tumor Volume</th>\n",
       "      <th>Median Tumor Volume</th>\n",
       "      <th>Tumor Volume Variance</th>\n",
       "      <th>Tumor Volume Std. Dev.</th>\n",
       "      <th>Tumor Volume Std. Err.</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Capomulin</th>\n",
       "      <td>40.675741</td>\n",
       "      <td>41.557809</td>\n",
       "      <td>24.947764</td>\n",
       "      <td>4.994774</td>\n",
       "      <td>0.329346</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ceftamin</th>\n",
       "      <td>52.591172</td>\n",
       "      <td>51.776157</td>\n",
       "      <td>39.290177</td>\n",
       "      <td>6.268188</td>\n",
       "      <td>0.469821</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Infubinol</th>\n",
       "      <td>52.884795</td>\n",
       "      <td>51.820584</td>\n",
       "      <td>43.128684</td>\n",
       "      <td>6.567243</td>\n",
       "      <td>0.492236</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ketapril</th>\n",
       "      <td>55.235638</td>\n",
       "      <td>53.698743</td>\n",
       "      <td>68.553577</td>\n",
       "      <td>8.279709</td>\n",
       "      <td>0.603860</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Naftisol</th>\n",
       "      <td>54.331565</td>\n",
       "      <td>52.509285</td>\n",
       "      <td>66.173479</td>\n",
       "      <td>8.134708</td>\n",
       "      <td>0.596466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Placebo</th>\n",
       "      <td>54.033581</td>\n",
       "      <td>52.288934</td>\n",
       "      <td>61.168083</td>\n",
       "      <td>7.821003</td>\n",
       "      <td>0.581331</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Propriva</th>\n",
       "      <td>52.322552</td>\n",
       "      <td>50.854632</td>\n",
       "      <td>42.351070</td>\n",
       "      <td>6.507770</td>\n",
       "      <td>0.512884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ramicane</th>\n",
       "      <td>40.216745</td>\n",
       "      <td>40.673236</td>\n",
       "      <td>23.486704</td>\n",
       "      <td>4.846308</td>\n",
       "      <td>0.320955</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Stelasyn</th>\n",
       "      <td>54.233149</td>\n",
       "      <td>52.431737</td>\n",
       "      <td>59.450562</td>\n",
       "      <td>7.710419</td>\n",
       "      <td>0.573111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Zoniferol</th>\n",
       "      <td>53.236507</td>\n",
       "      <td>51.818479</td>\n",
       "      <td>48.533355</td>\n",
       "      <td>6.966589</td>\n",
       "      <td>0.516398</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Mean Tumor Volume  Median Tumor Volume  Tumor Volume Variance  \\\n",
       "Drug Regimen                                                                  \n",
       "Capomulin             40.675741            41.557809              24.947764   \n",
       "Ceftamin              52.591172            51.776157              39.290177   \n",
       "Infubinol             52.884795            51.820584              43.128684   \n",
       "Ketapril              55.235638            53.698743              68.553577   \n",
       "Naftisol              54.331565            52.509285              66.173479   \n",
       "Placebo               54.033581            52.288934              61.168083   \n",
       "Propriva              52.322552            50.854632              42.351070   \n",
       "Ramicane              40.216745            40.673236              23.486704   \n",
       "Stelasyn              54.233149            52.431737              59.450562   \n",
       "Zoniferol             53.236507            51.818479              48.533355   \n",
       "\n",
       "              Tumor Volume Std. Dev.  Tumor Volume Std. Err.  \n",
       "Drug Regimen                                                  \n",
       "Capomulin                   4.994774                0.329346  \n",
       "Ceftamin                    6.268188                0.469821  \n",
       "Infubinol                   6.567243                0.492236  \n",
       "Ketapril                    8.279709                0.603860  \n",
       "Naftisol                    8.134708                0.596466  \n",
       "Placebo                     7.821003                0.581331  \n",
       "Propriva                    6.507770                0.512884  \n",
       "Ramicane                    4.846308                0.320955  \n",
       "Stelasyn                    7.710419                0.573111  \n",
       "Zoniferol                   6.966589                0.516398  "
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen\n",
    "\n",
    "# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: \n",
    "# mean, median, variance, standard deviation, and SEM of the tumor volume. \n",
    "\n",
    "mean = combined_data.groupby('Drug Regimen')['Tumor Volume (mm3)'].mean()\n",
    "median = combined_data.groupby('Drug Regimen')['Tumor Volume (mm3)'].median()\n",
    "variance = combined_data.groupby('Drug Regimen')['Tumor Volume (mm3)'].var()\n",
    "standard_devition = combined_data.groupby('Drug Regimen')['Tumor Volume (mm3)'].std()\n",
    "SEM = combined_data.groupby('Drug Regimen')['Tumor Volume (mm3)'].sem()\n",
    "\n",
    "# Assemble the resulting series into a single summary DataFrame.\n",
    "summary_stats = pd.DataFrame({\"Mean Tumor Volume\":mean,\n",
    "                          \"Median Tumor Volume\":median,\n",
    "                          \"Tumor Volume Variance\":variance,\n",
    "                          \"Tumor Volume Std. Dev.\":standard_devition,\n",
    "                          \"Tumor Volume Std. Err.\":SEM})\n",
    "\n",
    "\n",
    "summary_stats"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>mean</th>\n",
       "      <th>median</th>\n",
       "      <th>var</th>\n",
       "      <th>std</th>\n",
       "      <th>sem</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Capomulin</th>\n",
       "      <td>40.675741</td>\n",
       "      <td>41.557809</td>\n",
       "      <td>24.947764</td>\n",
       "      <td>4.994774</td>\n",
       "      <td>0.329346</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ceftamin</th>\n",
       "      <td>52.591172</td>\n",
       "      <td>51.776157</td>\n",
       "      <td>39.290177</td>\n",
       "      <td>6.268188</td>\n",
       "      <td>0.469821</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Infubinol</th>\n",
       "      <td>52.884795</td>\n",
       "      <td>51.820584</td>\n",
       "      <td>43.128684</td>\n",
       "      <td>6.567243</td>\n",
       "      <td>0.492236</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ketapril</th>\n",
       "      <td>55.235638</td>\n",
       "      <td>53.698743</td>\n",
       "      <td>68.553577</td>\n",
       "      <td>8.279709</td>\n",
       "      <td>0.603860</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Naftisol</th>\n",
       "      <td>54.331565</td>\n",
       "      <td>52.509285</td>\n",
       "      <td>66.173479</td>\n",
       "      <td>8.134708</td>\n",
       "      <td>0.596466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Placebo</th>\n",
       "      <td>54.033581</td>\n",
       "      <td>52.288934</td>\n",
       "      <td>61.168083</td>\n",
       "      <td>7.821003</td>\n",
       "      <td>0.581331</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Propriva</th>\n",
       "      <td>52.322552</td>\n",
       "      <td>50.854632</td>\n",
       "      <td>42.351070</td>\n",
       "      <td>6.507770</td>\n",
       "      <td>0.512884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ramicane</th>\n",
       "      <td>40.216745</td>\n",
       "      <td>40.673236</td>\n",
       "      <td>23.486704</td>\n",
       "      <td>4.846308</td>\n",
       "      <td>0.320955</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Stelasyn</th>\n",
       "      <td>54.233149</td>\n",
       "      <td>52.431737</td>\n",
       "      <td>59.450562</td>\n",
       "      <td>7.710419</td>\n",
       "      <td>0.573111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Zoniferol</th>\n",
       "      <td>53.236507</td>\n",
       "      <td>51.818479</td>\n",
       "      <td>48.533355</td>\n",
       "      <td>6.966589</td>\n",
       "      <td>0.516398</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   mean     median        var       std       sem\n",
       "Drug Regimen                                                     \n",
       "Capomulin     40.675741  41.557809  24.947764  4.994774  0.329346\n",
       "Ceftamin      52.591172  51.776157  39.290177  6.268188  0.469821\n",
       "Infubinol     52.884795  51.820584  43.128684  6.567243  0.492236\n",
       "Ketapril      55.235638  53.698743  68.553577  8.279709  0.603860\n",
       "Naftisol      54.331565  52.509285  66.173479  8.134708  0.596466\n",
       "Placebo       54.033581  52.288934  61.168083  7.821003  0.581331\n",
       "Propriva      52.322552  50.854632  42.351070  6.507770  0.512884\n",
       "Ramicane      40.216745  40.673236  23.486704  4.846308  0.320955\n",
       "Stelasyn      54.233149  52.431737  59.450562  7.710419  0.573111\n",
       "Zoniferol     53.236507  51.818479  48.533355  6.966589  0.516398"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# A more advanced method to generate a summary statistics table of mean, median, variance, standard deviation,\n",
    "# and SEM of the tumor volume for each regimen (only one method is required in the solution)\n",
    "\n",
    "# Using the aggregation method, produce the same summary statistics in a single line\n",
    "summary_df = combined_data.groupby('Drug Regimen')['Tumor Volume (mm3)'].agg(['mean', 'median', 'var', 'std', 'sem'])\n",
    "summary_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Bar and Pie Charts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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EVQoanPnzkVoaCi2bt2K3r17w8/PD+7u7oWZjYiIiKhYy/M8ahMnTkRMTAx27NiBV69eoUGDBqhTpw5WrFiB5OTkwsxIREREVCypPOFt/fr18euvvyIhIQEjRozA6tWrYW9vz7JGREREpGYqF7X3oqKiEBERgdjYWLi7u/O+NSIiIiI1U6moPXz4EMHBwahSpQq++uorWFhY4PTp0zh16hSMjIwKKyMRERFRsZTnwQRt27bF4cOH0bJlS/zwww9o164d9PQKNA0bEREREX1GnpvWvn37YGdnh7t372LGjBmYMWNGrsdFRUWpLRwRERFRcZbnohYYGFiYOYiIiIjoIyxqRERERDKV71GfRERERFS4WNSIiIiIZIpFjYiIiEimWNSIiIiIZIpFjYiIiEim8jTqc8mSJXn+hAEBAfkOQ0RERET/J09FLSQkROn5kydPkJqaCnNzcwDAy5cvYWxsjDJlyrCoEREREalJni59xsfHKx6zZ89GzZo1ERsbi+fPn+P58+eIjY2Fp6cnvv/++8LOS0RERFRsqHyP2rRp07B06VK4uLgotrm4uCAkJATfffedWsMRERERFWcqF7WEhARkZmbm2J6VlYVHjx6pJRQRERER5aOoNWvWDN988w0iIyMhiiIAIDIyEkOHDkXz5s3VHpCIiIiouFK5qK1evRply5ZFnTp1YGhoCAMDA9StWxd2dnb47bffCiMjERERUbGU50XZ37O2tsbevXtx/fp1XL16FaIowtXVFVWqVCmMfERERETFlspF7b0KFSpAFEVUqlQJenr5/jRERERE9AkqX/pMTU3FoEGDYGxsjGrVquHu3bsA3k10O3fuXLUHJCIiIiquVC5qU6ZMwcWLF3HkyBEYGhoqtjdv3hxbtmxRazgiIiKi4kzla5Y7duzAli1bUK9ePQiCoNju5uaGmzdvqjUcERERUXGm8hm1J0+eoEyZMjm2p6SkKBU3IiIiIioYlYvaF198gT179iievy9nv/76K+rXr6++ZERERETFnMqXPufMmYPWrVsjJiYGb9++xY8//ogrV67g5MmTiIiIKIyMRERERMWSymfUvL29cfz4caSmpqJSpUrYv38/bGxscPLkSdSuXbswMhIREREVSyoXNQDw8PDA2rVrcfnyZcTExGDDhg3w8PBQ+fP8+++/6NChA+zt7SEIAnbs2KG0XxRFBAUFwd7eHkZGRmjSpAmuXLmidEx6ejr8/f1hZWWFkiVLomPHjrh//35+3hYRERGRrKhc1Hx8fLBq1SokJSUV+MVTUlJQo0YNLFu2LNf98+fPx6JFi7Bs2TKcPXsWtra2aNGiBV69eqU4ZvTo0di+fTs2b96MY8eO4fXr12jfvj2ysrIKnI+IiIhISioXNQ8PD3z33XewtbVF165dsWPHDmRkZOTrxdu0aYNZs2ahS5cuOfaJoojFixdj6tSp6NKlC9zd3bF27VqkpqZi48aNAICkpCSsWrUKCxcuRPPmzVGrVi1s2LABly5dwoEDB/KViYiIiEguVC5qS5YswYMHD7Bz506Ympqif//+sLW1xZAhQ9Q6mCA+Ph6JiYlo2bKlYpuBgQEaN26MEydOAADOnTuHzMxMpWPs7e3h7u6uOCY36enpSE5OVnoQERERyU2+7lHT0dFBy5YtERoaikePHuGXX37BmTNn0LRpU7UFS0xMBADY2NgobbexsVHsS0xMRIkSJVC6dOlPHpObOXPmwMzMTPFwcHBQW24iIiIidclXUXsvMTERK1aswLx58xAdHQ0vLy915VL4eBJdURT/c2Ld/zpmypQpSEpKUjzu3bunlqxERERE6qRyUUtOTsaaNWvQokULODg4YPny5ejQoQOuX7+O06dPqy2Yra0tAOQ4M/b48WPFWTZbW1tkZGTgxYsXnzwmNwYGBihVqpTSg4iIiEhuVC5qNjY2mDp1KqpVq4YTJ07g2rVrCAwMhLOzs1qDVaxYEba2tggPD1dsy8jIQEREBLy9vQEAtWvXhr6+vtIxCQkJuHz5suIYIiIiIk2l0soEoijixx9/RJ8+fWBsbFzgF3/9+jVu3LiheB4fH48LFy7AwsIC5cuXx+jRoxEcHIzKlSujcuXKCA4OhrGxMXr16gUAMDMzw6BBgzBu3DhYWlrCwsIC48ePh4eHB5o3b17gfERERERSUrmojRw5Ej4+PqhcuXKBXzwyMhI+Pj6K52PHjgUA9O/fH6GhoZg4cSLS0tIwfPhwvHjxAnXr1sX+/fthamqq+JiQkBDo6emhW7duSEtLQ7NmzRAaGgpdXd0C5yMiIiKSkkpFTUdHB5UrV8azZ8/UUtSaNGkCURQ/uV8QBAQFBSEoKOiTxxgaGmLp0qVYunRpgfMQERERyYnK96jNnz8fEyZMwOXLlwsjDxERERH9fyqdUQOAPn36IDU1FTVq1ECJEiVgZGSktP/58+dqC0dERERUnKlc1BYvXlwIMYiIiIjoYyoXtf79+xdGDiIiIiL6SL5WJrh58ya+++479OzZE48fPwYA7Nu3D1euXFFrOCIiIqLiTOWiFhERAQ8PD5w+fRrbtm3D69evAQDR0dEIDAxUe0AiIiKi4krlojZ58mTMmjUL4eHhKFGihGK7j48PTp48qdZwRERERMWZykXt0qVL6Ny5c47t1tbWePbsmVpCEREREVE+ipq5uTkSEhJybD9//jzKli2rllBERERElI+i1qtXL0yaNAmJiYkQBAHZ2dk4fvw4xo8fj379+hVGRiIiIqJiSeWiNnv2bJQvXx5ly5bF69ev4ebmhkaNGsHb2xvfffddYWQkIiIiKpZUnkdNX18fv//+O77//ntERUUhOzsbtWrVUsvan0RERET0f1Quau85OTnByckJWVlZuHTpEl68eIHSpUurMxsRERFRsabypc/Ro0dj1apVAICsrCw0btwYnp6ecHBwwJEjR9Sdj4iIiKjYUrmo/fnnn6hRowYAYPfu3bh16xauXr2K0aNHY+rUqWoPSERERFRcqVzUnj59CltbWwDA3r170a1bN1SpUgWDBg3CpUuX1B6QiIiIqLhSuajZ2NggJiYGWVlZ2LdvH5o3bw4ASE1Nha6urtoDEhERERVXKg8mGDhwILp16wY7OzsIgoAWLVoAAE6fPo2qVauqPSARERFRcaVyUQsKCoK7uzvu3buHr7/+GgYGBgAAXV1dTJ48We0BiYiIiIqrfE3P8dVXX+XY1r9//wKHISIiIqL/o/I9agBw8OBBtG/fHpUqVYKzszPat2+PAwcOqDsbERERUbGmclFbtmwZWrduDVNTU4waNQoBAQEoVaoU2rZti2XLlhVGRiIiIqJiSeVLn3PmzEFISAhGjhyp2BYQEIAGDRpg9uzZStuJiIiIKP9UPqOWnJyM1q1b59jesmVLJCcnqyUUEREREeWjqHXs2BHbt2/PsX3nzp3o0KGDWkIRERERUR4vfS5ZskTxb1dXV8yePRtHjhxB/fr1AQCnTp3C8ePHMW7cuMJJSURERFQM5amohYSEKD0vXbo0YmJiEBMTo9hmbm6O1atX47vvvlNvQiIiIqJiKk9FLT4+vrBzEBEREdFH8jWPGvBucfZnz56pMwsRERERfUClovby5UuMGDECVlZWsLGxQZkyZWBlZYWRI0fi5cuXhRSRiIiIqHjK8zxqz58/R/369fHgwQP07t0brq6uEEURsbGxCA0NxcGDB3HixAmULl26MPMSERERFRt5LmozZ85EiRIlcPPmTdjY2OTY17JlS8ycOTPHwAMiIiIiyp88X/rcsWMHFixYkKOkAYCtrS3mz5+f6/xqRERERJQ/eS5qCQkJqFat2if3u7u7IzExUS2hiIiIiEiFomZlZYXbt29/cn98fDwsLS3VkYmIiIiIoEJRa926NaZOnYqMjIwc+9LT0zFt2rRc1wAlIiIiovzJ82CCGTNmwMvLC5UrV8aIESNQtWpVAEBMTAx+/vlnpKenY/369YUWlIiIiKi4yXNRK1euHE6ePInhw4djypQpEEURACAIAlq0aIFly5bBwcGh0IISERERFTd5LmoAULFiRfzzzz948eIF4uLiAADOzs6wsLAolHBERERExZlKRe290qVLo06dOurOQkREREQfyPdan0RERERUuFjUiIiIiGSKRY2IiIhIpvJU1Dw9PfHixQsA79b1TE1NLdRQRERERJTHohYbG4uUlBQA7+ZTe/36daGGIiIiIqI8jvqsWbMmBg4ciIYNG0IURSxYsAAmJia5Hjt9+nS1BiQiIiIqrvJU1EJDQxEYGIi///4bgiDgn3/+gZ5ezg8VBIFFjYiIiEhN8lTUXFxcsHnzZgCAjo4ODh48iDJlyhRqMCIiIqLiTuUJb7OzswsjBxERERF9JF8rE9y8eROLFy9GbGwsBEGAq6srRo0ahUqVKqk7HxEREVGxpfI8amFhYXBzc8OZM2dQvXp1uLu74/Tp06hWrRrCw8MLIyMRERFRsaTyGbXJkydjzJgxmDt3bo7tkyZNQosWLdQWjoiIiKg4U/mMWmxsLAYNGpRju5+fH2JiYtQSioiIiIjyUdSsra1x4cKFHNsvXLjAkaBEREREaqTypc9vvvkGQ4YMwa1bt+Dt7Q1BEHDs2DHMmzcP48aNK4yMRERERMWSykVt2rRpMDU1xcKFCzFlyhQAgL29PYKCghAQEKD2gERERETFlcpFTRAEjBkzBmPGjMGrV68AAKampmoPRkRERFTc5WsetfdY0IiIiIgKj8qDCYiIiIioaLCoEREREckUixoRERGRTLGoEREREclUvorayJEj8fz5c3VnISIiIqIP5Lmo3b9/X/HvjRs34vXr1wAADw8P3Lt3T/3JiIiIiIq5PE/PUbVqVVhaWqJBgwZ48+YN7t27h/Lly+P27dvIzMwszIxERERExVKez6glJSVh69atqF27NrKzs9G2bVtUqVIF6enpCAsLQ2JiYmHmJCIiIip28lzUMjMzUadOHYwbNw5GRkY4f/481qxZA11dXaxevRqVKlWCi4tLYWYlIiIiKlbyfOmzVKlSqFWrFho0aICMjAykpqaiQYMG0NPTw5YtW1CuXDmcOXOmMLMSERERFSt5PqP28OFDfPfddzAwMMDbt2/h5eWFL7/8EhkZGYiKioIgCGjYsGFhZiUiIiIqVvJc1KysrNChQwfMmTMHxsbGOHv2LPz9/SEIAsaPH49SpUqhcePGag0XFBQEQRCUHra2tor9oigiKCgI9vb2MDIyQpMmTXDlyhW1ZiAiIiKSSr4nvDUzM0O3bt2gr6+PQ4cOIT4+HsOHD1dnNgBAtWrVkJCQoHhcunRJsW/+/PlYtGgRli1bhrNnz8LW1hYtWrTAq1ev1J6DiIiIqKjlq6hFR0ejXLlyAABHR0fo6+vD1tYW3bt3V2s4ANDT04Otra3iYW1tDeDd2bTFixdj6tSp6NKlC9zd3bF27VqkpqZi48aNas9BREREVNTyVdQcHBygo/PuQy9fvgwHBwe1hvpQXFwc7O3tUbFiRfTo0QO3bt0CAMTHxyMxMREtW7ZUHGtgYIDGjRvjxIkTn/2c6enpSE5OVnoQERERyY2s1/qsW7cu1q1bh7CwMPz6669ITEyEt7c3nj17ppi3zcbGRuljbGxs/nNOtzlz5sDMzEzxKMyiSURERJRfsi5qbdq0QdeuXeHh4YHmzZtjz549AIC1a9cqjhEEQeljRFHMse1jU6ZMQVJSkuLBJbCIiIhIjmRd1D5WsmRJeHh4IC4uTjH68+OzZ48fP85xlu1jBgYGKFWqlNKDiIiISG40qqilp6cjNjYWdnZ2qFixImxtbREeHq7Yn5GRgYiICHh7e0uYkoiIiEg98rwygRTGjx+PDh06oHz58nj8+DFmzZqF5ORk9O/fH4IgYPTo0QgODkblypVRuXJlBAcHw9jYGL169ZI6OhEREVGBybqo3b9/Hz179sTTp09hbW2NevXq4dSpU3B0dAQATJw4EWlpaRg+fDhevHiBunXrYv/+/TA1NZU4OREREVHBybqobd68+bP7BUFAUFAQgoKCiiYQERERURHSqHvUiIiIiIoTFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIpFjUiIiIimWJRIyIiIpIprSlqP//8MypWrAhDQ0PUrl0bR48elToSERERUYFoRVHbsmULRo8ejalTp+L8+fP48ssv0aZNG9y9e1fqaERERET5pid1AHVYtGgRBg0ahMGDBwMAFi9ejLCwMCxfvhxz5szJcXx6ejrS09MVz5OSkgAAycnJKr1udnpqAVKrTtV8BVGU743vq+D4vtRDW98b31fB8X2ph7a+N1Xf1/vjRVH874NFDZeeni7q6uqK27ZtU9oeEBAgNmrUKNePCQwMFAHwwQcffPDBBx98SPa4d+/ef/YcjT+j9vTpU2RlZcHGxkZpu42NDRITE3P9mClTpmDs2LGK59nZ2Xj+/DksLS0hCEKh5k1OToaDgwPu3buHUqVKFeprFSVtfV+A9r43vi/Noq3vC9De98b3pVmK8n2JoohXr17B3t7+P4/V+KL23scFSxTFT5YuAwMDGBgYKG0zNzcvrGi5KlWqlFZ9g7+nre8L0N73xvelWbT1fQHa+974vjRLUb0vMzOzPB2n8YMJrKysoKurm+Ps2ePHj3OcZSMiIiLSJBpf1EqUKIHatWsjPDxcaXt4eDi8vb0lSkVERERUcFpx6XPs2LHo27cvvLy8UL9+faxcuRJ3797FsGHDpI6Wg4GBAQIDA3NcetV02vq+AO19b3xfmkVb3xegve+N70uzyPV9CaKYl7Gh8vfzzz9j/vz5SEhIgLu7O0JCQtCoUSOpYxERERHlm9YUNSIiIiJto/H3qBERERFpKxY1IiIiIpliUSMiIiKSKRY1IiIiIpliUSMiIiKSKa2YR00TvHz5EmfOnMHjx4+RnZ2ttK9fv34SpSIiucvOzsaNGzdy/dnBKYioqGVkZOT6vVi+fHmJEmk/Ts9RBHbv3o3evXsjJSUFpqamSmuQCoKA58+fS5hOPW7cuIGbN2+iUaNGMDIy+uxaq3KVnJyc52M1aX27Xbt25fnYjh07FmIS9erSpUuej922bVshJik8p06dQq9evXDnzh18/KNaEARkZWVJlEw9Xr58iVWrViE2NhaCIMDV1RWDBg3K8xqIcqGtPzs+FBcXBz8/P5w4cUJp+/uf9Zr+vQgAMTExuHv3LjIyMpS2S/1zkUWtCFSpUgVt27ZFcHAwjI2NpY6jVs+ePUP37t1x6NAhCIKAuLg4ODk5YdCgQTA3N8fChQuljphnOjo6/1kuNfGHko5O3u5w0LT3NXDgwDwfu2bNmkJMUnhq1qyJKlWqYMaMGbCzs8vx/alpheZDkZGRaNWqFYyMjFCnTh2IoojIyEikpaVh//798PT0lDpinmnrz44PNWjQAHp6epg8eXKu34s1atSQKFnB3bp1C507d8alS5cgCILij6L371HqrxmLWhEoWbIkLl26BCcnJ6mjqF2/fv3w+PFj/Pbbb3B1dcXFixfh5OSE/fv3Y8yYMbhy5YrUEfMsIiIiz8c2bty4EJMQvVOyZElcvHgRzs7OUkdRuy+//BLOzs749ddfoaf37i6ct2/fYvDgwbh16xb+/fdfiRPmXXH42VGyZEmcO3cOVatWlTqK2nXo0AG6urr49ddf4eTkhDNnzuDZs2cYN24cFixYgC+//FLSfLxHrQi0atUKkZGRWlnU9u/fj7CwMJQrV05pe+XKlXHnzh2JUuWPpv4Apf/z5MkTXLt2DYIgoEqVKrC2tpY6UoHUrVsXN27c0MqiFhkZqVTSAEBPTw8TJ06El5eXhMlUVxx+dri5ueHp06dSxygUJ0+exKFDh2BtbQ0dHR3o6OigYcOGmDNnDgICAnD+/HlJ87GoFYF27dphwoQJiImJgYeHB/T19ZX2S339uyBSUlJyvZz79OlT2S1s+1+io6Ph7u4OHR0dREdHf/bY6tWrF1Eq9YuIiMCCBQuU7guaMGGC5H81FkRKSgr8/f2xbt06xU3Ourq66NevH5YuXaqxtxz4+/tj3LhxSExMzPVnhyZ/H5YqVQp3797NcYbm3r17MDU1lSiVenx8752bmxv8/Pw0+lL1vHnzMHHiRAQHB+f6vaip994B7y5tmpiYAACsrKzw8OFDuLi4wNHREdeuXZM4HQCRCp0gCJ986OjoSB2vQNq2bSt+9913oiiKoomJiXjr1i0xKytL/Prrr8WuXbtKnE41giCIjx49UvxbR0dH675m69evF/X09MRu3bqJP/74o7h48WKxW7duor6+vvj7779LHS/fhgwZIjo5OYl79+4Vk5KSxKSkJHHPnj1ipUqVxGHDhkkdL98+9f2n6d+HoiiK/v7+Yrly5cTNmzeLd+/eFe/duydu2rRJLFeunDhq1Cip4+Xb2bNnRQsLC7Fs2bJi586dxU6dOonlypUTLS0txXPnzkkdL98+/P778KEN34sNGzYUt2/fLoqiKPbs2VNs3bq1eOzYMbFfv35itWrVpA0niiLvUaMCiYmJQZMmTVC7dm0cOnQIHTt2xJUrV/D8+XMcP34clSpVkjpint25cwfly5eHIAj/ednW0dGxiFKpl6urK4YMGYIxY8YobV+0aBF+/fVXxMbGSpSsYKysrPDnn3+iSZMmStsPHz6Mbt264cmTJ9IEKyBt/T4E3k3zMGHCBKxYsQJv374FAOjr6+Pbb7/F3LlzNe6M/HvadO/dh/7rPjxNvvwbFhaGlJQUdOnSBbdu3UL79u1x9epVWFpaYsuWLWjatKmk+VjUqMASExOxfPlynDt3DtnZ2fD09MSIESNgZ2cndbR8yczMxJAhQzBt2jStu6/QwMAAV65cyXHP040bN+Du7o43b95IlKxgjI2Nce7cObi6uiptv3LlCurUqYOUlBSJkhVMSkoKSpYsKXWMQpWamoqbN29CFEU4Oztr7GXq94yMjHD+/Pkcl3RjYmLg5eWF1NRUiZKRKp4/f47SpUvLYpop3qNWSJYsWYIhQ4bA0NAQS5Ys+eyxAQEBRZSqcNja2mLGjBlSx1AbfX19bN++HdOmTZM6ito5ODjg4MGDOYrawYMH4eDgIFGqgqtfvz4CAwOxbt06GBoaAgDS0tIwY8YM1K9fX+J0+WdjY4Nu3brBz88PDRs2lDpOoTA2Noa5uTkEQdD4kgZo1713xeW+3bVr1+Krr75S+qPIwsJCwkTKeEatkFSsWBGRkZGwtLRExYoVP3mcIAi4detWESZTP21cdWHgwIHw8PDA2LFjpY6iVsuXL8fo0aPh5+cHb29vCIKAY8eOITQ0FD/++COGDh0qdcR8uXTpEtq0aYM3b96gRo0aEAQBFy5cgKGhIcLCwlCtWjWpI+bL7t27ERoair///huOjo7w8/NDv379YG9vL3W0Anv79i1mzJiBJUuW4PXr1wAAExMT+Pv7IzAwMMfN6poiICAA27dvx4IFC5T+H5swYQK6du2KxYsXSx0xz3R0dJCYmIgyZcoo5orLrTJo8vxwAGBtbY3U1FR06NABffr0QevWrZVGI0uNRY0KRFtXXZg9ezYWLFiAZs2aoXbt2jkuP2nyWdDt27dj4cKFivvR3o/69PX1lThZwaSlpWHDhg24evUqRFGEm5sbevfuDSMjI6mjFdizZ8+wbt06hIaGIiYmBq1atYKfnx86duwoq18oqhg2bBi2b9+OmTNnKs56njx5EkFBQfD19cWKFSskTpg/2nTvXXG4bxd490fDvn37sGnTJuzcuRNGRkb4+uuv0adPH3h7e0sdj0WNCkZbV13Q9rOg2iQzMxMuLi74+++/4ebmJnWcQrd06VJMmDABGRkZsLKywrBhwzB58mSN+//PzMwMmzdvRps2bZS2//PPP+jRoweSkpIkSqYe2nbvXXGRmpqK7du3Y+PGjThw4ADKlSuHmzdvSppJM/8U0wCqXDJbtGhRISYpXA8ePEBAQIDW/RCKj4+XOkKhuHfvHgRBUExQfObMGWzcuBFubm4YMmSIxOnyR19fH+np6bK46bewJCYmYt26dVizZg3u3r2Lr776CoMGDcLDhw8xd+5cnDp1Cvv375c6pkoMDQ1RoUKFHNsrVKiAEiVKFH0gNTM2NoaHh4fUMdTqwYMHOH78eK63uWjyVYYPGRsbo1WrVnjx4gXu3Lkji5HwLGqFJK8zGWv6LxdtXnXhPfGjdd80Wa9evTBkyBD07dsXiYmJaN68Odzd3bFhwwYkJiZi+vTpUkfMF39/f8ybNw+//fabxl4KzM22bduwZs0ahIWFwc3NDSNGjECfPn1gbm6uOKZmzZqoVauWdCHzacSIEfj++++xZs0axeXA9PR0zJ49GyNHjpQ4Xf6lpKRg7ty5OHjwYK6FRlPPxq9ZswbDhg1DiRIlYGlpmeM2F00vau/PpP3+++84cOAAHBwc0LNnT2zdulXqaCxqheXw4cNSRygS2rzqwqpVqxASEoK4uDgA75bFGj16NAYPHixxsvy7fPky6tSpAwD4448/4OHhgePHj2P//v0YNmyYxha106dP4+DBg9i/fz88PDxy3FO4bds2iZIVzMCBA9GjRw8cP34cX3zxRa7HODk5YerUqUWcLH+6dOmi9Pz9paX3C3pfvHgRGRkZaNasmRTx1GLw4MGIiIhA3759c128XFNNnz4d06dPx5QpU6CjoyN1HLXq2bMndu/eDWNjY3z99dc4cuSILO5Ne49FjQrkm2++AQDMnDkzxz5NHgk0bdo0hISEwN/fX+lG5zFjxuD27duYNWuWxAnzJzMzU3H24sCBA4oiXbVqVSQkJEgZrUDMzc3RtWtXqWOoXUJCwn/eVmBkZITAwMAiSlQwHy+h9PHXTJOniHnvn3/+wZ49e9CgQQOpo6hVamoqevTooXUlDXj3u2rLli1o1aqVLM/IczBBEfDx8fnsX1WHDh0qwjSUF1ZWVli6dCl69uyptH3Tpk3w9/fX2MWJ69atCx8fH7Rr1w4tW7bEqVOnUKNGDZw6dQpfffUV7t+/L3VE+kBUVBT09fUV9zrt3LkTa9asgZubG4KCgrTiXi5tU7FiRezduzfH5MuabuLEibCwsMDkyZOljlLsyK86aqGaNWsqPc/MzMSFCxdw+fJl9O/fX5pQ9FlZWVnw8vLKsb127dqKIfeaaN68eejcuTN++OEH9O/fX3HJadeuXYpLoprq7du3OHLkCG7evIlevXrB1NQUDx8+RKlSpRQLLmuaoUOHYvLkyfDw8MCtW7fQo0cPdO7cGVu3bkVqaqpGzcmVG238mn3//feYPn061q5dq1WDrObMmYP27dtj3759ud7mommD4jRpUnqeUZNQUFAQXr9+jQULFkgdpUBSUlIQERGBu3fvIiMjQ2mf1N/g+eXv7w99ff0cP3zGjx+PtLQ0/PTTTxIlK7isrCwkJyejdOnSim23b9+GsbExypQpI2Gy/Ltz5w5at26Nu3fvIj09HdevX4eTkxNGjx6NN2/eaOycXGZmZoiKikKlSpUwb948HDp0CGFhYTh+/Dh69OiBe/fuSR0x37T1a1arVi3FtBwVKlTIUWiioqIkSlYw33//PQIDA+Hi4gIbG5scgwk07crQh5PSV6hQ4ZNXveQwHRPPqEmoT58+qFOnjkYXtfPnz6Nt27ZITU1FSkoKLCws8PTpU8UvfU0tasC7wQT79+9HvXr1AACnTp3CvXv30K9fP6XpVzTtL0ldXV2lkgYg12kSNMmoUaPg5eWFixcvwtLSUrG9c+fOGj34QxRFxajBAwcOoH379gDe3culqZff39PWr1mnTp2kjlAoFi1ahNWrV2PAgAFSR1GLD6dgun37tnRB8oBFTUInT55UrEuoqcaMGYMOHTpg+fLlMDc3x6lTp6Cvr48+ffpg1KhRUsfLt8uXL8PT0xMAFJMdWltbw9raGpcvX1Ycpwkjujw9PXHw4EGULl0atWrV+mxmTf1r/9ixYzh+/HiOe7YcHR3x4MEDiVIVnJeXF2bNmoXmzZsjIiICy5cvB/Dul4yNjY3E6QpGW79mmjKwQ1UGBgZaN0AC0IwJs1nUisDHQ9JFUURCQgIiIyM1fuHvCxcu4JdffoGuri50dXWRnp4OJycnzJ8/H/3798/x3jWFNk2v4uvrqxjp6evrqxHlUlXZ2dm5jjC+f/++xi2E/aHFixejd+/e2LFjB6ZOnQpnZ2cAwJ9//imr6QPyQ1u/Ztpq1KhRWLp06X/ez6VpNGHCbN6jVgQGDhyo9FxHRwfW1tZo2rQpWrZsKVEq9bC2tsbx48dRpUoVuLi4YMmSJWjVqhWuXr0KT09PpKamSh2RioHu3bvDzMwMK1euhKmpKaKjo2FtbQ1fX1+UL18ea9askTqiWr158wa6uroau3A5oF1fMwsLC1y/fh1WVlYoXbr0Z3/pa+r6x507d8ahQ4dgaWmJatWq5fje09S5CgFg7ty5uHr1qmwnzJZfIi2kST9wVFWrVi1ERkaiSpUq8PHxwfTp0/H06VOsX79e45dPOXv2LLZu3ZrrIAlN/aHk5OSEs2fPKt0TBAAvX76Ep6en5DfN5ldISAh8fHzg5uaGN2/eoFevXoiLi4OVlRU2bdokdTy10/RbJgDt+pqFhIQozgJq+kjcTzE3N9fYKyT/Re4TZvOMWhF7/fp1jiVFSpUqJVGagouMjMSrV6/g4+ODJ0+eoH///jh27BicnZ2xevXqHFOTaIrNmzejX79+aNmyJcLDw9GyZUvExcUhMTERnTt31tjyraOjg8TExByjOx89egQHB4cchVSTpKWlYfPmzTh37hyys7Ph6emJ3r17w8jISOpo+ZaVlYWQkBD88ccfuf7BoKlnZ97Txq8ZaZ6Pr3p9TOqf9yxqRSA+Ph4jR47EkSNH8ObNG8V2URQ1evZ+bVa9enUMHToUI0aMgKmpKS5evIiKFSti6NChsLOzw4wZM6SOqJJdu3YBeDcibe3atUozxGdlZeHgwYMIDw/HtWvXpIqosg8HScycORPjx4/XqnmrgHfL9vz2228YO3Yspk2bhqlTp+L27dvYsWMHpk+frtGjqrVZVlYWtm/fjtjYWAiCAFdXV/j6+sryshrJH4taEXh/0++oUaNyzD8DAI0bN5YillrEx8fj7du3qFy5stL2uLg46Ovra+y0DyVLlsSVK1dQoUIFWFlZ4fDhw/Dw8EBsbCyaNm2qccstfW7Zl/dfp4ULFyqmf9AERkZGiIuLQ7ly5aCrq4uEhASNnQfuUypVqoQlS5agXbt2MDU1xYULFxTbTp06hY0bN0odMd/mzJkDGxsb+Pn5KW1fvXo1njx5gkmTJkmUrGAuX74MX19fJCYmwsXFBQBw/fp1WFtbY9euXRp9S8iff/75ybO7mjpi/EOPHz/GtWvXIAgCqlSpIpufJ6z3RSA6Ohrnzp1T/E+rTQYMGAA/P78cRe306dP47bffcOTIEWmCFZCFhQVevXoFAChbtiwuX74MDw8PvHz5UuMGSERHRyMzMxO6urqoWLEizp49CysrK6ljFVjNmjUxcOBANGzYEKIoYsGCBZ+czV5TF5tPTExU/GI3MTFBUlISAKB9+/YaP2L8l19+ybVoVqtWDT169NDYojZ48GBUq1YNkZGRivkKX7x4gQEDBmDIkCE4efKkxAnzZ8mSJZg6dSr69++PnTt3YuDAgbh58ybOnj2LESNGSB2vQJKTkzFixAhs3rxZcYVLV1cX3bt3x08//ZRjjdqipn2rq8rQF198odEziH/O+fPnc51bp169erhw4ULRB1KTL7/8EuHh4QCAbt26YdSoUfjmm2/Qs2dPNGvWTOJ0qqlVq5biXiZBEGQ9DF0VoaGhsLS0xN9//w1BEPDPP/9g+/btOR47duyQOmq+lStXTnH21tnZGfv37wfwbqDL+ylXNFViYiLs7OxybLe2tta4M9YfunjxIubMmaM0qXTp0qUxe/Zsjf6Z+PPPP2PlypVYtmwZSpQogYkTJyI8PBwBAQGKPyA01eDBg3H69Gn8/fffePnyJZKSkvD3338jMjIS33zzjdTxeEatKPz2228YNmwYHjx4AHd39xzDmqtXry5RsoITBEFx5ulDSUlJGn3v3bJlyxT3E06ZMgX6+vo4duwYunTponFnMszNzXHr1i1YW1vjzp07OQazaCoXFxds3rwZwLtLuwcPHpTNpQp16dy5Mw4ePIi6deti1KhR6NmzJ1atWoW7d+9izJgxUscrEAcHBxw/fhwVK1ZU2n78+HHY29tLlKrgXFxc8OjRI1SrVk1p++PHjxXz4Gmiu3fvKm7jMTIyUvzc79u3L+rVq4dly5ZJGa9A9uzZg7CwMDRs2FCxrVWrVvj111/RunVrCZO9w6JWBJ48eYKbN28qjSwRBEErBhN8+eWXmDNnDjZt2gRdXV0A726knTNnjtI3vaaxsLBQ/FtHRwcTJ07ExIkTJUyUf127dkXjxo0VZy+8vLwUX6uPaer0HNpSPj82d+5cxb+/+uorlCtXDidOnICzszM6duwoYbKCGzx4MEaPHo3MzEw0bdoUAHDw4EFMnDgR48aNkzidapKTkxX/Dg4ORkBAAIKCgpSWn5s5cybmzZsnVcQCs7W1xbNnz+Do6AhHR0ecOnUKNWrUQHx8PDT9VndLS8tcL2+amZnlWG5PChxMUATc3Nzg6uqKiRMn5jqYwNHRUaJkBRcTE4NGjRrB3NwcX375JQDg6NGjSE5OxqFDh+Du7i5xwvz51M3pz549Q5kyZTSuXO/btw83btxAQEAAZs6c+cmZ3zVp2a9du3ahTZs20NfXV4xq/RRNLzXaSBRFTJ48GUuWLFHcmG5oaIhJkyZp3D2FOjo6Sj/X3/9afb/tw+ea9rPjvcGDB8PBwQGBgYFYsWIFxo4diwYNGiAyMhJdunTBqlWrpI6YbytXrsTWrVuxbt06xR+0iYmJitV1hg4dKmk+FrUiULJkSVy8eFGjT3t/zsOHD7Fs2TJcvHgRRkZGqF69OkaOHKl0VkrTfGq+sYcPH6JSpUpIS0uTKFnBDBw4EEuWLNGKJXo+/Bp9blSrpv1y/K/S+SFtKKCvX79GbGwsjIyMULlyZY289y4iIiLPx2rqKP/s7GxkZ2crphj5448/FHNmDhs2LMearZqkVq1auHHjBtLT01G+fHkA7y71GhgY5BgoJ8XoVha1ItChQwcMGDAAXbt2lToK/Yf369iNGTMG33//vdIowqysLPz777+4ffs2zp8/L1VE0nKfK50f0rQCSprt7t27cHBwyHFFSBRF3Lt3T1FwNJEq82IGBgYWYpLcsagVgZUrV2LWrFnw8/ODh4dHjsEEmvZXcXR0NNzd3aGjo4Po6OjPHqtpAyXe39h8584dxfxc75UoUQIVKlTAzJkzUbduXakiFpg2Lo1Fmkkbvxf//fffz+5v1KhRESVRL227HUSTsKgVAW26LAPkvOT0fmDExzTxvb3n4+ODbdu2yeJGUnXS1qWxgHc3oh88eBCPHz/OMbhg9erVEqVSnzdv3mjFGp/vaev3Ym4/7z88C6WpPxN1dHTw6NEjWFtbK22/c+cO3NzckJKSIlEy9Tl37pxiNQk3NzfUqlVL6kgAOOqzSGjbiLT4+HjF/6zx8fESpykchw8fBgBkZGQgPj4elSpV0orlX4KDgxESEqJYGuvHH39UWhpLU82YMQMzZ86El5cX7OzstGauuKysLAQHB2PFihV49OgRrl+/DicnJ0ybNg0VKlTAoEGDpI6Yb9r6vfjixQul55mZmTh//jymTZuG2bNnS5Qq/8aOHQvgXdmcNm2a0jJtWVlZOH36tMau6fze48eP0aNHDxw5cgTm5uYQRRFJSUnw8fHB5s2bc5TTIicSUQ6pqamin5+fqKurK+rq6oo3b94URVEU/f39xTlz5kicLv+MjY3F+Ph4URRF0dLSUoyOjhZFURRjYmJEW1tbCZMVjK2trbhu3TqpY6jdjBkzRCcnJ3HDhg2ikZGR4vtwy5YtYr169SROVzDa+r34KREREaKnp6fUMVTWpEkTsUmTJqIgCKK3t7fieZMmTcSWLVuKQ4YMEa9fvy51zALp1q2bWLt2bTEmJkax7cqVK6KXl5fYo0cPCZO9o/mnCDREREQEFixYoLRI74QJExRTWmiyBw8e4Pjx47lectLURaMnT56Mixcv4siRI0oTHjZv3hyBgYGYPHmyhOnyT5uWxvpQRkaGYjJObbJu3TqsXLkSzZo1w7BhwxTbq1evjqtXr0qYrOC09XvxU6ytrXHt2jWpY6hkyZIl2Lt3L4yMjDBw4ED8+OOPKFWqlNSx1G7fvn04cOAAXF1dFdvc3Nzw008/oWXLlhIme4dFrQhs2LABAwcORJcuXRAQEABRFHHixAk0a9YMoaGh6NWrl9QR823NmjWKodmWlpZKl5wEQdDYorZjxw5s2bIF9erVU3pPbm5uuHnzpoTJCub90lgeHh6KpbEOHTqE8PBwjVsa60ODBw/Gxo0bNW7ViP/y4MGDXKf1yc7ORmZmpgSJ1Edbvxc/HmAliiISEhIwd+5c1KhRQ6JU+TN27Fj06NEDRkZGWLduHebNm6eVRS07OzvHID8A0NfXl8WtSyxqRWD27NmYP3++0pIvo0aNwqJFi/D9999rdFGbPn06pk+fjilTpuR5WgFN8OTJk1yXI0pJSdHo+5+0aWmsD7158wYrV67EgQMHUL169Rw/dBctWiRRsoKpVq0ajh49mmNS7K1bt8rmRuf80tbvxZo1a+Y6wKpevXoaN6jF3t4ef/31F9q2bQtRFHH//n3F1+xjmjw9R9OmTTFq1Chs2rRJsXzZgwcPMGbMGFn80cBRn0XAwMAAV65cyfGX8Y0bN+Du7v7Jb3xNYGlpiTNnzqBSpUpSR1Grxo0b46uvvoK/vz9MTU0RHR2NihUrYuTIkYiLi0NYWJjUEekDPj4+n9wnCAIOHTpUhGnUZ/fu3ejbty+mTJmCmTNnYsaMGbh27RrWrVuHv//+Gy1atJA6In3kzp07Ss91dHRgbW2tkSN2V65cCX9/f7x9+/aTx4hasBTivXv34Ovri8uXLyvmirt79y48PDywc+dOlCtXTtJ8LGpFwNnZGRMmTMixDMUvv/yCBQsWIC4uTqJkBTdx4kRYWFho7D1bn3LixAm0bt0avXv3RmhoKIYOHYorV67gxIkT+Pfff1G7dm2pI6rk4yVuciMIwmd/IJM0wsLCEBwcjHPnziE7Oxuenp6YPn26LO6dUdWHa2L+F026xGZhYYHr16/DysoKfn5++PHHH7Vi9Q8AePXqFe7cuYPq1avjwIEDsLS0zPU4Tbusm5vw8HBcvXoVoijCzc0NzZs3lzoSABa1IrF8+XKMHj0afn5+8Pb2hiAIOHbsGEJDQ/Hjjz9Kvo5YQWRlZaF9+/ZIS0vLdTJfTbvktGDBAowfPx4AcOnSJSxYsEDpF+TEiRMxZMgQnDp1SuKkqtm5c+cn9504cQJLly6FKIoauzTWh+7fvw9BEFC2bFmpo9BH8vIHgyaeoTExMUF0dDScnJygq6uLxMRE6ad0ULO1a9eiR48eGrnE1+e8ffsWhoaGuHDhgmzXpuY9akXg22+/ha2tLRYuXIg//vgDAODq6ootW7bA19dX4nQFExwcjLCwMLi4uABAjsEEmmbatGmwtLTEwIED4eHhgbVr1yr2vXr1Cq1atVLprIBc5PZ9dvXqVUyZMgW7d+9G79698f3330uQTD2ys7Mxa9YsLFy4EK9fvwYAmJqaYty4cZg6darG3j/p5OSEs2fP5jiL8fLlS3h6euLWrVsSJcuf9/MTapv69eujU6dOqF27NkRRREBAAIyMjHI9VtPuU3uvf//+ePnyJdavX4+bN29iwoQJsLCwQFRUFGxsbDT2DyM9PT04OjrK+w8DCaYEIS1ibm4urlmzRuoYarN161bR0NBQ3L59u9L2169fi97e3mKVKlXExMREacKpyYMHD8TBgweL+vr6Yvv27cVLly5JHanAJk+eLFpbW4s///yzePHiRfHChQviTz/9JFpbW4v/+9//pI6Xb4IgiI8ePcqxPTExUSxRooQEiQouJSVFHD58uGhvby9aW1uLPXv2FJ88eSJ1rAJJTEwUJ02aJH711Veijo6O2KZNG7FTp065PjTVxYsXRWtra9HZ2VnU09NTzOn33XffiX379pU4XcGsXr1abNOmjfjs2TOpo+SKlz6LUGRkpNI8app2n1NubG1tcfToUVSuXFnqKGrz22+/ISAgAHv27IGPjw9ev36N1q1b4/Hjxzhy5IhiVJCmSUpKQnBwMJYuXYqaNWti3rx5WjGPH/BudNqKFStyrJu7c+dODB8+HA8ePJAoWf7s2rULANCpUyesXbsWZmZmin1ZWVk4ePAgwsPDNW5eLgCYMGECfv75Z/Tu3RtGRkbYuHEjmjRpgq1bt0odTS0qVqyIyMjIT97LpamaNWuG2rVrY/78+TA1NcXFixfh5OSEEydOoFevXrh9+7bUEfOtVq1auHHjBjIzM+Ho6IiSJUsq7Y+KipIo2Tu89FkE7t+/j549e+L48eMwNzcH8O7Shbe3NzZt2gQHBwdpAxbAqFGjsHTpUixZskTqKGozePBgPH/+HJ06dcLOnTsxbdo0JCYmIiIiQmNL2vz58zFv3jzY2tpi06ZNGn/J/WPPnz9H1apVc2yvWrUqnj9/LkGigunUqROAd7cP9O/fX2mfvr4+KlSogIULF0qQrOC2bduGVatWoUePHgCA3r17o0GDBsjKyoKurq7E6QpOW5fVi4yMxMqVK3NsL1u2LBITEyVIpD6dOnX65JrVcsAzakWgZcuWSE5Oxtq1axX3cl27dg1+fn4oWbIk9u/fL3HC/OvcuTMOHToES0tLVKtWLcdggm3btkmUrOCmTJmC+fPno0KFCoiIiJB8iHZB6OjowMjICM2bN//sL0NN/XrVrVsXdevWzfEHg7+/P86ePatxgz/eq1ixIs6ePQsrKyupo6hNiRIlEB8fr3RPk5GREa5fv67Rf7R+6ODBgzh48GCuq7Vo6j1qNjY22LdvH2rVqqV0Rm3//v0YNGgQ7t27J3VElaWmpmLChAnYsWMHMjMz0axZMyxdulR2/7/xjFoROHr0KE6cOKEoaQDg4uKCpUuXokGDBhImKzhzc3N06dJF6hhq8/F70dfXh5WVVY4VFjSt0PTr108jB3fk1fz589GuXTscOHAA9evXhyAIOHHiBO7du4e9e/dKHU9lp0+fxvPnz5XOzqxbtw6BgYFISUlBp06dsHTpUo0cgZeVlYUSJUoobdPT09OaqWFmzJiBmTNnwsvLC3Z2dlrz/52vry9mzpypGBD3fq6xyZMno2vXrhKny5/AwECEhoYqXYb/9ttvZXcZnmfUioCLiwvWr1+POnXqKG0/c+YMevXqhRs3bkiUjD42cODAPB23Zs2aQk5Cqnr48CF++uknpXmQhg8frpGXq1u3bg0fHx9MmjQJwLupYjw9PTFgwAC4urrihx9+wNChQxEUFCRt0HzQ0dFBmzZtlErm7t270bRpU6V7gzTtj6H37OzsMH/+fPTt21fqKGqVnJyMtm3b4sqVK3j16hXs7e2RmJiIevXq4Z9//slxX5cmqFSpEmbPnq24DH/mzBk0aNAAb968kdVleBa1IrBz504EBwfjp59+Qu3atSEIAiIjI+Hv749JkyYp7kchItU0a9YMI0aM+ORZ3adPn6JOnToaN42FnZ0ddu/eDS8vLwDA1KlTERERgWPHjgF4t4RUYGAgYmJipIyZL9r+x5C2rtby3qFDhxAVFaWYW1Iuk8Lmh6ZchmdRKwKlS5dGamoq3r59Cz29d1eb3//7479CNPHG5z///BN//PEH7t69i4yMDKV9Uo+WIe2mo6MDHR0dTJ06FTNmzMix/9GjR7C3t5f3HEm5MDQ0RFxcnOKXRcOGDdG6dWt89913AIDbt2/Dw8MDr169kjIm5WLSpEkwMTHR6PVKP3To0CGMHDkSp06dyrFaRFJSEry9vbFixQqNHEGe2+TEHy4ZKBe8R60ILF68WOoIhWbJkiWYOnUq+vfvj507d2LgwIG4efMmzp49ixEjRkgdj4qB5cuXY8KECYiOjsb69ethYmIidaQCs7GxQXx8PBwcHJCRkYGoqCilIvrq1ascA3dIHt68eYOVK1fiwIEDqF69usav1rJ48WJ88803uS7pZWZmhqFDh2LRokUaWdREUcSAAQOULsO/efMGw4YNk9VleJ5RowKpWrUqAgMD0bNnT6WRQNOnT8fz58+xbNkyqSOSFtPR0UFiYiKePXuGTp06oUSJEti5cyecnJwAaO4ZtaFDh+LSpUuYN28eduzYgbVr1+Lhw4eKm/B///13LF68GGfPnpU4KX3Mx8fns/s1bXUGR0dH7Nu3D66urrnuv3r1Klq2bIm7d+8WcbKC05TL8CxqRSwtLQ2ZmZlK2zRp8eGPGRsbIzY2Fo6OjihTpgzCw8NRo0YNxMXFoV69enj27JnUEUmLvS9qZcqUQVJSEnr27InTp09jy5YtaN68ucYWtSdPnqBLly44fvw4TExMsHbtWnTu3Fmxv1mzZqhXrx5mz54tYUoqDgwNDXH58mU4Ozvnuv/GjRvw8PDQinWC5YqXPotASkoKJk2ahD/++CPX4qJpv0Q+ZGtri2fPnsHR0RGOjo44deoUatSogfj4eNlOHkjayczMDHv27MGUKVPQtm1bzJs3D7169ZI6Vr5YW1vj6NGjSEpKgomJSY4RaFu3btWKS7zaJC/TFAmCgL/++qsI0qhP2bJlcenSpU8WtejoaNjZ2RVxquKFRa0ITJw4EYcPH8bPP/+Mfv364aeffsKDBw/wyy+/YO7cuVLHK5CmTZti9+7d8PT0xKBBgzBmzBj8+eefiIyM1Kr51UiePp6jShAEzJ07F7Vq1cKgQYNw6NAhiZKpx4dLR33IwsKiiJPQf/nU10rTtW3bFtOnT0ebNm1gaGiotC8tLQ2BgYFo3769ROmKB176LALly5fHunXr0KRJE5QqVQpRUVFwdnbG+vXrsWnTJo2ckPO97OxsZGdnK0az/vHHHzh27BicnZ3RuXNnWQ1xJu3z4aXPj124cAGdOnXCvXv3NPqsNZGUHj16BE9PT+jq6mLkyJFwcXGBIAiIjY3FTz/9hKysLERFRcHGxkbqqFqLRa0ImJiY4MqVK3B0dES5cuWwbds21KlTB/Hx8fDw8MDr16+ljqhWiYmJmD17Nn777Tfet0CFKiIiAg0aNFD8ofCxZ8+eYc+ePejXr18RJyPSHnfu3MG3336LsLAwxS0tgiCgVatW+Pnnn1GhQgVpA2o5HakDFAdOTk64ffs2AMDNzU2xBMfu3bsVi7RrmpcvX6J3796wtraGvb09lixZguzsbEyfPh2VKlXCqVOnNHZNO9IcjRs3/mRJA95NPsqSRlQwjo6O2Lt3L54+fYrTp0/j1KlTePr0Kfbu3cuSVgR4Rq0IhISEQFdXFwEBATh8+DDatWuHrKwsZGZmIiQkBKNGjZI6osqGDx+O3bt3o3v37ti3bx9iY2PRqlUrvHnzBoGBgWjcuLHUEYmIiDQei5oE7t69i8jISDg7O6N69epSx8kXR0dHrFq1Cs2bN8etW7fg7OyMgIAArZ7cl4iIqKjx0mchOnToENzc3JCcnKy0vXz58mjWrBl69uyJo0ePSpSuYB4+fAg3NzcA7y7tGhoaYvDgwRKnIiIi0i4saoUor0tvaKLs7GylpVF0dXVzrFtKREREBcNLn4VIm5fe0NHRQZs2bRRrpO3evRtNmzbNUdakXiONiIhIk3HC20L06NGjzy6crKenhydPnhRhIvXp37+/0vM+ffpIlISIiEh7sagVIm1eekPqRWqJiIiKA96jVojeL73x5s2bHPu49AYRERH9F96jVoi49AYREREVBItaIePSG0RERJRfLGpF5MWLF7hx4wZEUUTlypVRunRpqSMRERGRzLGoEREREckUBxMQERERyRSLGhEREZFMsagRERERyRSLGhEREZFMsagREUmoSZMmGD16tNQxiEimWNSISDIDBgyAIAgQBAH6+vqwsbFBixYtsHr1amRnZ0uW6/bt24pcgiDAzMwM9erVw+7du9X+Wtu2bcP333+v9s9LRNqBRY2IJNW6dWskJCTg9u3b+Oeff+Dj44NRo0ahffv2ePv27Sc/LjMzs9CzHThwAAkJCTh9+jTq1KmDrl274vLly2p9DQsLC5iamqr1cxKR9mBRIyJJGRgYwNbWFmXLloWnpyf+97//YefOnfjnn38QGhqqOE4QBKxYsQK+vr4oWbIkZs2ahdDQUJibmyt9vh07dkAQBKVts2bNQpkyZWBqaorBgwdj8uTJqFmz5n9ms7S0hK2tLapWrYrZs2cjMzMThw8fVux/8OABunfvjtKlS8PS0hK+vr64ffu2Yv/bt28REBAAc3NzWFpaYtKkSejfvz86deqkOObjS58VKlTArFmz0K9fP5iYmMDR0RE7d+7EkydP4OvrCxMTE3h4eCAyMlIp64kTJ9CoUSMYGRnBwcEBAQEBSElJUfq8wcHB8PPzg6mpKcqXL4+VK1f+538DIpIWixoRyU7Tpk1Ro0YNbNu2TWl7YGAgfH19cenSJfj5+eXpc/3++++YPXs25s2bh3PnzqF8+fJYvny5SnkyMzPx66+/AgD09fUBAKmpqfDx8YGJiQn+/fdfHDt2DCYmJmjdujUyMjIAAPPmzcPvv/+ONWvW4Pjx40hOTsaOHTv+8/VCQkLQoEEDnD9/Hu3atUPfvn3Rr18/9OnTB1FRUXB2dka/fv0Uy9JdunQJrVq1QpcuXRAdHY0tW7bg2LFjGDlypNLnXbhwIby8vHD+/HkMHz4c3377La5evarSfwsiKmIiEZFE+vfvL/r6+ua6r3v37qKrq6viOQBx9OjRSsesWbNGNDMzU9q2fft28cMfbXXr1hVHjBihdEyDBg3EGjVqfDJXfHy8CEA0MjISS5YsKero6IgAxAoVKojPnj0TRVEUV61aJbq4uIjZ2dmKj0tPTxeNjIzEsLAwURRF0cbGRvzhhx8U+9++fSuWL19e6T03btxYHDVqlOK5o6Oj2KdPH8XzhIQEEYA4bdo0xbaTJ0+KAMSEhARRFEWxb9++4pAhQ5Tew9GjR0UdHR0xLS0t18+bnZ0tlilTRly+fPkn/zsQkfR4Ro2IZEkUxRyXML28vFT+PNeuXUOdOnWUtn38/FO2bNmC8+fPY9euXXB2dsZvv/0GCwsLAMC5c+dw48YNmJqawsTEBCYmJrCwsMCbN29w8+ZNJCUl4dGjR0qvpauri9q1a//n61avXl3xbxsbGwCAh4dHjm2PHz9WZAkNDVXkMDExQatWrZCdnY34+PhcP68gCLC1tVV8DiKSJz2pAxAR5SY2NhYVK1ZU2layZEml5zo6OorLf+/lNsjg48L38cd8ioODAypXrozKlSvDxMQEXbt2RUxMDMqUKYPs7GzUrl0bv//+e46Ps7a2LtBrv7+8+uHH57bt/cjY7OxsDB06FAEBATk+V/ny5XP9vO8/j5Sja4nov/GMGhHJzqFDh3Dp0iV07dr1s8dZW1vj1atXSjfNX7hwQekYFxcXnDlzRmnbxzfi50Xjxo3h7u6O2bNnAwA8PT0RFxeHMmXKwNnZWelhZmYGMzMz2NjYKL12VlYWzp8/r/Jr/xdPT09cuXIlRw5nZ2eUKFFC7a9HREWHRY2IJJWeno7ExEQ8ePAAUVFRCA4Ohq+vL9q3b49+/fp99mPr1q0LY2Nj/O9//8ONGzewceNGpZGiAODv749Vq1Zh7dq1iIuLw6xZsxAdHZ3jTFdejBs3Dr/88gsePHiA3r17w8rKCr6+vjh69Cji4+MRERGBUaNG4f79+4rXnjNnDnbu3Ilr165h1KhRePHiRb5e+3MmTZqEkydPYsSIEbhw4QLi4uKwa9cu+Pv7q/V1iKjosagRkaT27dsHOzs7VKhQAa1bt8bhw4exZMkS7Ny5E7q6up/9WAsLC2zYsAF79+6Fh4cHNm3ahKCgIKVjevfujSlTpmD8+PHw9PREfHw8BgwYAENDQ5Wztm/fHhUqVMDs2bNhbGyMf//9F+XLl0eXLl3g6uoKPz8/pKWloVSpUgDeFaiePXuiX79+qF+/vuLesfy89udUr14dERERiIuLw5dffolatWph2rRpsLOzU+vrEFHRE8S83qxBRKQlWrRoAVtbW6xfv75IXzc7Oxuurq7o1q0bVyMgojzhYAIi0mqpqalYsWIFWrVqBV1dXWzatAkHDhxAeHh4ob/2nTt3sH//fjRu3Bjp6elYtmwZ4uPj0atXr0J/bSLSDixqRKTVBEHA3r17MWvWLKSnp8PFxQV//fUXmjdvXuivraOjg9DQUIwfPx6iKMLd3R0HDhyAq6trob82EWkHXvokIiIikikOJiAiIiKSKRY1IiIiIpliUSMiIiKSKRY1IiIiIpliUSMiIiKSKRY1IiIiIpliUSMiIiKSKRY1IiIiIpn6f/lEQavO64odAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a bar plot showing the total number of rows (Mouse ID/Timepoints) for each drug regimen using Pandas.\n",
    "\n",
    "# Count the occurrences of each drug regimen\n",
    "drug_counts = combined_data['Drug Regimen'].value_counts()\n",
    "\n",
    "# Create a bar plot from the counts\n",
    "drug_counts.plot(kind='bar', figsize=(7, 5), xlabel=\"Drug Regimen\", ylabel='# of Observed Mouse Timepoint')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAmoAAAH8CAYAAABhBYO8AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABeSElEQVR4nO3deVxN+eM/8Ndp0UJKixYSiZSypLFkBtn3LDP2NQZjyb59DMWQZZDBDGMGWcYyZqzDSLbGTkLILnvXrqhU6vz+8HO/rsK9uTnn1Ov5eNzHwz3n1H1dJa/OOe/3WxBFUQQRERERyY6B1AGIiIiIKGcsakREREQyxaJGREREJFMsakREREQyxaJGREREJFMsakREREQyxaJGREREJFNGUgeQg6ysLNy7dw8WFhYQBEHqOERERJSPiaKI58+fw8nJCQYGHz5nxqIG4N69e3B2dpY6BhERERUgt2/fRsmSJT94DIsaAAsLCwCv/8KKFi0qcRoiIiLKz5KSkuDs7KzuHx/CogaoL3cWLVqURY2IiIg+C21ut+JgAiIiIiKZYlEjIiIikikWNSIiIiKZYlEjIiIikikWNSIiIiKZYlEjIiIikikWNSIiIiKZYlEjIiIikikWNSIiIiKZYlEjIiIikikWNSIiIiKZYlEjIiIikikWNSIiIiKZYlEjIiIikikWNSIiIiKZYlEjIiIikikjqQMUJKXHbZc6wgfdmNFC6ghERET0Fp5RIyIiIpIpFjUiIiIimeKlT9IZL+ESERF9HjyjRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMsWiRkRERCRTLGpEREREMiVpUZs+fTq++OILWFhYoHjx4mjT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WFhInJyIiIjo08m6qK1bt+6D+wVBQEhICEJCQj5PICIiIqLPSFH3qBEREREVJCxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkUyxqRERERDLFokZEREQkU/mmqP3yyy8oU6YMTE1NUa1aNRw4cEDqSERERESfJF8UtfXr12PYsGGYMGECTp06ha+++grNmjXDrVu3pI5GRERElGtGUgfQh7lz56JPnz7o27cvAGDevHmIiIjAokWLMH369GzHp6WlIS0tTf08MTERAJCUlJSnObPSUvL0838qbd8/38fnocv3Y355L3wfnwe/t+SH70N+8rITvPncoih+/GBR4dLS0kRDQ0Nx48aNGtuDgoLEOnXq5PgxwcHBIgA++OCDDz744IMPyR63b9/+aM9R/Bm1R48eITMzE/b29hrb7e3toVKpcvyY8ePHY8SIEernWVlZePLkCWxsbCAIQp7m1ZekpCQ4Ozvj9u3bKFq0qNRxco3vQ37yy3vh+5Cf/PJe+D7kR2nvRRRFPH/+HE5OTh89VvFF7Y13C5Yoiu8tXSYmJjAxMdHYZmVllVfR8lTRokUV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",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a bar plot showing the total number of rows (Mouse ID/Timepoints) for each drug regimen using pyplot.\n",
    "\n",
    "# Count the occurrences of each drug regimen\n",
    "drug_counts = combined_data['Drug Regimen'].value_counts()\n",
    "\n",
    "# Extract the drug regimens and their corresponding counts\n",
    "regimens = drug_counts.index\n",
    "counts = drug_counts.values\n",
    "\n",
    "#Set the plot size\n",
    "plt.figure(figsize=(7,5))\n",
    "\n",
    "\n",
    "# Create a bar plot using pyplot\n",
    "plt.bar(regimens, counts, align='center')\n",
    "\n",
    "# Set the tick locations\n",
    "#tick_locations = [value for value in regimens]\n",
    "plt.xticks(regimens, rotation='vertical')\n",
    "\n",
    "# Give our chart some labels and a tile\n",
    "plt.xlabel(\"Drug Regimen\")\n",
    "plt.ylabel(\"# of Observed Mouse Timepoint\")\n",
    "\n",
    "\n",
    "# Display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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IJbVlUvbFu8rG19KO5ZJ3mrTqcxLzJA6nix1HBwqFJ0GS+ltTKcC4gblArATywrtErp7jbTr6/230s323MjL4ZRyukqt+0pt+kit+0ht+4f+dDpNpwPiFuUCiAc+j7RnrbRng1S+RSrbEvqzfItUsT26i4fDKaW3k7I6hW45XaU2fUMFIq+XlJBsOiGA76FcAPEu4Jcqt4UKR+V2qaZEqt0b2nujtnTf3/eG7vdUKCxzPFyJUnK2lJK978+c0N9TckITK7Py9906SZkdWAoKxBjKBYCjZ1mSv17ye6SAN/Snv37/LVAvyRFaxulwhm6uRMmdtP/PpAyOHgdsjnIBAADCihlPAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAOJS165d9be//c10DMCWKBcAWtzUqVPlcDgOuG3atMl0NAAtwG06AID4MHbsWD399NON7mvdurWhNABaEiMXACIiKSlJ7dq1a3RzuVx6++23NWjQICUnJ6t79+66++675ff7G77O4XBoxowZmjBhglJTU9W3b18tWLBAmzZt0siRI5WWlqZhw4apoKCg4WsKCgp0/vnnq23btkpPT9eQIUM0b968w+arqKjQtddeqzZt2igzM1Nnn322VqxY0WL/HoCdUS4AGDN37lxdfvnl+vnPf641a9ZoxowZeuaZZ3Tvvfc2+rx77rlHV155pZYvX64+ffrosssu03XXXafp06frq6++kiTddNNNDZ9fXV2tcePGad68eVq2bJnGjBmjiRMnauvWrQfNYVmWxo8fr507d2rOnDlasmSJBg4cqHPOOUelpaUt9w8A2JUFAC3sqquuslwul5WWltZwu/DCC63hw4db9913X6PPff7556327ds3fCzJuvPOOxs+XrBggSXJevLJJxvue/nll63k5OTDZujXr5/18MMPN3zcpUsX669//atlWZb13//+18rMzLQ8Hk+jr+nRo4c1Y8aMJn+/QLxjzgWAiDjrrLP06KOPNnyclpamnj17avHixY1GKgKBgDwej2pra5WamipJGjBgQMPjbdu2lSSdcMIJje7zeDyqrKxUZmamampqdPfdd+udd97Rjh075Pf7VVdXd8iRiyVLlqi6ulqtWrVqdH9dXV2jyy0Ajg7lAkBEfFsmvisYDOruu+/WlClTDvj85OTkhr8nJCQ0/N3hcBzyvmAwKEm6/fbbNXfuXD300EPq2bOnUlJSdOGFF8rr9R40WzAYVPv27fXxxx8f8Fh2dvbRfYMAGlAuABgzcOBArV+//oDScaw+++wzTZ06VZMnT5YUmoNRWFh42Bw7d+6U2+1W165dw5oFiEeUCwDG/OY3v9GECROUn5+viy66SE6nUytXrtSqVav0hz/8odnP27NnT82ePVsTJ06Uw+HQXXfd1TCqcTCjRo3SsGHDNGnSJN1///3q3bu3duzYoTlz5mjSpEkaPHhws7MA8YjVIgCMGTNmjN555x19+OGHGjJkiE499VT95S9/UZcuXY7pef/6178qJydHp512miZOnKgxY8Zo4MCBh/x8h8OhOXPm6Mwzz9S0adPUq1cvXXrppSosLGyY4wHg6Dksy7JMhwAAAPbByAUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAir/w8KvDsSkjzCYAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a pie plot showing the distribution of female versus male mice using Pandas\n",
    "\n",
    "# Count the occurrences of each gender\n",
    "gender_counts = combined_data['Sex'].value_counts()\n",
    "\n",
    "# Create a pie plot using Pandas\n",
    "gender_counts.plot(kind='pie', autopct='%1.1f%%')\n",
    "\n",
    "# Set the aspect ratio to 'equal' for a circular pie\n",
    "plt.axis('equal')\n",
    "\n",
    "# Display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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IJbVlUvbFu8rG19KO5ZJ3mrTqcxLzJA6nix1HBwqFJ0GS+ltTKcC4gblArATywrtErp7jbTr6/230s323MjL4ZRyukqt+0pt+kit+0ht+4f+dDpNpwPiFuUCiAc+j7RnrbRng1S+RSrbEvqzfItUsT26i4fDKaW3k7I6hW45XaU2fUMFIq+XlJBsOiGA76FcAPEu4Jcqt4UKR+V2qaZEqt0b2nujtnTf3/eG7vdUKCxzPFyJUnK2lJK978+c0N9TckITK7Py9906SZkdWAoKxBjKBYCjZ1mSv17ye6SAN/Snv37/LVAvyRFaxulwhm6uRMmdtP/PpAyOHgdsjnIBAADCihlPAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAAAgrCgXAOJS165d9be//c10DMCWKBcAWtzUqVPlcDgOuG3atMl0NAAtwG06AID4MHbsWD399NON7mvdurWhNABaEiMXACIiKSlJ7dq1a3RzuVx6++23NWjQICUnJ6t79+66++675ff7G77O4XBoxowZmjBhglJTU9W3b18tWLBAmzZt0siRI5WWlqZhw4apoKCg4WsKCgp0/vnnq23btkpPT9eQIUM0b968w+arqKjQtddeqzZt2igzM1Nnn322VqxY0WL/HoCdUS4AGDN37lxdfvnl+vnPf641a9ZoxowZeuaZZ3Tvvfc2+rx77rlHV155pZYvX64+ffrosssu03XXXafp06frq6++kiTddNNNDZ9fXV2tcePGad68eVq2bJnGjBmjiRMnauvWrQfNYVmWxo8fr507d2rOnDlasmSJBg4cqHPOOUelpaUt9w8A2JUFAC3sqquuslwul5WWltZwu/DCC63hw4db9913X6PPff7556327ds3fCzJuvPOOxs+XrBggSXJevLJJxvue/nll63k5OTDZujXr5/18MMPN3zcpUsX669//atlWZb13//+18rMzLQ8Hk+jr+nRo4c1Y8aMJn+/QLxjzgWAiDjrrLP06KOPNnyclpamnj17avHixY1GKgKBgDwej2pra5WamipJGjBgQMPjbdu2lSSdcMIJje7zeDyqrKxUZmamampqdPfdd+udd97Rjh075Pf7VVdXd8iRiyVLlqi6ulqtWrVqdH9dXV2jyy0Ajg7lAkBEfFsmvisYDOruu+/WlClTDvj85OTkhr8nJCQ0/N3hcBzyvmAwKEm6/fbbNXfuXD300EPq2bOnUlJSdOGFF8rr9R40WzAYVPv27fXxxx8f8Fh2dvbRfYMAGlAuABgzcOBArV+//oDScaw+++wzTZ06VZMnT5YUmoNRWFh42Bw7d+6U2+1W165dw5oFiEeUCwDG/OY3v9GECROUn5+viy66SE6nUytXrtSqVav0hz/8odnP27NnT82ePVsTJ06Uw+HQXXfd1TCqcTCjRo3SsGHDNGnSJN1///3q3bu3duzYoTlz5mjSpEkaPHhws7MA8YjVIgCMGTNmjN555x19+OGHGjJkiE499VT95S9/UZcuXY7pef/6178qJydHp512miZOnKgxY8Zo4MCBh/x8h8OhOXPm6Mwzz9S0adPUq1cvXXrppSosLGyY4wHg6Dksy7JMhwAAAPbByAUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAgrygUAAAir/w8KvDsSkjzCYAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a pie plot showing the distribution of female versus male mice using pyplot\n",
    "\n",
    "# Count the occurrences of each gender\n",
    "gender_counts = combined_data['Sex'].value_counts()\n",
    "\n",
    "# Extract the gender labels and their corresponding counts\n",
    "genders = gender_counts.index\n",
    "counts = gender_counts.values\n",
    "\n",
    "# Create a pie plot using pyplot\n",
    "plt.pie(counts, labels=genders, autopct='%1.1f%%')\n",
    "\n",
    "# Set y-axis label\n",
    "plt.ylabel(\"Sex\")\n",
    "\n",
    "# Set the aspect ratio to 'equal' for a circular pie\n",
    "plt.axis('equal')\n",
    "\n",
    "# Display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Quartiles, Outliers and Boxplots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the final tumor volume of each mouse across four of the treatment regimens:  \n",
    "# Capomulin, Ramicane, Infubinol, and Ceftamin\n",
    "\n",
    "# Start by getting the last (greatest) timepoint for each mouse\n",
    "\n",
    "\n",
    "# Merge this group df with the original DataFrame to get the tumor volume at the last timepoint\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Capomulin's potential outliers: Series([], Name: Tumor Volume (mm3), dtype: float64)\n",
      "Ramicane's potential outliers: Series([], Name: Tumor Volume (mm3), dtype: float64)\n",
      "Infubinol's potential outliers: 31    36.321346\n",
      "Name: Tumor Volume (mm3), dtype: float64\n",
      "Ceftamin's potential outliers: Series([], Name: Tumor Volume (mm3), dtype: float64)\n"
     ]
    }
   ],
   "source": [
    "# Put treatments into a list for for loop (and later for plot labels)\n",
    "\n",
    "\n",
    "# Create empty list to fill with tumor vol data (for plotting)\n",
    "\n",
    "\n",
    "# Calculate the IQR and quantitatively determine if there are any potential outliers. \n",
    "\n",
    "    \n",
    "    # Locate the rows which contain mice on each drug and get the tumor volumes\n",
    "\n",
    "    \n",
    "    # add subset \n",
    "\n",
    "    \n",
    "    # Determine outliers using upper and lower bounds\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Z3T9+vVC55Jq1arp0UcfvesxK6vinONjY2OVmZmpunXrFvoZSUxMdOjnoyzOGwVu/ndbMJbHLOdtwowTBQcHy2Kx3PUkcO7cOfXu3VvNmzfXp59+qtjYWK1YsUKSinQV3+4H5uZlt643DKPIspt/qRWsu92y/Px8STcugRm3POHibl3Yd3LrL1OLxWJro6Ly9PRUUFCQWrZsqbfffls5OTmaN2+eJGnLli2aOnWqRo4cqZ07d+ro0aMaMWKErl27VugYt/u+2fO9vNfgz+HDhys2NlbLli3T/v37dfToUdWtW7dYdRS0mZ+fr759++ro0aOFXgkJCXr88cfv2n5lYe+//4JfRDf/7Nnzc3e3X653q+VOv5xvdy5B8c7x+fn5atCgQZGfj1OnTumVV16xq72yOm/c7ji3/m4o7wgzTlSnTh317NlTK1asKNTLUuDy5cs6dOiQcnNztXTpUnXo0EFNmzbVxYsXi2ybm5trG9MiSadOndLly5dt/wMODQ3Vt99+W2if/fv3KzQ0tERfg4+Pj5KTkwstq0hzEZSluXPn6o9//KMuXryoffv2qVOnTho/frxatWqloKCgUunFaNmypfbt23fHX4T79u3TpEmT1Lt3bzVr1kxWq1X/+c9/7GqjdevWOnHihAIDAxUUFFTodbtxBLi3gjsCb/7Zu9PP3YEDB2x/T0tL0+nTp23nBXsFBQXpvvvuK3QuuX79ug4dOlTic0lFVJxzfOvWrZWSkqKqVasW+fmoV6/eHY993333KS8vr9CysjpvVASEGSd75513lJeXp0cffVSffvqpEhISFBcXp7ffflsdO3ZUkyZNlJubq//5n//R2bNn9eGHH2rVqlVFjlOtWjVNnDhRBw8e1OHDhzVixAh16NBBjz76qKQbgwDXr1+vVatWKSEhQVFRUdq6datefvnlEtXfrVs3HTp0SB988IESEhI0d+5cHT9+vETHrKy6dOmiZs2aKTIyUkFBQTp06JC+/PJLnT59WnPmzFFMTIzT23zxxRdtg8UPHTqkhIQEffjhhzp16pSkG7+8PvzwQ8XFxengwYMaPHiw3bfyTpgwQT///LOef/55fffddzp79qx27typkSNHFjkZo3jc3d3VoUMHvf766zp58qS++eYbzZ49+7bbzp8/X7t379bx48c1fPhw1atXz645bm7m6empcePG6ZVXXtGOHTt08uRJjRo1SllZWXrhhRdK8BVVXPc6xz/55JPq2LGjBgwYoC+//FJJSUnav3+/Zs+eXeg/qLcKDAzUwYMHlZSUpP/85z/Kz88vs/NGRUCYcbLGjRvr8OHD6tq1q1566SU1b95c3bt31+7du7Vy5Uo98sgjioqK0uLFi9W8eXNt2rRJixYtKnIcDw8PzZgxQ4MGDVLHjh3l7u6ujz/+2LZ+wIABeuutt/TGG2+oWbNmWr16tdatW6cuXbqUqP6ePXtqzpw5mj59utq1a6eMjAwNHTq0RMeszKZNm6a1a9dqwIABGjhwoJ577jm1b99eP/30k8aPH+/09urWrauvv/5amZmZCgsLU5s2bbR27Vpb9/H777+vtLQ0tWrVSkOGDNGkSZNUv359u9rw9/fX3//+d+Xl5alnz55q3ry5Jk+eLG9v70LX7WGf999/X9evX1fbtm01efJkLViw4Lbbvf7665o8ebLatGmj5ORkffbZZ7rvvvscbvf111/Xb3/7Ww0ZMkStW7fWv/71L3355ZeqXbu2w8esyO51jrdYLNq+fbsef/xxjRw5Uk2bNtXvfvc7JSUl2cYt3s7LL7+sKlWq6OGHH5aPj4/Onz+vsWPHlsl5oyKwGLcOkIDLrV+/XlOmTGH6cAAAioH/RgEAAFMjzAAAAFPjMhMAADA1emYAAICpEWYAAICpEWYAAICpEWYAAICpEWYAAICpEWYAAICpEWYAAICpEWYAAICpEWYAAICp/T8ojXMI63ORKAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a box plot that shows the distrubution of the tumor volume for each treatment group.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Line and Scatter Plots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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njwZTz75JLZs2YKAgABMmTIFKSkpytfm5+ejb9+++OOPP/Dmm29ix44dmDZtGuLi4vDUU081+ZmsXLkSu3fvxieffILvvvsOVVVVGDFiBMrKygAAb7zxBh5++GEAUBnS6NSp0y1/znFxcZg2bRq6deuGzZs349NPP8XJkycRHh6OCxcuAGgY7nv99dcB/D1k8sYbb9z2/AHA+PHjERoaip9//hlPPfUUPv74Y8ydOxdjxoxBbGwstmzZgiFDhih/VxsVFhYiIiICu3btwttvv41t27YhJiYGL730EmbOnHnH923OiBEjkJKSgqVLl2L37t1YtWoVevbsqfIHweLFi/Hoo48iKCgIP/zwA7755htUVFTgvvvuw5kzZ9R6XwAYOXIk9PX1YWdnh3HjxuHUqVMq2xufh4SENHltSEiIyv61tbXN/lHV2Hby5Em16yQJiERtID8/XwQgTpgwQa3XKxQKsa6uTkxMTBQBiCdOnFBumzx5sghA/PTTT1Ve8+6774oAxP3794uiKIo7d+4UAYhLly5V2W/Tpk0iAHHNmjXKNg8PD9HU1FS8fPmysu348eMiALFTp05iVVWVsn3r1q0iAHHbtm3KtkGDBomDBg1q8jkmT54senh4qLQBEBcsWKB8Hh8fLwIQ4+Pjm3zGH374QeW1I0aMEAMCApq8z79169at2Xoa32vgwIEq7VVVVaKdnZ04atQolXa5XC6GhoaKffv2veV71dfXi7W1taKfn584d+5cZXtycrIIQFy3bl2T1zR+vp9//lnZVldXJzo6OooAxNTUVGV7cXGxqK+vL77wwgvKtqefflq0sLAQs7OzVY77wQcfiADE06dPi6IoillZWSIAsXv37mJ9fb1yvyNHjogAxA0bNijbZsyYId7tP5GlpaWiqampOGLECJX2nJwc0djYWHzssceUbevWrRMBiMnJyXc87oIFC0QA4ocffqjS3qNHDxGAuHnzZmVb489r3LhxyrZXXnlFBCAePnxY5fXPPvusKAiCmJ6eLopi879zovj3z6vxnBUVFYkAxE8++eSWNefk5IgGBgbi888/r9JeUVEhuri4iOPHj7/tZ26ulh07doivvfaa+Ouvv4qJiYniihUrRDc3N9Hc3Fw8fvy4cr/vvvtOBCAePHiwyXH/+9//ikZGRsrnY8aMEW1sbMSKigqV/e677z4RgLh4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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a line plot of tumor volume vs. time point for a single mouse treated with Capomulin\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjMAAAGwCAYAAABcnuQpAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjYuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8o6BhiAAAACXBIWXMAAA9hAAAPYQGoP6dpAABAYElEQVR4nO3de1hVZf7//9cGFDzgVkkEhNTwiGhZaulYimmSXqD2mXLyUFozlmkeKi1Lh2wq1CbHjjpqo5WlTd/M0akhrQQ1Kw9oHicdQkXFaLI4aHhgr98f/mDactoL92bvBc/Hde3rat9ruXi7Lm29vNd9sBmGYQgAAMCi/LxdAAAAwJUgzAAAAEsjzAAAAEsjzAAAAEsjzAAAAEsjzAAAAEsjzAAAAEsL8HYBnuZwOHTy5EkFBwfLZrN5uxwAAOACwzCUn5+viIgI+flV3PdS48PMyZMnFRUV5e0yAABAFWRlZSkyMrLCc2p8mAkODpZ06WY0atTIy9UAAABX5OXlKSoqquQ5XpEaH2aKXy01atSIMAMAgMW4MkSEAcAAAMDSCDMAAMDSCDMAAMDSCDMAAMDSfCbMJCcny2azacqUKU7tBw8eVGJioux2u4KDg3XTTTfp2LFj3ikSAAD4HJ8IM9u3b9fixYvVpUsXp/aMjAz17t1bHTp0UGpqqr755hvNmjVLQUFBXqoUAAD4Gq9PzS4oKNDIkSO1ZMkSPfvss07HnnrqKQ0aNEjz5s0rabvmmmuqu0QAAODDvN4zM2HCBA0ePFj9+/d3anc4HProo4/Url07DRw4UKGhobrxxhu1Zs2aCq937tw55eXlOX0AAEDN5dUws2rVKqWnpys5ObnUsZycHBUUFGjOnDmKj4/X+vXrNWzYMN1xxx1KS0sr95rJycmy2+0lH7YyAACgZvPaa6asrCxNnjxZ69evL3MMjMPhkCQNGTJEU6dOlSRdd9112rp1qxYtWqQ+ffqUed0ZM2bokUceKflevBwyAABwnyKHoW2Zp5WTX6jQ4CD1aN1U/n7e2dDZa2Fm586dysnJ0Q033FDSVlRUpE2bNunVV1/VmTNnFBAQoJiYGKdf17FjR23ZsqXc6wYGBiowMNBjdQMAUNul7MvW7HUHlJ1bWNIWbg9SUkKM4mPDq70er4WZW2+9VXv37nVqGzt2rDp06KDHH39cgYGB6t69u7799luncw4dOqSWLVtWZ6kAAOD/l7IvW+NXpMu4rP1UbqHGr0jXwlHXV3ug8VqYCQ4OVmxsrFNbgwYNFBISUtI+bdo0DR8+XLfccovi4uKUkpKidevWKTU11QsVAwBQuxU5DM1ed6BUkJEkQ5JN0ux1BzQgJqxaXzl5fTZTRYYNG6ZFixZp3rx56ty5s5YuXaoPPvhAvXv39nZpAADUOtsyTzu9WrqcISk7t1DbMk9XX1HygXVmfq2sHpf77rtP9913X/UXAwAAnOTklx9kqnKeu/h0zwwAAPAdocGurcDv6nnuQpgBAAAu6dG6qcLtQSpvNIxNl2Y19WjdtDrLIswAAADX+PvZlJRwacmUywNN8fekhJhqX2+GMAMAAFwWHxuuhaOuV5jd+VVSmD3IK9OyJR8bAAwAAHxffGy4BsSEsQIwAACwLn8/m3pGh3i7DEm8ZgIAABZHmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJZGmAEAAJYW4O0CAACo7YochrZlnlZOfqFCg4PUo3VT+fvZvF2WZRBmAADwopR92Zq97oCycwtL2sLtQUpKiFF8bLgXK7MOXjMBAOAlKfuyNX5FulOQkaRTuYUavyJdKfuyvVSZtRBmAADwgiKHodnrDsgo41hx2+x1B1TkKOsM/BphBgAAL9iWebpUj8yvGZKycwu1LfN09RVlUYyZAQCUi4GpnpOTX36Qqcp5tRlhBgBQJgamelZocJBbz6vNeM0EACiFgame16N1U4Xbg1ReP5dNl8Jjj9ZNq7MsSyLMAACcMDC1evj72ZSUECNJpQJN8fekhBhe67mAMAMAcMLA1OoTHxuuhaOuV5jd+VVSmD1IC0ddz+s8FzFmBgDgxOoDU602aDk+NlwDYsIsVbOvIcwAQDWxykPWygNTrTpo2d/Ppp7RId4uw7IIMwBQDaz0kC0emHoqt7DMcTM2XXoN4msDU4sHLV9ec/GgZV7b1FyMmQEAD7PazCArDkxl0HLtRpgBAA+y6kPWagNTGbRcu/GaCQA8yMxD1tfGTFhpYKrVBy3jyhBmAMCDrP6QtcrAVCsPWsaV4zUTAHgQD9nqwWq6tRthBgA8iIds9bDioGW4D2EGADyIh2z1sdqgZbiPzTAM3xpC72Z5eXmy2+3Kzc1Vo0aNvF0OgFrKSuvMWJ1VFidExcw8vwkzAFBNeMgCrjPz/GY2EwBUE6vMDAKshjEzAADA0ggzAADA0nwmzCQnJ8tms2nKlCllHn/ggQdks9m0YMGCaq0LAAD4Np8IM9u3b9fixYvVpUuXMo+vWbNGX3/9tSIiIqq5MgAA4Ou8HmYKCgo0cuRILVmyRE2aNCl1/MSJE5o4caLeeecd1alTxwsVAgAAX+b1MDNhwgQNHjxY/fv3L3XM4XBo9OjRmjZtmjp16uTS9c6dO6e8vDynDwAAqLm8OjV71apVSk9P1/bt28s8PnfuXAUEBGjSpEkuXzM5OVmzZ892V4kAAMDHea1nJisrS5MnT9aKFSsUFFR6g7WdO3fqpZde0vLly2Wzub6o1IwZM5Sbm1vyycrKcmfZAADAx3htBeA1a9Zo2LBh8vf3L2krKiqSzWaTn5+f5s6dq2nTpsnPz8/puJ+fn6KionTkyBGXfg4rAAMAYD2WWAH41ltv1d69e53axo4dqw4dOujxxx9XeHi4Bg4c6HR84MCBGj16tMaOHVudpQIAAB/mtTATHBys2NhYp7YGDRooJCSkpD0kxHnZ7zp16igsLEzt27evtjoBAIBv8/psJgAAgCvhUxtNpqamVnjc1XEyAACg9qBnBgAAWBphBgAAWBphBgAAWBphBgAAWFqVBgBnZWXpyJEjOnv2rJo1a6ZOnTopMDDQ3bUBAABUyuUwc/ToUS1atEgrV65UVlaWfr1wcN26dXXzzTdr3Lhx+r//+z+nVXsBAAA8yaXUMXnyZHXu3FmHDx/WM888o/379ys3N1fnz5/XqVOn9PHHH6t3796aNWuWunTpUu7GkQAAAO7mUs9M3bp1lZGRoWbNmpU6Fhoaqn79+qlfv35KSkrSxx9/rKNHj6p79+5uLxYAAPiGIoehbZmnlZNfqNDgIPVo3VT+fq5vDO1OXttosrqw0SQAAO6Vsi9bs9cdUHZuYUlbuD1ISQkxio8Nd8vPMPP8ZnALAABwWcq+bI1fke4UZCTpVG6hxq9IV8q+7GqvyVSYWbp0qe69914tW7ZMkvTee++pY8eOuuaaa5SUlOSRAgEAgG8ochiave6AynqlU9w2e90BFTmq96WPy7OZFixYoJkzZ2rgwIF66qmndPLkSf3lL3/R1KlT5XA49OKLL6pFixYaN26cJ+sFAMvypTEGQFVsyzxdqkfm1wxJ2bmF2pZ5Wj2jQ6qtLpfDzF//+lctXrxYI0aM0K5du9SjRw8tWrRI999/vyQpMjJSr732GmEGAMpQHWMMAE/LyS8/yFTlPHdx+TXT0aNH1bt3b0lS165d5e/vr5tuuqnk+M0336yMjAz3VwgAFueLYwyAqggNDnLree7icpipX7++zpw5U/K9WbNmatiwodM5Fy9edF9lAFAD+OoYA6AqerRuqnB7kMp7OWrTpR7HHq2bVmdZroeZDh06aM+ePSXfs7Ky1LJly5Lv//73v9WqVSu3FgcAVmdmjAHg6/z9bEpKiJGkUoGm+HtSQky1jwVzOczMnTtX7du3L/f4sWPH9MADD7ilKACoKXx1jAFQVfGx4Vo46nqF2Z1fJYXZg7Rw1PVeGQPm8gDg3/zmNxUef+ihh664GACoaXx1jAFwJeJjwzUgJsxnZudVadfsYgUFBXI4HE5trLILAP9TPMbgVG5hmeNmbLr0L9rqHmMAXCl/P1u1Tr+uiOkVgDMzMzV48GA1aNBAdrtdTZo0UZMmTdS4cWM1adLEEzUCgGX56hgDoCYx3TMzcuRISdLf/vY3NW/eXDYbfwEBoCLFYwwuX2cmjHVmALcwvdFkw4YNtXPnzgoHA/sSNpoE4CtYARhwnZnnt+meme7duysrK8syYQYAfIUvjTEAahLTYWbp0qV68MEHdeLECcXGxqpOnTpOx7t06eK24gAAMIsesNrHdJj54YcflJGRobFjx5a02Ww2GYYhm82moqIitxYIAICr2AOrdjIdZu677z517dpVK1euZAAwAMBnFO+BdflA0OI9sLy1oBs8z3SYOXr0qNauXas2bdp4oh4AAEyrbA8smy7tgTUgJoxXTjWQ6XVm+vXrp2+++cYTtQAAUCXsgVW7me6ZSUhI0NSpU7V371517ty51ADgxMREtxUHAIAr2AOrdjMdZh588EFJ0jPPPFPqGAOAAQDewB5YtZvp10wOh6PcD0EGAOANxXtglTcaxqZLs5rYA6tmMh1mAADwNeyBVbtVadfsbdu2KTU1VTk5OaV2zZ4/f75bCgNQfVhkDDUBe2DVXqbDzPPPP6+ZM2eqffv2pdaZYc0ZwHpYZAw1SXxsuAbEhBHOaxnTG002b95cc+fO1ZgxYzxUknux0SRQvvIWGSv+3z6LjAHwFjPPb9NjZvz8/PSb3/ymysUB8A2VLTImXVpkrMhh6t87AFDtTIeZqVOn6rXXXvNELQCqEYuMAagpTI+ZeeyxxzR48GBFR0crJiam1KJ5q1evdltxADyHRcYA1BSmw8zDDz+sjRs3Ki4uTiEhIQz6BSyKRcYA1BSmw8xbb72lDz74QIMHD/ZEPQCqSfEiY6dyC8scN2PTpSmtLDIGwNeZHjPTtGlTRUdHe6IWANWIRcYA1BSmw8zTTz+tpKQknT171hP1AKhGxYuMhdmdXyWF2YOYlg3AMkyvM9O1a1dlZGTIMAy1atWq1ADg9PR0txZ4pVhnBqgcKwAD8DVmnt+mx8wMHTq0qnUB8FH+fjb1jA7xdhkAUCWme2ashp4ZAACsx6MrALuihucjAADgQ1wKMx07dtS7776r8+fPV3je4cOHNX78eM2dO9ctxQEAAFTGpTEzr732mh5//HFNmDBBt912m7p166aIiAgFBQXpp59+0oEDB7RlyxYdOHBAEydO1EMPPeTpugEAACSZHDOzdetWvffee9q0aZOOHDmiX375RVdddZW6du2qgQMHatSoUWrcuLEHyzWPMTNA5ZjNBMDXeGw2U69evdSrV68rKq48ycnJevLJJzV58mQtWLBAFy5c0MyZM/Xxxx/ru+++k91uV//+/TVnzhxFRER4pAagNkrZl63Z6w44bToZbg9SUkIM68yAoAtLMD012xO2b9+uxYsXq0uXLiVtZ8+eVXp6umbNmqVrr71WP/30k6ZMmaLExETt2LHDi9UCNUfKvmyNX5FeajuDU7mFGr8inYXzajmCLqzCI7OZzCgoKNDIkSO1ZMkSNWnSpKTdbrdrw4YNuuuuu9S+fXvddNNNeuWVV7Rz504dO3as3OudO3dOeXl5Th8ApRU5DM1ed6DMfZmK22avO6AiB7MTa6PioPvrICP9L+im7Mv2UmVAaV4PMxMmTNDgwYPVv3//Ss/Nzc2VzWarcFxOcnKy7HZ7yScqKsqN1QI1x7bM06UeVL9mSMrOLdS2zNPVVxR8AkEXVuPVMLNq1Sqlp6crOTm50nMLCwv1xBNPaMSIERUOBJoxY4Zyc3NLPllZWe4sGagxcvLLDzJVOQ81B0EXVuO1MTNZWVmaPHmy1q9fr6CgoArPvXDhgn73u9/J4XDo9ddfr/DcwMBABQYGurNUoEYKDa74753Z81BzEHRhNVXqmcnIyNDMmTN19913KycnR5KUkpKi/fv3u3yNnTt3KicnRzfccIMCAgIUEBCgtLQ0vfzyywoICFBRUZGkS0HmrrvuUmZmpjZs2MD0asBNerRuqnB7kMqbl2LTpcGePVo3rc6y4AMIurAa02EmLS1NnTt31tdff63Vq1eroKBAkrRnzx4lJSW5fJ1bb71Ve/fu1e7du0s+3bp108iRI7V79275+/uXBJnDhw/r008/VUgIG+EB7uLvZ1NSQowklQo0xd+TEmKYhlsLEXRhNabDzBNPPKFnn31WGzZsUN26dUva4+Li9OWXX7p8neDgYMXGxjp9GjRooJCQEMXGxurixYv67W9/qx07duidd95RUVGRTp06pVOnTlW6rQIA18THhmvhqOsVZnf+F3aYPYhp2bUYQRdWY3rMzN69e/Xuu++Wam/WrJl+/PFHtxQlScePH9fatWslSdddd53TsY0bN6pv375u+1lAbRYfG64BMWEsjAYnxUH38nVmwlhnBj7IdJhp3LixsrOz1bp1a6f2Xbt2qUWLFldUTGpqasl/t2rVit23gWri72dTz2he48IZQRdWYTrMjBgxQo8//rjef/992Ww2ORwOffHFF3rsscd0zz33eKJGAKgRrLg1AEEXVmBqo0np0uyiMWPGaNWqVTIMo2Tm0YgRI7R8+XL5+/t7qtYqYaNJAL6ArQEAc8w8v02HmWIZGRnatWuXHA6HunbtqrZt21apWE8jzADwtvL2wCruk2GwNVCax3bN/rXo6GhFR0dX9ZcDQK1Q2dYANl3aGmBATJjPv3ICfJXpMGMYhv7f//t/2rhxo3JycuRwOJyOr1692m3FAYDVmdkagLEpQNWYDjOTJ0/W4sWLFRcXp+bNm8tm418SAFAetgYAPM90mFmxYoVWr16tQYMGeaIeAKhR2Bqg+llx1hiujOkwY7fbdc0113iiFgCocYq3BjiVW1jmuBmbLi1Ex9YA7sGssdrJ9HYGTz/9tGbPnq1ffvnFE/UAQI1SvDVAedNGDbE1gLsUzxq7fIzSqdxCjV+RrpR92V6qDJ5mumfmzjvv1MqVKxUaGqpWrVqpTp06TsfT09PdVhwAAK5g1ljtZjrMjBkzRjt37tSoUaMYAAwAlSh+yJaHh6x7MGusdjMdZj766CN98skn6t27tyfqAYAahYds9WDWWO1mesxMVFQUK+kCgIt4yFYPZo3VbqbDzIsvvqjp06fryJEjHigHAGoWHrLVo3jWWHkv6my6NKuJWWM1k+nXTKNGjdLZs2cVHR2t+vXrlxoAfPr0abcVBwBWx9Ts6lE8a2z8inTZJKd7XRxwmDVWc5kOMwsWLPBAGQBQM/GQrT7xseFaOOr6UuvMhLHOTI1X5V2zrYJdswH4AhZzqz6sAFwzmHl+mw4zx44dq/D41VdfbeZyHkeYAeAreMgCrjPz/Db9mqlVq1YVri1TVFRk9pIAUCv4+9mYfg14gOkws2vXLqfvFy5c0K5duzR//nw999xzbisMAADAFabDzLXXXluqrVu3boqIiNALL7ygO+64wy2FAQAAuML0OjPladeunbZv3+6uywEAALjEdM9MXl6e03fDMJSdna2nn35abdu2dVthAAAArjAdZho3blxqALBhGIqKitKqVavcVhgAAIArTIeZjRs3On338/NTs2bN1KZNGwUEmL4cAADAFTGdPvr06eOJOgAAAKrEpTCzdu1aly+YmJhY5WIAAADMcinMDB061KWL2Ww2Fs0DAADVyqUw43A4PF0HAABAlbhtnRkAAABvqFKYSUtLU0JCgtq0aaO2bdsqMTFRmzdvdndtAAAAlTIdZlasWKH+/furfv36mjRpkiZOnKh69erp1ltv1bvvvuuJGgEAAMplMwzDMPMLOnbsqHHjxmnq1KlO7fPnz9eSJUt08OBBtxZ4pcxsIQ4AAHyDmee36Z6Z7777TgkJCaXaExMTlZmZafZyAAAAV8R0mImKitJnn31Wqv2zzz5TVFSUW4oCAABwlekVgB999FFNmjRJu3fvVq9evWSz2bRlyxYtX75cL730kidqBAAAKJfLYeaHH35Qs2bNNH78eIWFhenFF1/U3//+d0mXxtG89957GjJkiMcKBQAAKIvLYaZFixZKTEzU/fffr6FDh2rYsGGerAsAAMAlLo+ZefPNN5WXl6eEhARFRUVp1qxZ+u677zxZGwAAQKVcDjN333231q9fr8zMTP3hD3/QO++8o7Zt2youLk7vvPOOCgsLPVknAABAmao0mykpKUnfffed1q9frxYtWmjcuHEKDw/XQw895IkaAQAAymV60byyfPDBBxo3bpx+/vlnn9s1m0XzAACwHjPPb9NTs4sd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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a scatter plot of mouse weight vs. the average observed tumor volume for the entire Capomulin regimen\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Correlation and Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The correlation between mouse weight and the average tumor volume is 0.84\n"
     ]
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Calculate the correlation coefficient and a linear regression model \n",
    "# for mouse weight and average observed tumor volume for the entire Capomulin regimen\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
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
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
