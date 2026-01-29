import pyorc

orc_file = "dl1pricingunmapped_data_comp-pricing-unmapped_shop_date_value=2024-01-01_RG_CA_INBFR_Q14_1_CA1_202401010859_20240101140410.orc"
txt_file = "dl1pricingunmapped_data_comp-pricing-unmapped_shop_date_value=2024-01-01_RG_CA_INBFR_Q14_1_CA1_202401010859_20240101140410.txt"

with open(orc_file, "rb") as f, open(txt_file, "w", encoding="utf-8") as out:
    reader = pyorc.Reader(f)

    # FIXED
    out.write("|".join(reader.schema.fields) + "\n")

    for row in reader:
        out.write("|".join(map(str, row)) + "\n")

print("TXT file generated:", txt_file)
