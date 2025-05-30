{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a42a52a4-5b7b-408e-bae5-5ec1deb568ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "# features.py\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "def decompose_plate(df):\n",
    "    \"\"\"\n",
    "    Extrait les composants de la plaque : lettres, chiffres, code région.\n",
    "    Exemple : X059CP797 → XCP, 059, 797\n",
    "    \"\"\"\n",
    "    df[\"letters\"] = df[\"plate\"].str[0] + df[\"plate\"].str[4:6]\n",
    "    df[\"digits\"] = df[\"plate\"].str[1:4].astype(int)\n",
    "    df[\"region_code\"] = df[\"plate\"].str[-3:]\n",
    "    return df\n",
    "\n",
    "\n",
    "def map_region_name(df, region_codes_dict):\n",
    "    \"\"\"\n",
    "    Ajoute le nom de la région à partir du code via REGION_CODES.\n",
    "    \"\"\"\n",
    "    reverse_region_map = {}\n",
    "    for region_name, codes in region_codes_dict.items():\n",
    "        for code in codes:\n",
    "            reverse_region_map[code] = region_name\n",
    "    df[\"region_name\"] = df[\"region_code\"].map(reverse_region_map)\n",
    "    return df\n",
    "\n",
    "\n",
    "def add_government_features(df, gov_codes):\n",
    "    \"\"\"\n",
    "    Marque les plaques gouvernementales avec importance et privilèges.\n",
    "    Ajoute :\n",
    "      - is_gov_plate (booléen)\n",
    "      - has_road_advantage (booléen)\n",
    "      - gov_importance_level (int)\n",
    "    \"\"\"\n",
    "    def gov_info(row):\n",
    "        for (let, (start, end), reg), (desc, is_forbidden, has_adv, level) in gov_codes.items():\n",
    "            if (\n",
    "                let == row[\"letters\"]\n",
    "                and reg == row[\"region_code\"]\n",
    "                and start <= row[\"digits\"] <= end\n",
    "            ):\n",
    "                return pd.Series([1, has_adv, level])\n",
    "        return pd.Series([0, 0, 0])\n",
    "    \n",
    "    df[[\"is_gov_plate\", \"has_road_advantage\", \"gov_importance_level\"]] = df.apply(gov_info, axis=1)\n",
    "    return df\n",
    "\n",
    "\n",
    "def enrich_dataset(df, region_codes, gov_codes):\n",
    "    \"\"\"\n",
    "    Pipeline complet : décomposition + mapping + étiquetage gouvernemental.\n",
    "    \"\"\"\n",
    "    df = decompose_plate(df)\n",
    "    df = map_region_name(df, region_codes)\n",
    "    df = add_government_features(df, gov_codes)\n",
    "    return df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdcb14e1-2322-4b22-929f-489f31182d95",
   "metadata": {},
   "outputs": [],
   "source": []
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
