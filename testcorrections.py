#!/usr/bin/env python3


def count_unique_proteins(proteins):
    # Set comprehension to split on period and extract first part
    # Find number of unique elements in the set
    return len({protein.split('.')[0] for protein in proteins})


def count_proteins(proteins):
    family_counts_dict = {}

    # Iterate through list, split on period, extract first part
    for protein in proteins:
        family_unique = protein.split('.')[0]

        # Create dict
        if family_unique not in family_counts_dict:
            # Add key to dict if family num not already in dict
            family_counts_dict[family_unique] = 1 
        else:
            # Increment count of key if family num already in dict
            family_counts_dict[family_unique] += 1 

    return family_counts_dict


def merge_protein_counts(counts_dict1, counts_dict2):
    combined_dict = {}

    # Use set union to get all unique keys from both dicts
    union_keys = set(counts_dict1.keys()) | set(counts_dict2.keys())

    # Iterate through all keys and get the counts
    for key in union_keys:
        count1 = counts_dict1.get(key, 0) # default 0 if key not found
        count2 = counts_dict2.get(key, 0)

        # New dict stores tuples (with counts) as values
        combined_dict[key] = ((count1, count2))

    return combined_dict


# Define months as a global variable
months = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}


def dates_to_iso8601(dates):
    dates_in_iso = []

    # Iterate through dates, split into parts, extract
    for date in dates:
        parts = date.split(" ")
        month = parts[0]
        day = parts[1].replace(",","")
        year = parts[2]

        # Ensure date has leading zero if only single digit
        if len(day) == 1:
            day = "0" + day

        # Format and order dates to match ISO format
        iso_date = year + "-" + months[month] + "-" + day
        dates_in_iso.append(iso_date)

    return dates_in_iso


def sort_dates(dates):
    # Use dates_to_iso8601 function as helper for sorting
    dates_in_iso = dates_to_iso8601(dates) 
    dates_in_iso.sort()

    # Invert months dict mapping back to names
    num_to_months = {num: month for month, num in months.items()}

    # Convert sorted dates back to original format
    sorted_dates = []

    for date in dates_in_iso:
        year, month, day = date.split('-')
        original_sorted = f"{num_to_months[month]}, {day}, {year}"
        sorted_dates.append(original_sorted)

    return sorted_dates
