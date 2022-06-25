# NCI_heatmap
A python script that sketches a heatmap for NCI (National Cancer Institute) screening results.

These screening results are represented as percent growth of treated cancer cells with the compounds at 10 micromolar concentration.

The screening results are provide by the NCI as csv files.

The csv files contain CELLNAME column with the names of the 60 cell lines and GIPRCNT column with the percent growth of each cell line.

The names of compounds are taken from the names of the csv files, so change the csv files names with your compounds names.

Dependencies: 
matplotlib=3.3.4
numpy=1.20.1
pandas=1.2.4
seaborn=0.11.1

![NCI_heatmap](https://user-images.githubusercontent.com/19835485/175772915-721fca44-c210-49c9-823e-5629fe837ea9.png).

The depicted figure is an output example for the script which is published in my paper (https://pubs.acs.org/doi/10.1021/acsomega.0c01829).

Kindly cite it if you use the script.

Enjoy it!
