"""
Pastas
"""

from pathlib import Path


project_path = Path(__file__).parents[1]


docs_path = project_path / 'docs'
docs_path.mkdir(exist_ok=True)

# Pastas
data_path = project_path / 'data'
data_path.mkdir(exist_ok=True)

input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)

output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)


if __name__ == '__main__':
    print(project_path)
