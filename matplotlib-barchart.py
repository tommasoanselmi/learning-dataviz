from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd

# plt.xkcd()
plt.style.use('seaborn-dark')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(30):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.xlabel("# of people who use")
plt.title("Most Popular Programming languages")
# plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
