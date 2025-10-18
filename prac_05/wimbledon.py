"""
Wimbledon Data Processor
Estimate: 40 minutes
Actual:   (fill in after you finish)

Reads 'wimbledon.csv' (UTF-8 with BOM) and prints:
- Champion win counts
- Countries of champions, alphabetically
The CSV is expected to include headers with columns named
  'Champion' and 'Country' (case-insensitive). If there are no
  headers, it assumes the order: Year, Country, Champion, Runner-up, Score.
"""
import csv

FILENAME = "wimbledon.csv"

def read_rows(filename):
    with open(filename, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    return rows

def get_indexes(header):
    header_lower = [h.strip().lower() for h in header]
    if "champion" in header_lower and "country" in header_lower:
        i_champ = header_lower.index("champion")
        i_country = header_lower.index("country")
        return i_champ, i_country, True
    # Fallback to no-header format: Year, Country, Champion, Runner-up, Score
    return 2, 1, False

def build_summaries(rows):
    header = rows[0]
    i_champ, i_country, had_header = get_indexes(header)
    data_rows = rows[1:] if had_header else rows
    champion_to_count = {}
    countries = set()
    for row in data_rows:
        if not row:  # skip blank lines
            continue
        champion = row[i_champ].strip()
        country = row[i_country].strip()
        countries.add(country)
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count, countries

def main():
    rows = read_rows(FILENAME)
    champion_to_count, countries = build_summaries(rows)

    print("Wimbledon Champions:")
    for champion, count in sorted(champion_to_count.items()):
        print(f"{champion} {count}")
    print()
    country_list = sorted(countries)
    print(f"These {len(country_list)} countries have won Wimbledon:")
    print(", ".join(country_list))

if __name__ == "__main__":
    main()
