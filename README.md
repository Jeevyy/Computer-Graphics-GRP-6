# Computer-Graphics: ICS 3C - Group 6 CAT 1
## About

This Python3 development project establishes an environment for data processing and file manipulation. It structures a PyCharm project, imports a massive dataset, and accomplishes three main tasks. It creates language-specific files and a comprehensive translation dataset ensurimg clean file management with GitHub integration.

## Tasks
1.  Build a Python3 project with the structure of projects in PyCharm then import the MASSIVE Dataset mentioned on the Data File above. 
    In this dataset, the pivot language is English, given that all the ids of the languages are matching, generate a en-xx.xlxs file for all the languages. In this question     use the id, utt and the annot_utt.

2.  For English (en), Swahili (sw) and German (de), generate separate jsonl files with test, train and dev respectively.
3.  Generate one large json file showing all the translations from en to xx with id and utt for all the train sets. 
    Pretty print your json file structure.

## Python Files

- `functions.py`: Contains functions to answer the queations for generating files from Excel to Jsonl.
- `main.py`: The main program file that loads, processes, and analyzes student data.

## Data Produced

- `Excel_Files`: The output excel files thats contains id's of all langauges.
- `JSONL_Files`: The jsonl files that contain the pretty printed jsonl formatted for each language.
- `JSONL_Output`: Contains DE, SW and EN jsonl files.
- `translations.json`: Large json file showing all the translations from en to xx with id and utt for all the train sets.

## Usage
### In order to run the dependencies needed, please do the following:

1. Run Dependencies Installation: Execute the `dependencies.sh` bash script to automatically install all project dependencies and libraries. Simply run bash `dependencies.sh` in your terminal.
2. Activate the Virtual Environment: Activate the Python virtual environment with source `venv/bin/activate` to work within an isolated environment for this project.
3. Run the Main Script: Use the command python `main.py` to execute the project's main Python script, which performs various data processing tasks.
4. Check Output: After running the script, find the generated files in the project directory, including Excel, JSON, and CSV files, depending on the tasks completed.

## Dependencies
- `os`
- `json`
- `pandas`
- `shutil`
- `googleapi`
- `zipfile`
  
## Authors

1. 146254 Singh Sehmi
2. 145835 Humphrey Dulo
3. 144914 Vasani Aman
4. 145351 Kihanya Mungai

## License

This project currently does not contain any licenses. 

