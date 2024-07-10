import os
import xml.etree.ElementTree as ET

def process_xml_file(file_path, target_archetype, new_flags_value):
    tree = ET.parse(file_path)
    root = tree.getroot()
    modified = False

    for item in root.findall(".//Item[@type='CEntityDef']"):
        archetype = item.find('archetypeName')
        if archetype is not None and archetype.text == target_archetype:
            flags = item.find('flags')
            if flags is not None:
                old_value = flags.get('value')
                flags.set('value', str(new_flags_value))
                modified = True
                print(f"In file {file_path}:")
                print(f"  Changed flags for {target_archetype} from {old_value} to {new_flags_value}")

    if modified:
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print(f"Modified: {file_path}")

def process_directory(directory, target_archetype, new_flags_value):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(root, file)
                try:
                    process_xml_file(file_path, target_archetype, new_flags_value)
                except ET.ParseError:
                    print(f"Error parsing XML file: {file_path}")

# Specify the directory path, target archetype name, and new flags value here
directory_path = '/path/to/your/xml/files'
target_archetype = 'prop_bench_07'  # Replace with the desired archetype name
new_flags_value = '1572897'  # Replace with the desired new flags value

process_directory(directory_path, target_archetype, new_flags_value)
