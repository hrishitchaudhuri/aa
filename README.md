# life-is-a-pain
Advanced Algorithms assignment


### Problem Definition
- [ ] Implement a 1-D Discrete Fourier Transform on the coefficient vectors of two polynomials, A and B, by multiplication of the Vandermonde matrix.  
- [ ] Implement a 1-D Fast Fourier Transform on the same vectors, and ensure the two FTs produce the same result.  
- [ ] Pointwise multiply the results to get the PVR of the product polynomial C.  
- [ ] RSA encrypt (128, 256 and 512-bit) the points with public key, and decrypt with a private key.  
- [ ] Implement a 1-D inverse FFT to interpolate the coefficient vector of C.  
- [ ] Verify the correctness of C by comparing with the coefficients generated by convoluting the coefficient vectors of A and B
- [ ] Implement a 2-D FFT and I-FFT using the 1-D FFT and I-FFT
- [ ] Verify the 2-D transforms on a randomly generated grayscale matrix (matrix values are from 0-255)
- [ ] Apply the 2-D FFT on a TIFF/JPG grayscale image and drop Fourier coefficients below some specified magnitude. Save these in a new file. 
- [ ] Apply 2-D IFFT on the quantized grayscale image and render it. Observe image quality. 


### Dataset Generation
- [ ] For 1-D transforms, randomly generate coefficient vectors of varying degree bounds (n = 4, 8, 16, ...., 1024, 2048)
- [ ] For the 2-D grayscale image, use randomly generated pixel values
- [ ] For testing on an actual image, use a grayscale TIFF or lossless JPG and use the OpenCV API to access raw pixel data
- [ ] To compare efficiency of the transforms, compare with built-in numpy functions. 
