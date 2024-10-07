def process_adx_file(file_path, row_index, add_value):
    """
    Process an .adx file, update specific rows, and save to a new .adx file.
    
    Parameters:
    - file_path: str, the path to the input .adx file.
    - row_index: int, the index of the column to update (0-based index).
    - add_value: int, the value to add to the specified rows.
    
    Returns:
    - None: Writes the updated data to a new file.
    """
    output_file = file_path.replace('.adx', '_updated.adx')  # New file with _updated suffix
    
    with open(file_path, mode='r') as infile, open(output_file, mode='w') as outfile:
        # Iterate over each line in the input file
        for line in infile:
            columns = line.split()  # Split the line by spaces (assuming space-delimited)
            if len(columns) > 1 and columns[1] == '3':  # Check if the cow ID (column 1) is 3
                columns[row_index] = str(int(columns[row_index]) + add_value)  # Update value
            outfile.write(' '.join(columns) + '\n')  # Write updated line to the output file
    
    print(f"File processing complete. Updated .adx file saved as {output_file}")

# Example usage:
process_adx_file('path_to_your_input_file.adx', 2, 20)