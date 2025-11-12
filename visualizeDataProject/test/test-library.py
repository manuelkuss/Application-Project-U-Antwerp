

import matplotlib.pyplot as plt
import spectrum_utils.plot as sup
import spectrum_utils.spectrum as sus


# Retrieve the spectrum by its USI.
usi = "mzspec:MSV000082283:f07074:scan:5475"
spectrum = sus.MsmsSpectrum.from_usi(usi)

# Annotate the spectrum with its ProForma string.
peptide = "EM[Oxidation]EVEES[Phospho]PEK"
spectrum = spectrum.annotate_proforma(peptide, 10, "ppm")

# Plot the spectrum.
fig, ax = plt.subplots(figsize=(12, 6))
sup.spectrum(spectrum, grid=False, ax=ax)
ax.set_title(peptide, fontdict={"fontsize": "xx-large"})
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
plt.savefig("proforma_ex1.png", bbox_inches="tight", dpi=300, transparent=True)
plt.close()

