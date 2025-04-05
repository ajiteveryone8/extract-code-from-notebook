import json

def extract_code_from_notebook(notebook_path, output_path=None):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    code_lines = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            for line in cell['source']:
                # Ensure line ends with '\n'
                if not line.endswith('\n'):
                    line += '\n'
                code_lines.append(line)

    # Optionally save to a .py file
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(code_lines)
    else:
        for line in code_lines:
            print(line, end='')



# Example usage
extract_code_from_notebook(r"pathToFile\Main.ipynb", 'output_code.py')
