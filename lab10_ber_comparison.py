import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run_lab10():
    st.header("📊 Laboratoriya 10 – BER tahlili barcha texnologiyalarda")

    st.write("""
    Bu laboratoriyada WDM, OCDMA, PON va ularning gibridlarida BER (Bit Error Rate) ni taqqoslaymiz.
    """)

    technologies = ['WDM', 'OCDMA', 'PON', 'WDM-OCDMA', 'WDM-PON', 'OCDMA-PON', 'WDM-OCDMA-PON']
    ber_values = np.random.uniform(1e-5, 1e-2, len(technologies))  # Tasodifiy BER (lekin kichik)

    fig, ax = plt.subplots()
    ax.bar(technologies, ber_values, color='teal')
    ax.set_ylabel("BER (Bit Error Rate)")
    ax.set_title("Texnologiyalar bo‘yicha BER taqqoslash")
    ax.set_yscale('log')
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    st.pyplot(fig)

    for tech, ber in zip(technologies, ber_values):
        st.write(f"**{tech}** → BER: `{ber:.2e}`")
