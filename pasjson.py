# Merci stackoverflow pr le script d'inversion des valeurs dans un .json
import json


def load_mapping_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def invert_mapping(original_mapping):
    return {value: key for key, value in original_mapping.items()}


def save_mapping_to_file(mapping, file_path):
    with open(file_path, 'w') as file:
        json.dump(mapping, file)


def main():
    original_mapping_file_path = input("Enter the path to the original JSON mapping file: ")

    original_mapping = load_mapping_from_file(original_mapping_file_path)

    if original_mapping:
        # Invert the mapping
        inverted_mapping = invert_mapping(original_mapping)

        # Input path to save the inverted JSON mapping file
        inverted_mapping_file_path = input("Enter the path to save the inverted JSON mapping file: ")

        # Save the inverted mapping to a new JSON file
        save_mapping_to_file(inverted_mapping, inverted_mapping_file_path)

        print(f"Inverted Mapping saved to {inverted_mapping_file_path}")
    else:
        print("Error: Original Mapping file not found.")


if __name__ == "__main__":
    main()
