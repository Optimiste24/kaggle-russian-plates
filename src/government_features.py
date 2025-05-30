{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eecd547d-a926-4287-b940-722e00cdcefd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from supplemental_english import GOVERNMENT_CODES\n",
    "\n",
    "def add_government_flags(df):\n",
    "    \"\"\"\n",
    "    Ajoute 3 variables :\n",
    "    - is_government (0/1)\n",
    "    - gov_agency (nom de l'agence)\n",
    "    - gov_significance (niveau d'importance 1-10)\n",
    "    \"\"\"\n",
    "    df['is_government'] = 0\n",
    "    df['gov_agency'] = None\n",
    "    df['gov_significance'] = 0\n",
    "    \n",
    "    for (letters, num_range, region), (agency, _, _, significance) in GOVERNMENT_CODES.items():\n",
    "        # Vérifie si la plaque correspond aux critères\n",
    "        mask = (\n",
    "            (df['letter1'] == letters[0]) & \n",
    "            (df['letters2'] == letters[1:]) & \n",
    "            (df['digits'].between(num_range[0], num_range[1])) & \n",
    "            (df['region_code'] == region)\n",
    "        \n",
    "        # Met à jour les flags\n",
    "        df.loc[mask, 'is_government'] = 1\n",
    "        df.loc[mask, 'gov_agency'] = agency\n",
    "        df.loc[mask, 'gov_significance'] = significance\n",
    "    \n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:.conda-kaggle_plates]",
   "language": "python",
   "name": "conda-env-.conda-kaggle_plates-py"
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
   "version": "3.9.21"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
