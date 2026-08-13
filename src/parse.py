import re
from extract import extract_text_from_image

def parse_receipt(image_path):
    text = extract_text_from_image(image_path)

    lines = text.split('\n')

    data = {
        "date": None,
        "subtotal": None,
        "tax": None,
        "total": None,
        "items": []
    }

    # pattern for a dollar amount like "12.99" or "$12.99"
    price_pattern = r'\$?\d+\.\d{2}'

    # pattern for a date like "5/26/2016" or "05/26/2016" or "5/26/16" or "05/26/16"
    date_pattern = r'\d{1,2}/\d{1,2}/\d{2,4}'

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # look for date
        date_match = re.search(date_pattern, line)
        if date_match and data["date"] is None:
            data["date"] = date_match.group()

        # look for subtotal / tax / total using keywords as anchors
        if re.search(r'sub\s*total', line, re.IGNORECASE):
            price_match = re.search(price_pattern, line)
            if price_match:
                data["subtotal"] = float(price_match.group().replace("$", ""))

        elif re.search(r'\btax\b', line, re.IGNORECASE):
            price_match = re.search(price_pattern, line)
            if price_match:
                data["tax"] = float(price_match.group().replace("$", ""))

        elif re.search(r'\btotal\b', line, re.IGNORECASE):
            price_match = re.search(price_pattern, line)
            if price_match:
                data["total"] = float(price_match.group().replace("$", ""))

        # look for items
        item_match = re.match(r'^(.+?)\s+\d{6,}\w*\s+(\d+\.\d{2})', line)
        if item_match:
            name = item_match.group(1).strip()
            price = float(item_match.group(2))
            data["items"].append({"name": name, "price": price})

    return data

if __name__ == "__main__":
    image_path = 'data/receipts/sample_receipt.jpg'
    data = parse_receipt(image_path)
    print(data)