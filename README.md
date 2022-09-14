Run code follow the file sequence:
`prepare_data` -> `clustering` -> `train_test_split` -> `collaborative filtering`

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
|   |   |   collaborative filtering.ipynb
|   |   |   train_test_split.ipynb
|   |   |   plot.ipynb
|   |   |   prepare_data.ipynb
|   |
|   |   
|___processing_data.py
|   README.md
```

- `cluster_first`: Phân cụm trước rồi mới chia train test
- `split_first`: Chia train test rồi mới phân cụm
- `processing_data.py`: File này nhận một đường dẫn đến file excel và trả về file csv đã xử lý.
- `prepare_data.ipynb`: File này xử lý dữ liệu RFM từ file csv đã xử lý.
- `clustering.ipynb`: File này phân cụm dữ liệu từ dữ liệu RFM trên.
- `train_test_split.ipynb`: Chia train test sau khi phân cụm.
- `collaborative filtering.ipynb`: File này làm lọc cộng tác từ dữ liệu đã xử lý ở trên.



## Test
- Train cluster 0,1: New + Inactive - Test cluster 2: Loyalty
- Đưa data vào notebook, xong nó ra:
    - giá trị f1_score
    - Xuất ra những sản phẩm recommend
- So sánh với CF data gốc


Model 3 (Traditional model- non-weighted)
|___data
|   |   DataFile.xlsx
|   |   filtered_data.csv
|   |   rfm_data.csv
|   |   rfm_weight.csv
|
|___notebooks
|   |___split_first
|   |   |   clustering.ipynb
|   |   |   collaborative filtering.ipynb
|   |   |   plot.ipynb
|   |   |   prepare_data.ipynb
|   |
|   |   
|___processing_data.py
|   README.md