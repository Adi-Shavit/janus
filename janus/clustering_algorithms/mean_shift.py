import pandas as pd
import numpy as np
from sklearn.cluster import MeanShift as MeanShiftModel

from janus.clustering_algorithms.clustering_base import ClusteringBase


class MeanShift(ClusteringBase):
    def __init__(self, data_set: pd.DataFrame, bandwidth=None, **kwargs):
        self.data_set = data_set
        self.model = MeanShiftModel(bandwidth=bandwidth, **kwargs)

    def fit(self):
        self.model.fit(self.data_set)

    @property
    def clusters(self):
        prediction = self.model.fit_predict(self.data_set)
        return np.unique(prediction)
