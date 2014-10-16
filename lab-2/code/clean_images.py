import os
import os.path

full_size_path = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/faces/full_size/"
resized_path = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/faces/resized/"

files = [f for f in os.listdir(full_size_path) if os.path.isfile(os.path.join(full_size_path, f))]

print files
