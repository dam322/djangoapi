# -*- coding: utf-8 -*-
"""ContentBased.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16jg4qlAgXFq1B9-tE4wGt65y1pxnhe5s
"""
from datetime import datetime
import json
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# response = requests.request("POST", url_igdb, headers=headers, data=payload)


# json_response = response.json()

class ContentBased:
    def __init__(self, json_response):
        self.json_response = json_response
        self.data = pd.DataFrame(self.json_response)
        self.X = np.array(self.data.summary)
        self.things()
        self.cos_sim_data = pd.DataFrame(cosine_similarity(self.X))

    def things(self):
        # self.data.columns
        self.data = self.data[['genres', 'summary', 'name']]
        self.data = self.data.dropna()
        text_data = self.X
        model = SentenceTransformer('distilbert-base-nli-mean-tokens')
        embeddings = model.encode(text_data)
        embed_data = embeddings
        self.X = np.array(embed_data)

    def give_recommendations(self, index, print_recommendation=False, print_recommendation_plots=False,
                             print_genres=False):
        """ Give recommendations for a game given its index in the data """
        index_recomm = self.cos_sim_data.loc[index].sort_values(ascending=False).index.tolist()[1:6]
        movies_recomm = self.data['name'].loc[index_recomm].values
        result = {'Games': movies_recomm, 'Index': index_recomm}
        if print_recommendation:
            print('The chosen game is this one: %s \n' % (self.data['name'].loc[index]))
            k = 1
            for movie in movies_recomm:
                print(f'The number {k} recommended game is this one: {movie} \n ')
                k += 1
        if print_recommendation_plots:
            print('The plot of the played game is this one:\n %s \n' % (self.data['summary'].loc[index]))
            k = 1
            for q in range(len(movies_recomm)):
                plot_q = self.data['summary'].loc[index_recomm[q]]
                print('The plot of the number %i recommended game is this one:\n %s \n' % (k, plot_q))
                k = k + 1
        if print_genres:
            genres_played = self.data['genres'].loc[index]
            print(f'The genres of the played game are as follows:\n {genres_played} \n')
            k = 1
            for q in range(len(movies_recomm)):
                plot_q = self.data['genres'].loc[index_recomm[q]]
                print(f'The genres of the number {k} recommended game are as follows:\n {plot_q} \n')
                k = k + 1
        return result

    def send_recommendations(self, input_user=None):
        if input_user is None:
            input_user = [65, 12, 41, 59, 58]
        recomm_list_final = []
        names = self.data['name'].loc[input_user].values
        # print(names)
        for index in input_user:
            recomm_i = self.give_recommendations(index)
            recomm_list_final.append(recomm_i['Games'])
        recomm_data = pd.DataFrame(recomm_list_final,
                                   columns=['First Recommendation', 'Second Recommendation', 'Third Recommendation',
                                            'Fourth Recommendation', 'Fifth Recommendation'])
        recomm_data['Selected Game'] = names
        recomm_data = recomm_data[
            ['Selected Game', 'First Recommendation', 'Second Recommendation', 'Third Recommendation',
             'Fourth Recommendation', 'Fifth Recommendation']]
        # print(recomm_data.sample(frac=1).head())
        return recomm_data['First Recommendation'].tolist()