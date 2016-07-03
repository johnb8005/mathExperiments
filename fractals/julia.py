"""
  Generate a Julia Set image
"""
 
import numpy
 
# Specify image width and height
w, h = 1900, 1297
 
# Specify real and imaginary range of image
re_min, re_max = -2.0, 2.0
im_min, im_max = -2.0, 2.0
 
# Pick a value for c
c = complex(0.285,0.01) #complex(0.0,0.71)
 
# Generate evenly spaced values over real and imaginary ranges
real_range = numpy.arange(re_min, re_max, (re_max - re_min) / w)
imag_range = numpy.arange(im_max, im_min, (im_min - im_max) / h)
 
# Open output file and write PGM header info
fout = open('julia.bmp', 'w')
fout.write('P2\n# Julia Set image\n' + str(w) + ' ' + str(h) + '\n255\n')
 
# Generate pixel values and write to file
for im in imag_range:
    for re in real_range:
        z = complex(re, im)
        n = 0
        while abs(z) < 10 and n <= 255:
            z = z*z + c
            n += 1
        # Write pixel to file
        fout.write(str(n) + ' ')
    # End of row
    fout.write('\n')
 
# Close file
fout.close()