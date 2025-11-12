import re

import pandas as pd
from pyteomics import mgf
import matplotlib.pyplot as plt
import spectrum_utils.plot as sup
import spectrum_utils.spectrum as sus

def read_mgf_file_and_return_first_spectrum():
    mgf_file_path = "../../resources/sample_preprocessed_spectra.mgf"

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
    first_spectrum = spectra[0]["spectrum"]
    first_spectrum_data = {
        "mz": first_spectrum.mz,
        "intensity": first_spectrum.intensity
    }

    return first_spectrum_data

read_mgf_file_and_return_first_spectrum()