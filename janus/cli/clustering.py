from pprint import pprint

from click import option, command
from sklearn.datasets import make_classification, make_multilabel_classification

SAMPLE_DATA, LABEL = make_multilabel_classification(n_samples=10, n_features=5, random_state=4)


def draw_data():
    pass


@command("cluster-data")
def cluster_data():
    pprint(SAMPLE_DATA)
    pprint(LABEL)


if __name__ == "__main__":
    cluster_data()
