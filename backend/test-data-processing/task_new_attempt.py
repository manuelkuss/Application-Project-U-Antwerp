import csv
import os

import pandas as pd
from pyteomics import mgf, mztab
import matplotlib.pyplot as plt
import spectrum_utils.plot as sup
import spectrum_utils.spectrum as sus

def parse_mgf_to_dataframe(mgf_file):
    """
    Parses an MGF file and returns a pandas DataFrame.
    """
    spectra = []
    for spectrum in mgf.read(mgf_file):
        spectra.append({
            'title': spectrum['params'].get('title'),
            'pepmass': spectrum['params'].get('pepmass'),
            'charge': spectrum['params'].get('charge'),
            'scans': spectrum['params'].get('scans'),
            'rtinseconds': spectrum['params'].get('rtinseconds'),
            'seq': spectrum['params'].get('seq'),
            'm/z array': spectrum.get('m/z array'),
            'intensity array': spectrum.get('intensity array'),
            'charge array': spectrum.get('charge array')
        })
    return pd.DataFrame(spectra)

def parse_mztab_to_dataframe(mztab_file):
    psm_df = pd.read_csv(mztab_file, sep='\t', skiprows=65)
    return psm_df
    # mztab_data = mztab.MzTab(mztab_file)
    # psm_df = mztab_data.psm_data
    # return psm_df

def data_processing_for_coding_task(mgf_file_path, mztab_file_path):

    mgf_df = parse_mgf_to_dataframe(mgf_file_path)
    mztab_df = parse_mztab_to_dataframe(mztab_file_path)

    mztab_df['scan_number'] = mztab_df['spectra_ref'].str.extract('index=(\d+)')
    mgf_df['scan_number'] = mgf_df['title']

    # merge
    merged_df = pd.merge(mztab_df, mgf_df, on='scan_number', how='inner')

    csv_file = 'sequence_metadata.csv'
    metadata_fieldnames = ['id', 'title', 'sequence']

    with open(csv_file, mode='w', newline='') as f:
        writer = csv.DictWriter(f, metadata_fieldnames)
        writer.writeheader()

    for i, row in merged_df.iterrows():
        pepmass = row['pepmass']
        precursor_mz = pepmass[0] if isinstance(row['pepmass'], (list, tuple)) else pepmass
        charge = row["charge_x"]
        precursor_charge = charge

        spectrum = sus.MsmsSpectrum(
            identifier=row['title'],
            precursor_mz=pepmass[0] if isinstance(row['pepmass'], (list, tuple)) else pepmass,
            precursor_charge=precursor_charge,
            mz=row["m/z array"],
            intensity=row["intensity array"],
        )
        spectrum = spectrum.annotate_proforma(row['sequence'], 10, "ppm")

        file_path = "../media/output_plots/sequence_" + row['title'] + ".png"

        fig, ax = plt.subplots(figsize=(12, 6))
        sup.spectrum(spectrum, grid=False, ax=ax)
        ax.set_title(row['sequence'], fontdict={"fontsize": "xx-large"})
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)
        plt.savefig(file_path, dpi=300, bbox_inches="tight", transparent=True)
        plt.close()

        new_data = {
            'id': row['title'],
            'title': row['title'],
            'sequence': row['sequence']
        }

        with open(csv_file, mode='a', newline='') as f:
            writer = csv.DictWriter(f, metadata_fieldnames)
            writer.writerow(new_data)
            print(f"Added sequence with id {new_data['id']}")

        if i == 10:
            break

data_processing_for_coding_task(mgf_file_path = "../../resources/sample_preprocessed_spectra.mgf", mztab_file_path = "../../resources/casanovo_20251029091517.mztab")


