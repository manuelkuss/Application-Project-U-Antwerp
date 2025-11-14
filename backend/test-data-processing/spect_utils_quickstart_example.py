import matplotlib.pyplot as plt
import spectrum_utils.plot as sup
import spectrum_utils.spectrum as sus


# Retrieve the spectrum by its USI.
usi = "mzspec:PXD004732:01650b_BC2-TUM_first_pool_53_01_01-3xHCD-1h-R2:scan:41840"
peptide = "WNQLQAFWGTGK"

# Changed this line:
# spectrum = sus.MsmsSpectrum.from_usi(usi)
spectrum = sus.MsmsSpectrum.from_usi(
    usi,
    precursor_mz=767.9739,
    precursor_charge=2
)

# Process the spectrum.
fragment_tol_mass, fragment_tol_mode = 10, "ppm"
spectrum = (
    spectrum.set_mz_range(min_mz=100, max_mz=1400)
    .remove_precursor_peak(fragment_tol_mass, fragment_tol_mode)
    .filter_intensity(min_intensity=0.05, max_num_peaks=50)
    .scale_intensity("root")
    .annotate_proforma(
        peptide, fragment_tol_mass, fragment_tol_mode, ion_types="aby"
    )
)

# Plot the spectrum.
fig, ax = plt.subplots(figsize=(12, 6))
sup.spectrum(spectrum, grid=False, ax=ax)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
plt.savefig("quickstart.png", bbox_inches="tight", dpi=300, transparent=True)
plt.close()

print(spectrum)