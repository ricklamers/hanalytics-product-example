# Hanalytics product example

This project contains two pipelines to showcase how to separate training from prediction in Orchest.

Based on fake generated product event data we fit a KMeans model to identify the cluster of high seller products.

The data is generated in `load_product_data.ipynb`.

The model is trained in `train_model.ipynb`.

A simple feature vector is generated from the product event data in the `utils.py` file by the `compute_event_df` function. This feature generation function is re-used for training and prediction. Assuming that we have access to low level event data.

### Train pipeline
![Train pipeline](https://pviz.orchest.io/?pipeline=https://github.com/ricklamers/hanalytics-product-example/blob/master/train.orchest)

### Predict pipeline
![Predict pipeline](https://pviz.orchest.io/?pipeline=https://github.com/ricklamers/hanalytics-product-example/blob/master/predict.orchest)