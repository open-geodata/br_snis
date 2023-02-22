"""
Pastas
"""

from pathlib import Path


project_path = Path(__file__).parents[1]


# Datasets Path
dataset_path = Path(project_path.anchor) / 'Datasets' / project_path.name
dataset_path.mkdir(exist_ok=True)

# Data
data_path = dataset_path / 'data'
data_path.mkdir(exist_ok=True)

# Input
input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)

input_path_temp = input_path / 'temp'
input_path_temp.mkdir(exist_ok=True)

# Output
output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)

# Docs
docs_path = project_path / 'docs'
docs_path.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(project_path)
