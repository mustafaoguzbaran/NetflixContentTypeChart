import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataNetflix = pd.read_csv("netflix_titles.csv")
countReleaseYear = dataNetflix.release_year.unique()
countReleaseYear.sort()
print(np.array(countReleaseYear))
print("Minimum Release Year: ",min(countReleaseYear))
contentType = dataNetflix.type
tvShowCount = contentType == "TV Show"
movieCount = contentType == "Movie"
print("TV Show: ",sum(tvShowCount))
print("Movie: ",sum(movieCount))
plotTvShow = dataNetflix[dataNetflix == "Movie"]
plotMovie = dataNetflix[dataNetflix == "TV Show"]
plt.hist(contentType, color="Red", label = "Types - Count")
plt.legend()
plt.show()
