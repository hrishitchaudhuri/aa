# life-is-a-pain
Advanced Algorithms assignment


### Problem Definition
- [x] Implement a 1-D Discrete Fourier Transform on the coefficient vectors of two polynomials, A and B, by multiplication of the Vandermonde matrix. (Hrishit)  
- [x] Implement a 1-D Fast Fourier Transform on the same vectors, and ensure the two FTs produce the same result.  (Gautham)
- [x] Pointwise multiply the results to get the PVR of the product polynomial C.  (Hrishit)
- [x] RSA encrypt (128, 256 and 512-bit) the points with public key, and decrypt with a private key. (Gautham) 
- [x] Implement a 1-D inverse FFT to interpolate the coefficient vector of C.  (Hrishit)
- [x] Verify the correctness of C by comparing with the coefficients generated by convoluting the coefficient vectors of A and B (Gautham)
- [x] Implement a 2-D FFT and I-FFT using the 1-D FFT and I-FFT (Gautham / Hrishit)
- [x] Verify the 2-D transforms on a randomly generated grayscale matrix (matrix values are from 0-255) (TBD)
- [x] Apply the 2-D FFT on a TIFF/JPG grayscale image and drop Fourier coefficients below some specified magnitude. Save these in a new file. (Hrishit) 
- [x] Apply 2-D IFFT on the quantized grayscale image and render it. Observe image quality. (Hrishit)


### Dataset Generation
- [x] For 1-D transforms, randomly generate coefficient vectors of varying degree bounds (n = 4, 8, 16, ...., 1024, 2048) (Gautham)
- [x] For the 2-D grayscale image, use randomly generated pixel values (Hrishit)
- [x] For testing on an actual image, use a grayscale TIFF or lossless JPG and use the OpenCV API to access raw pixel data (Hrishit)
- [x] To compare efficiency of the transforms, compare with built-in numpy functions. (Gautham)
