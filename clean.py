import json
import math

# 1. 建立 raw.txt 資料 (以 UN World Population 數據為例，單位：十億人)
raw_data = {
    "source": "UN World Population Prospects",
    "unit": "Billion",
    "data": {
        "2024": 8.16,
        "2030": 8.55,
        "2050": 9.66,
        "2100": 10.35
    }
}

with open('../data/raw.txt', 'w', encoding='utf-8') as f:
    f.write(json.dumps(raw_data, indent=4))

# 2. 計算人口數據
years = [2024, 2030, 2050, 2100]
values = [8.16, 8.55, 9.66, 10.35]

mean_val = round(sum(values) / len(values), 2)
total_growth_rate = round(((values[-1] - values[0]) / values[0]) * 100, 2)

# CAGR 計算公式: (End_Value / Start_Value) ^ (1 / Years) - 1
cagr_2024_2100 = round((math.pow(values[-1] / values[0], 1 / (2100 - 2024)) - 1) * 100, 2)
cagr_2024_2050 = round((math.pow(values[2] / values[0], 1 / (2050 - 2024)) - 1) * 100, 2)

# 3. 輸出 cleaned.json
cleaned_result = {
    "metadata": {
        "source": "UN World Population Prospects (2024 Revision)",
        "processed_by": "clean.py"
    },
    "population_projections": raw_data["data"],
    "analytics": {
        "mean_population": mean_val,
        "total_growth_rate_pct": total_growth_rate,
        "cagr_2024_2050_pct": cagr_2024_2050,
        "cagr_2024_2100_pct": cagr_2024_2100
    }
}

with open('../data/cleaned.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_result, f, indent=4, ensure_ascii=False)

print("Data processing complete. Outputs generated in /data/")