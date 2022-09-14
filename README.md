Run code follow the file sequence:
`prepare_data` -> `clustering` -> `plot'

## Cấu trúc file:
```
project
|___data
|   |   DataFile.xlsx
|   |   filtered_data.csv
|   |   rfm_data.csv
|   |   rfm_weight.csv --- import from RFM WEIGHTING for Clustering (A).xlsx
|   |   weight_matrix.csv --- import from RFM WEIGHTING for kNN CF recommender system (B).xlsx
|
|___notebooks
|   |___cluster_first
|   |   |   clustering.ipynb
|   |   |   
|   |   | 
|   |   |   plot.ipynb
|   |   |   prepare_data.ipynb
|   |
|   |   
|___processing_data.py
|   README.md
```
