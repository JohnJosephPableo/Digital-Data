import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def nrz_l(data):
    signal = np.zeros(len(data) * 2)
    for i, bit in enumerate(data):
        signal[i * 2] = bit
        signal[i * 2 + 1] = bit
    return signal

def nrz_i(data):
    signal = np.zeros(len(data) * 2)
    prev_bit = 1
    for i, bit in enumerate(data):
        if bit == 0:
            signal[i * 2] = prev_bit
            signal[i * 2 + 1] = prev_bit
        else:
            signal[i * 2] = 1 - prev_bit
            signal[i * 2 + 1] = 1 - prev_bit
            prev_bit = 1 - prev_bit
    return signal

def bipolar(data):
    size = len(data)
    signal = np.zeros(size * 2)
    next_bit = 0
    one_bit = 1
    prev_signal = 0
    for i, bit in enumerate(data):

        if i < size - 1:
            next_bit = data[i + 1]
        else:
            next_bit = 0
        
        if bit == 0:
            if i == 0:
                one_bit = 0
            signal[i * 2] = 0
            if next_bit == 0: 
                signal[i * 2 + 1] = 0
            else: 
                if one_bit == 1: 
                    signal[i * 2 + 1] = -1
                    one_bit = 0
                else:
                    signal[i * 2 + 1] = 1
                    one_bit = 1
                prev_signal = signal[i * 2 + 1]
        else:
            if i == 0:
                prev_signal = 1
            signal[i * 2] = prev_signal
            if next_bit == 0:
                signal[i * 2 + 1] = 0
            else:
                if one_bit == 1:
                     signal[i * 2 + 1] = -1
                     one_bit = 0
                else:
                    signal[i * 2 + 1] = 1
                    one_bit = 1
            prev_signal = signal[i * 2 + 1]

    return signal

def pseudo(data):
    signal = np.zeros(len(data) * 2)
    prev_bit = 1
    for i, bit in enumerate(data):
        if i < len(data) - 1:
            next_bit = data[i + 1]
        else:
            next_bit = 0 
        if bit == 0:
            if prev_bit == 1:
                signal[i * 2] = 1
                signal[i * 2 + 1] = -1
            else:
                signal[i * 2] = -1
                signal[i * 2 + 1] = 1
        else:
            signal[i * 2] = 0
            signal[i * 2 + 1] = 0
    return

def manchester(data):
    return

def diff_man(data):
    return

def main():
    st.title("Digital Data")

    data = st.text_input("Enter the digital data (0s and 1s):", "01110111")

    mode = st.radio(
        "Select an encoding technique",
        ["NRZ-L", "NRZ-I", "Bipolar AMI", "Pseudoternary", "Manchester", "Differential Manchester"],
    )

    data = [int(bit) for bit in data]

    if mode == "NRZ-L":
        signal = nrz_l(data)
    elif mode == "NRZ-I":
        signal = nrz_i(data)
    elif mode == "Bipolar AMI":
        signal = bipolar(data)
    elif mode == "Pseudoternary":
        signal = pseudo(data)
    elif mode == "Manchester":
        signal = manchester(data)
    elif mode == "Differential Manchester":
        signal = diff_man(data)

    # Add other encoding techniques here

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.step(np.arange(len(signal)), signal, where='post')
    ax.set_xticks(np.arange(0, len(signal), 2))
    ax.set_xticklabels(data)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['0', '1'])
    ax.set_title(mode)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
