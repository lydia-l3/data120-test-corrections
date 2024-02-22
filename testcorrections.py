#!/usr/bin/env python3

# proteins = ["PF13411.1", "PF12728.1", "PF01381.2", "PF00205.2", "PF10875", "PF05766.1", "PF00860.2", "PF10766.1", "PF11812.1"]

def count_unique_proteins(proteins):
    return len({protein.split('.')[0] for protein in proteins})

# print(count_unique_proteins(proteins))
  

def count_proteins(proteins):
    family_counts_dict = {}
     
    for protein in proteins:
        family_unique = protein.split('.')[0]
    
        if family_unique not in family_counts_dict:
            family_counts_dict[family_unique] = 1
        else:
            family_counts_dict[family_unique] += 1
        
    return family_counts_dict


def merge_protein_counts(counts_dict1, counts_dict2):
    combined_dict = {}

    # Use set union to get all unique keys from both dicts
    union_keys = set(counts_dict1.keys()) | set(counts_dict2.keys())

    # Use dict .get() to get the counts for keys from both dicts
    for key in union_keys:
        count1 = counts_dict1.get(key, 0) # default 0 if key not found
        count2 = counts_dict2.get(key, 0)
        
        # New dict stores tuples (with counts) as values
        combined_dict[key] = ((count1, count2))
    
    return combined_dict
   
# print(merge_protein_counts(dict1, dict2))

# dates_list = ["February 6, 1992", "February 18, 1992", "February 27, 1992", "September 6, 1994", "December 1, 1993"]


def dates_to_iso8601(dates): 
    dates_in_iso = []
    
    # Dictionary for month mapping to number
    months = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}
    
    for date in dates:
        parts = date.split(" ")
        month = parts[0]
        day = parts[1].replace(",","")
        year = parts[2]

        if len(day) == 1:
            day = "0" + day
        
        iso_date = year + "-" + months[month] + "-" + day
        dates_in_iso.append(iso_date)

    return dates_in_iso
        
# print(dates_to_iso8601(dates_list))


# Helper function for sort_dates function
def bubble_sort_dates(date_tuples):
    # Iterate through each element
    for i in range(len(date_tuples)-1):
        for j in range(0, len(date_tuples)-i-1):
            # Swap element if greater than the next
            if date_tuples[j] > date_tuples[j+1]:
                date_tuples[j], date_tuples[j+1] = date_tuples[j+1], date_tuples[j]
    return date_tuples

def sort_dates(dates):
    # Dictionary for month mapping to number
    months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    
    # Convert each date in list to a tuple
    date_tuples = []
    for date in dates:
        parts = date.split(" ")
        month = months[parts[0]]
        day = int(parts[1].replace(",",""))
        year = int(parts[2])
        date_tuples.append((month, day, year))
    
    # Implement helper function to sort dates
    bubbled_sorted_dates = bubble_sort_dates(date_tuples)

    # Invert months dictionary mapping using dict .items()
    num_to_months = {num: month for month, num in months.items()}

    # Convert dates back to original dates_list format using f formatting
    original_dates = [f"{num_to_months[month]} {day}, {year}" for month, day, year in bubbled_sorted_dates]
    
    return original_dates

# print(sort_dates(dates_list))
