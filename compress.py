import image

FILE_PATH='images/chess/chess_grayscale'
SUFFIX='jpg'

FILE_NAME=FILE_PATH+'.'+SUFFIX

for keep in [0.1, 0.05, 0.01]:
    wr_filename_1 = FILE_PATH + '_numpy_' + str(keep * 100) + '.' + SUFFIX
    wr_filename_2 = FILE_PATH + '_painpy_' + str(keep * 100) + '.' + SUFFIX

    image.numpy_compress_image(FILE_NAME, wr_filename_1, keep)
    image.painpy_compress_image(FILE_NAME, wr_filename_2, keep)