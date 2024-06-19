import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA


def task5(df, filename1, filename2):
    # Step 1: Bag of Words representation
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['words'])
    feature_names = vectorizer.get_feature_names_out()

    # Step 2: Normalization
    X = normalize(X, norm='max')

    # Step 3: PCA
    pca = PCA(n_components=2, random_state=535)
    X_embedded = pca.fit_transform(X.toarray())

    # Step 4: Plot 1 - Top 10 Positive and Negative Tokens for Each Component
    component_0 = pca.components_[0]
    component_1 = pca.components_[1]
    indices_0 = np.argsort(component_0)
    ......

    fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    axs[0].barh(top_10_positive_0 + top_10_negative_0,
                list(positive_weights_0) + list(negative_weights_0))
    axs[0].set_title("Component 0")
    axs[1].barh(top_10_positive_1 + top_10_negative_1,
                list(positive_weights_1) + list(negative_weights_1))
    axs[1].set_title("Component 1")
    plt.tight_layout()
    plt.savefig(filename1)
    plt.close()

    # Step 5: Plot 2 - Seed URL Representation in 2D
    seed_urls = df['seed_url'].unique()
    labels = np.array([np.where(seed_urls == url)[0][0] for url in df['seed_url']])
    colors = plt.cm.rainbow_r([i / len(seed_urls) for i in range(len(seed_urls))])
    for i, seed_url in enumerate(seed_urls):
        x = X_embedded[labels == i, 0]
        y = X_embedded[labels == i, 1]
        color = colors[i]
        plt.scatter(x, y, color=color, label=seed_url)
    plt.legend()
    plt.savefig(filename2)
    plt.close()

    # Step 6: Return result
    result = {}
    result['0'] = {
        "positive": top_10_positive_0,
        "negative": top_10_negative_0,
        "positive_weights": positive_weights_0.tolist(),
        "negative_weights": negative_weights_0.tolist()
    }
    result['1'] = {
        "positive": top_10_positive_1,
        "negative": top_10_negative_1,
        "positive_weights": positive_weights_1.tolist(),
        "negative_weights": negative_weights_1.tolist()
    }

    # 反转negative中的内容
    result['0']['negative'] = result["0"]['negative'][::-1]
    result['0']['negative_weights'] = result['0']['negative_weights'][::-1]
    result['1']['negative'] = result['1']['negative'][::-1]
    result['1']['negative_weights'] = result['1']['negative_weights'][::-1]

    return result
