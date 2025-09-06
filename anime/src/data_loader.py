import os
import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        # Load CSV
        df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna()

        # Keep original column names from dataset
        required_cols = {'Name', 'Genres', 'sypnopsis'}

        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError(f"Missing column(s) in CSV file: {missing}. Available: {list(df.columns)}")

        # Create combined column
        df['combined_info'] = (
            "Title: " + df["Name"] +
            " Overview: " + df["sypnopsis"] +
            " Genres: " + df["Genres"]
        )

        # Ensure save directory exists
        os.makedirs(os.path.dirname(self.processed_csv), exist_ok=True)

        # Save processed file
        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv
