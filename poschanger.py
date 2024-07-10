import os
import xml.etree.ElementTree as ET

def process_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    modified = False

    for item in root.findall(".//Item[@type='CEntityDef']"):
        archetype = item.find('archetypeName')
        if archetype is not None and archetype.text == 'prop_bench_10':
            position = item.find('position')
            if position is not None:
                z = float(position.get('z'))
                new_z = z - 0.65
                position.set('z', f"{new_z:.5f}")
                modified = True

    if modified:
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print(f"Modified: {file_path}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(root, file)
                try:
                    process_xml_file(file_path)
                except ET.ParseError:
                    print(f"Error parsing XML file: {file_path}")

# Specify the directory path here
directory_path = 'C:\\Users\\U3F\\Desktop\\ltsren'

process_directory(directory_path)
