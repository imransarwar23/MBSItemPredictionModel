import xml.etree.ElementTree as ET
import pandas as pd

def convert_mbs_xml_to_csv(xml_path: str, csv_output_path: str):
    # Parse XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    mbs_data = []

    for data in root.findall(".//Data"):
        item_num = data.findtext("ItemNum")
        description = data.findtext("Description")
        fee = data.findtext("ScheduleFee")
        derived_fee = data.findtext("DerivedFee")

        if item_num and description:
            mbs_data.append({
                "ItemNum": item_num.strip(),
                "Description": description.strip().replace("\n", " "),
                "Fee": fee.strip() if fee else None,
                "DerivedFee": derived_fee.strip() if derived_fee else None
            })

    # Convert to DataFrame and export
    df = pd.DataFrame(mbs_data)
    df.to_csv(csv_output_path, index=False)
    print(f"CSV exported to: {csv_output_path}")
    print(f"Total items exported: {len(df)}")

# Example usage
if __name__ == "__main__":
    convert_mbs_xml_to_csv(
        xml_path="mbs_items.XML",
        csv_output_path="mbs_items.csv"
    )
