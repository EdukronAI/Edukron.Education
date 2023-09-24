import os

# Define the directory where you want to create the files
directory = "D:/Blog/Edukron"

# Define the structure as a dictionary
structure = {
    "index.md": "",
    "introduction-python-data-types.md": "",
    "numeric-data-types.md": {
        "integers.md": "",
        "floating-point-numbers.md": "",
        "complex-numbers.md": "",
    },
    "text-data-types.md": {
        "strings.md": "",
        "string-methods.md": "",
    },
    "sequence-data-types.md": {
        "lists.md": "",
        "tuples.md": "",
        "range.md": "",
    },
    "mapping-data-types.md": {
        "dictionaries.md": "",
    },
    "set-data-types.md": {
        "sets.md": "",
        "frozensets.md": "",
    },
    "boolean-data-type.md": "",
    "binary-data-types.md": {
        "bytes.md": "",
        "bytearray.md": "",
        "memoryview.md": "",
    },
    "date-time-data-types.md": {
        "date.md": "",
        "time.md": "",
        "datetime.md": "",
        "timedelta.md": "",
    },
    "other-built-in-types.md": {
        "none-type.md": "",
        "ellipsis-type.md": "",
    },
    "type-conversion.md": "",
    "creating-custom-data-types.md": "",
    "common-operations-on-data-types.md": "",
    "python-type-hierarchy.md": "",
    "choosing-right-data-type.md": "",
    "best-practices-for-data-types.md": "",
    "python-versions-differences.md": "",
    "further-reading-resources.md": "",
    "license.md": "",
}

# Create directories and files based on the structure
def create_structure(base_path, structure):
    for item, subitems in structure.items():
        if isinstance(subitems, dict):
            # Create a directory
            os.makedirs(os.path.join(base_path, item), exist_ok=True)
            create_structure(os.path.join(base_path, item), subitems)
        else:
            # Create a file with content
            with open(os.path.join(base_path, item), "w") as file:
                file.write(f"# {item}\n\nThis is the content of {item}.")

# Call the function to create the structure
create_structure(directory, structure)
