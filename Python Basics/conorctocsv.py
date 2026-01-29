import pyorc
import csv

input_orc = "cdm_data_PRICINGUNMAPPED_pricing_um_lambda_shop_date_value=2025-05-29_RG_IC23_TC_1_SIE-BNA_7_202505290332_20250529073433.orc"
output_csv = "cdm_data_PRICINGUNMAPPED_pricing_um_lambda_shop_date_value=2025-05-29.csv"

with open(input_orc, "rb") as orc_file:
    reader = pyorc.Reader(orc_file)
    columns = reader.schema.fields.keys()

    with open(output_csv, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)  # header
        for row in reader:
            writer.writerow(row)

print(f"✅ Conversion complete. Saved as: {output_csv}")
