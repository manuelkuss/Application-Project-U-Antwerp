import json
import spectrum_utils.spectrum as sus
from django.shortcuts import render
from pyteomics import mgf
import csv
import os
import pandas as pd
from pyteomics import mgf, mztab

import matplotlib.pyplot as plt
import spectrum_utils.iplot as sup

# change to
# import spectrum_utils.iplot as sup
import spectrum_utils.spectrum as sus

def read_mgf_file_and_return_first_n_spectra(mgf_file_path, n: int):

    spectra = []
    with mgf.read(mgf_file_path) as reader:
        for i, spec in enumerate(reader, start=1):
            mz = spec["m/z array"]  # numpy array of fragment m/z
            inten = spec["intensity array"]  # numpy array of fragment intensities
            meta = spec["params"]  # dict of spectrum-level metadata

            title = meta.get("title")
            pepmass = meta.get("pepmass")  # (precursor_mz, intensity?) or float
            charge = meta.get("charge")
            rt = meta.get("rtinseconds")

            su_spec = sus.MsmsSpectrum(
                identifier=title,
                precursor_mz=spec["params"]["pepmass"][0],
                precursor_charge=spec["params"].get("charge", [None])[0],
                mz=spec["m/z array"],
                intensity=spec["intensity array"],
            )

            spectra.append({"spectrum": su_spec})

    # spectra_df = pd.DataFrame(spectra)
    response_spectra = []
    for i in range(n):
        s = spectra[i]["spectrum"]
        response_spectra.append({
            "title": "chart_" + str(i),
            "mz": s.mz.tolist(),
            "intensity": s.intensity.tolist()
        })

    chartData = response_spectra

    return chartData


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



def get_plotly_data_for_sequence(mgf_file_path, mztab_file_path, id: int):

    mgf_df = parse_mgf_to_dataframe(mgf_file_path)
    mztab_df = parse_mztab_to_dataframe(mztab_file_path)

    mztab_df['scan_number'] = mztab_df['spectra_ref'].str.extract('index=(\d+)')
    mgf_df['scan_number'] = mgf_df['title']

    # merge
    merged_df = pd.merge(mztab_df, mgf_df, on='scan_number', how='inner')

    # row = merged_df[merged_df['title'] == str(id)]
    # print(row)

    # annotate
    # spectrum = spectrum.annotate_proforma(row['sequence'], 10, "ppm")

    for i, row in merged_df.iterrows():
        if row['title'] == str(id):
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

            # annotate
            spectrum = spectrum.annotate_proforma(row['sequence'], 10, "ppm")

            # change to:
            chart = sup.spectrum(spectrum)
            chart.properties(width=640, height=400).save("iplot_spectrum.json")



            # mz_value = spectrum.mz[ann.peak_index]
            # intensity_value = spectrum.intensity[ann.peak_index]
            # label = str(ann.interpretation)  # readable fragment label

            # annotations_list = []
            # for ann in spectrum.annotation:
            #     annotations_list.append ({
            #         "mz": float(spectrum.mz[ann.peak_index]),
            #         "intensity": float(spectrum.intensity[ann.peak_index]),
            #         "label": str(ann.interpretation)
            #     })



            # fig, ax = plt.subplots(figsize=(12, 6))
            # sup.spectrum(spectrum, grid=False, ax=ax)
            # ax.set_title(row['sequence'], fontdict={"fontsize": "xx-large"})
            # ax.spines["right"].set_visible(False)
            # ax.spines["top"].set_visible(False)
            # plt.close()
            #
            # return {
            #     "id": row["title"],
            #     "sequence": row["sequence"],
            #     "mz": spectrum.mz.tolist(),
            #     "intensity": spectrum.intensity.tolist(),
            #     # "annotations": annotations_list
            # }

# print(get_plotly_data_for_sequence(
#         mgf_file_path="../../../resources/sample_preprocessed_spectra.mgf",
#         mztab_file_path="../../../resources/casanovo_20251029091517.mztab",
#         id=3))

def data_processing_for_coding_task(mgf_file_path, mztab_file_path, sequence_metadata_csv_file_path, output_plot_path):

    mgf_df = parse_mgf_to_dataframe(mgf_file_path)
    mztab_df = parse_mztab_to_dataframe(mztab_file_path)

    mztab_df['scan_number'] = mztab_df['spectra_ref'].str.extract('index=(\d+)')
    mgf_df['scan_number'] = mgf_df['title']

    # merge
    merged_df = pd.merge(mztab_df, mgf_df, on='scan_number', how='inner')

    for i, row in merged_df.iterrows():

        # -- generate iplot json file (with spectrum_utils.iplot import)

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

        # annotate
        spectrum = spectrum.annotate_proforma(row['sequence'], 10, "ppm")

        iplot_file_path = output_plot_path + "sequence_" + row['title'] + ".json"

        chart = sup.spectrum(spectrum)
        chart.properties(width=640, height=400).save(iplot_file_path)


        # -- generate plots (with spectrum_utils.plot import)

        # pepmass = row['pepmass']
        # precursor_mz = pepmass[0] if isinstance(row['pepmass'], (list, tuple)) else pepmass
        # charge = row["charge_x"]
        # precursor_charge = charge
        #
        # spectrum = sus.MsmsSpectrum(
        #     identifier=row['title'],
        #     precursor_mz=pepmass[0] if isinstance(row['pepmass'], (list, tuple)) else pepmass,
        #     precursor_charge=precursor_charge,
        #     mz=row["m/z array"],
        #     intensity=row["intensity array"],
        # )
        # spectrum = spectrum.annotate_proforma(row['sequence'], 10, "ppm")
        #
        # file_path = output_plot_path + "sequence_" + row['title'] + ".png"
        #
        # fig, ax = plt.subplots(figsize=(12, 6))
        # sup.spectrum(spectrum, grid=False, ax=ax)
        # ax.set_title(row['sequence'], fontdict={"fontsize": "xx-large"})
        # ax.spines["right"].set_visible(False)
        # ax.spines["top"].set_visible(False)
        # plt.savefig(file_path, dpi=300, bbox_inches="tight", transparent=True)
        # plt.close()
        #


        # -- write metadata to metadata csv file

        row_dict = row.to_dict()
        new_data = {
            'id': row['title'],
            **row_dict
        }

        if not os.path.exists(sequence_metadata_csv_file_path):
            with open(sequence_metadata_csv_file_path, mode='w', newline='') as f:
                writer = csv.DictWriter(f, new_data.keys())
                writer.writeheader()

        with open(sequence_metadata_csv_file_path, mode='a', newline='') as f:
            writer = csv.DictWriter(f, new_data.keys())
            writer.writerow(new_data)
            print(f"Added sequence with id {new_data['id']}")
            # print(f"Added sequence with id {new_data}")

# data_processing_for_coding_task(mgf_file_path="../../../resources/sample_preprocessed_spectra.mgf",
#                                         mztab_file_path="../../../resources/casanovo_20251029091517.mztab",
#                                         sequence_metadata_csv_file_path="../../assets/sample_preprocessed_spectra/sample_preprocessed_spectra_info.csv",
#                                         output_plot_path="../../media/output_iplots/")
