# piecewise-cdf-sampler
Sample from a linearly piecewise CDF, represented by its (x,y) coordinates

Useful for resampling data from CDF images where source data is not recoverable.

Input:

`[piecewise-data]`: A file containing x/y coordinates representing a monotonically increasing function where `0<=y<=1` (piecewise CDF); 
1 coordinate pair per line, x/y coordinates delimited by spaces.
`[num]`: How many numbers to sample

Output:
`num` samples from the input CDF file
