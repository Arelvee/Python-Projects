import pywt

# Create a db4 wavelet object
wavelet = pywt.Wavelet('db4')

# Print the decomposition low-pass and high-pass filter coefficients
print("Decomposition low-pass filter:", wavelet.dec_lo)
print("Decomposition high-pass filter:", wavelet.dec_hi)

# Print the reconstruction low-pass and high-pass filter coefficients
print("Reconstruction low-pass filter:", wavelet.rec_lo)
print("Reconstruction high-pass filter:", wavelet.rec_hi)