import re
import csv
import os

# === CONFIGURATION ===
# 🔹 Change this to the full path of your SQL file
input_file = r"C:\python_data_engineering\gitrepo\Learn2025\prod_gba_db_schema_20250121.sql"

# 🔹 Output CSV will be created in the same folder as the input file
output_csv = os.path.join(os.path.dirname(input_file), "greatest_least_usage.csv")

# === READ FILE ===
with open(input_file, "r", encoding="utf-8") as f:
    sql = f.read()

# === SPLIT BY DDL DEFINITIONS ===
objects = re.split(r"(?i)(?=create\s+or\s+replace\s+(?:view|procedure)\s+)", sql)

results = []

# === PARSE EACH OBJECT ===
for obj in objects:
    # Check for GREATEST and LEAST usage
    funcs = []
    if re.search(r"(?i)\bgreatest\b", obj):
        funcs.append("GREATEST")
    if re.search(r"(?i)\bleast\b", obj):
        funcs.append("LEAST")

    if funcs:
        # Extract object type and name
        match = re.search(r"(?i)create\s+or\s+replace\s+(view|procedure)\s+([\w\"\.]+)", obj)
        if match:
            obj_type = match.group(1).upper()
            obj_name = match.group(2)
            results.append({
                "Object_Type": obj_type,
                "Object_Name": obj_name,
                "Matched_Function": ", ".join(funcs)
            })

# === WRITE TO CSV ===
with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Object_Type", "Object_Name", "Matched_Function"])
    writer.writeheader()
    writer.writerows(results)

print(f"✅ Extraction complete! {len(results)} objects found.")
print(f"📄 Results saved to: {output_csv}")
