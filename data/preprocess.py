import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import argparse
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt 
import matplotlib.patches as patches

def xml_to_csv(path):
    xml_list = []
    for file in os.scandir(path):
        if file.is_file() and file.name.endswith(('.xml')):
            xml_file = os.path.join(path, file.name)
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for member in root.findall('object'):
                value = (root.find('filename').text,
                        int(root.find('size')[0].text),
                        int(root.find('size')[1].text),
                        member[0].text,
                        int(member[5][0].text),
                        int(member[5][1].text),
                        int(member[5][2].text),
                        int(member[5][3].text) )
                xml_list.append(value)

    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'xmax', 'ymin', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


if __name__ == "__main__":
    path_train = '/kaggle/input/custom-dataset-new/train' #Your path_data_train
    path_valid = '/kaggle/input/custom-dataset-new/valid' #Your path_data_valid
    path_test = '/kaggle/input/custom-dataset-new/test'   #Your path_data_test
    
    train = xml_to_csv(path_train)
    valid = xml_to_csv(path_valid)
    test = xml_to_csv(path_test)
    
    print('Successfully converted xml to csv.')
