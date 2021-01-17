# %%[markdown]
"""
# Move Sample Images
- We would like to move the images that we have sampled and saved in the csv file `styles_sample.csv` to different folders for each of the following categories:
    - by `Topwear`, `Shoes`, `Bottomwear`, `Headwear`
    - further categorized by `Men` & `Women`
"""
# %%
import pandas as pd
import os
import shutil

# %%
df = pd.read_csv(
    os.path.join("dataset", "database", "item_catalogue_sample.csv",),
    index_col="id",
    dtype={
        "gender": "category",
        "masterCategory": "category",
        "subCategory": "category",
        "articleType": "category",
        "baseColour": "category",
        "season": "category",
        "productDisplayName": "category",
    },
).sort_index(ascending=True,)

df.info()

# %%

for ind, row in df.iterrows():
    source = os.path.join("dataset", "images", f"{ind}.jpg",)
    gender = row["gender"]
    sub_catergory = row["subCategory"]
    destination = os.path.join(
        "dataset", "database", "item_catalogue_image_sample", sub_catergory, gender,
    )

    if not os.path.isdir(destination):
        os.makedirs(destination)

    shutil.copy(source, destination)

# %%
