import pandas as pd
import numpy as np
from sklearn.cluster import AffinityPropagation as AffinityPropagationModel

from janus.clustering_algorithms.clustering_base import ClusteringBase


class AffinityPropagation(ClusteringBase):
    def __init__(self, data_set: pd.DataFrame, damping=0.9, **kwargs):
        self.data_set = data_set
        self.model = AffinityPropagationModel(damping=damping, **kwargs)

    def fit(self):
        self.model.fit(self.data_set)

    @property
    def clusters(self):
        prediction = self.model.predict(self.data_set)
        return np.unique(prediction)
