import os
import shutil
import pandas as pd
import json


def copy_jsonl_files(source_dir, destination_dir):
    for filename in os.listdir(source_dir):
        if filename.endswith('.jsonl'):
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination_dir, filename)
            shutil.copy2(source_file, destination_file)
    print(f"JSONL files copied to '{destination_dir}' within the project.")


def create_excel_files(jsonl_dir, output_dir):
    language_dfs = {}
    for filename in os.listdir(jsonl_dir):
        if filename.endswith('.jsonl'):
            file_path = os.path.join(jsonl_dir, filename)
            lang_code = os.path.splitext(filename)[0]

            json_objects = []
            with open(file_path, 'r', encoding='utf-8') as jsonl_file:
                for line in jsonl_file:
                    json_data = json.loads(line)
                    json_objects.append(json_data)

            df = pd.DataFrame(json_objects)
            language_dfs[lang_code] = df

    for lang_code, df in language_dfs.items():
        output_file = os.path.join(output_dir, f'en-{lang_code}.xlsx')
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=lang_code, index=False)


def process_excel_files(excel_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    language_files = {
        'en': 'en-en-US.xlsx',
        'sw': 'en-sw-KE.xlsx',
        'de': 'en-de-DE.xlsx'
    }

    for lang, excel_file in language_files.items():
        file_path = os.path.join(excel_dir, excel_file)
        df = pd.read_excel(file_path)
        split_and_save_data(df, lang, output_dir)


def split_and_save_data(data, lang, output_dir):
    splits = ['train', 'dev', 'test']
    for split in splits:
        if split == 'train':
            split_df = data.sample(frac=0.8, random_state=42)
        elif split == 'dev':
            split_df = data.sample(frac=0.1, random_state=42)
        elif split == 'test':
            split_df = data.sample(frac=0.1, random_state=42)
        else:
            continue

        if not split_df.empty:
            output_file = os.path.join(output_dir, f'{lang}-{split}.jsonl')
            split_df[['id', 'utt', 'annot_utt']].to_json(output_file, orient='records', lines=True, force_ascii=False,
                                                         date_format='iso')


def generate_translations_json(jsonl_dir, output_file):
    translations = {}
    languages = ['en', 'sw', 'de']

    for lang in languages:
        file_path = os.path.join(jsonl_dir, f'{lang}-train.jsonl')
        translations[lang] = []

        with open(file_path, 'r', encoding='utf-8') as jsonl_file:
            for line in jsonl_file:
                data = json.loads(line)
                translations[lang].append({
                    'id': data['id'],
                    'utt': data['utt']
                })

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(translations, json_file, indent=4, ensure_ascii=False)
