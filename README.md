# Jupyter Notebook Python Code Extractor

This tool extracts all Python code from the code cells of a Jupyter Notebook (`.ipynb`) file and saves it into a `.py` file with proper formatting and line breaks.

## Features

- Extracts code from all code cells in a Jupyter notebook
- Ensures each line ends with a newline character (`\n`)
- Outputs to a clean `.py` file

## Requirements

- Python 3.x

## Clone the Repository

```bash
git clone https://github.com/ajiteveryone8/extract-code-from-notebook
cd jupyter-code-extractor
```

## Usage

Run the script using Python:

```bash
python extract_code.py <input_notebook.ipynb> <output_file.py>
```

### Example

```bash
python extract_code.py my_notebook.ipynb output_code.py
```

This command will extract all Python code from `my_notebook.ipynb` and save it to `output_code.py`.

## Notes

- If the output file is not provided, the code will be printed directly to the terminal.

## License

This project is open-source and free to use.
