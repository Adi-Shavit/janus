from abc import ABC, abstractmethod


class ClusteringBase(ABC):

    @abstractmethod
    def fit(self):
        pass

    @property
    @abstractmethod
    def clusters(self):
        pass
