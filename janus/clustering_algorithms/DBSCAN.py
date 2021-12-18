import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN as DBSCANModel

from janus.clustering_algorithms.clustering_base import ClusteringBase


class DBSCAN(ClusteringBase):
    def __init__(self, data_set: pd.DataFrame, eps=0.30, min_samples=9, **kwargs):
        self.data_set = data_set
        self.model = DBSCANModel(eps=eps, min_samples=min_samples, **kwargs)

    def fit(self):
        self.model.fit(self.data_set)

    @property
    def clusters(self):
        prediction = self.model.fit_predict(self.data_set)
        return np.unique(prediction)
