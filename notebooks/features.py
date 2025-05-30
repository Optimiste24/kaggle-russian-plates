# features.py

import pandas as pd

def decompose_plate(df):
    df["letters"] = df["plate"].str[0] + df["plate"].str[4:6]
    df["digits"] = df["plate"].str[1:4].astype(int)
    df["region_code"] = df["plate"].str.extract(r'(\d{2,3})$')[0]

    return df

def map_region_name(df, region_codes_dict):
    reverse_region_map = {}
    for region_name, codes in region_codes_dict.items():
        for code in codes:
            reverse_region_map[code] = region_name
    df["region_name"] = df["region_code"].map(reverse_region_map)
    return df

def add_government_features(df, gov_codes):
    def gov_info(row):
        for (let, (start, end), reg), (desc, is_forbidden, has_adv, level) in gov_codes.items():
            if (
                let == row["letters"]
                and reg == row["region_code"]
                and start <= row["digits"] <= end
            ):
                return pd.Series([1, has_adv, level])
        return pd.Series([0, 0, 0])
    
    df[["is_gov_plate", "has_road_advantage", "gov_importance_level"]] = df.apply(gov_info, axis=1)
    return df

def enrich_dataset(df, region_codes, gov_codes):
    df = decompose_plate(df)
    df = map_region_name(df, region_codes)
    df = add_government_features(df, gov_codes)
    return df
