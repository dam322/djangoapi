import json
import pandas as pd


def recommend_games(json_response):
    """ This function returns a list of games recommended to the user based on the games he has played before. """
    # url = f"https://api.rawg.io/api/games?key=e7e0be95eb69479f9a6949c88dc5b0fa&genres=action&exclude_additions=true
    # &metacritic=80,100&ordering=-rating&page_size=100&dates=2018-01-01,2023-02-17"

    # response = requests.request("GET", url)
    # json_response = response.json()
    games_df = pd.DataFrame(json_response['results'])
    # games_df.head()
    user_input = json_response['user_input']

    games_with_genres = games_df.copy()
    for index, row in games_df.iterrows():
        for genre in row['genres']:
            games_with_genres.at[index, genre['name']] = 1
    games_with_genres = games_with_genres.fillna(0)
    games_with_genres = games_with_genres.drop('stores', axis=1).drop('reviews_count', axis=1).drop('platforms',
                                                                                                    axis=1).drop(
        'background_image', axis=1).drop('ratings', axis=1).drop('slug', axis=1).drop('added', axis=1).drop(
        'saturated_color', axis=1).drop('rating_top', axis=1).drop('user_game', axis=1).drop('short_screenshots',
                                                                                             axis=1).drop(
        'dominant_color', axis=1).drop('updated', axis=1).drop('reviews_text_count', axis=1).drop('esrb_rating',
                                                                                                  axis=1).drop(
        'released', axis=1).drop('tba', axis=1).drop('added_by_status', axis=1).drop('ratings_count', axis=1).drop(
        'suggestions_count', axis=1).drop('tags', axis=1).drop('playtime', axis=1).drop('score', axis=1).drop('clip',
                                                                                                              axis=1).drop(
        'parent_platforms', axis=1)
    # games_with_genres

    input_games = pd.DataFrame(user_input)
    # input_games

    input_id = games_df[games_df['name'].isin(input_games['name'].tolist())]
    input_games = pd.merge(input_id, input_games)
    input_games = input_games.drop('stores', axis=1).drop('reviews_count', axis=1).drop('platforms', axis=1).drop(
        'background_image', axis=1).drop('ratings', axis=1).drop('slug', axis=1).drop('added', axis=1).drop(
        'saturated_color', axis=1).drop('rating_top', axis=1).drop('user_game', axis=1).drop('short_screenshots',
                                                                                             axis=1).drop(
        'dominant_color', axis=1).drop('updated', axis=1).drop('reviews_text_count', axis=1).drop('esrb_rating',
                                                                                                  axis=1).drop(
        'released', axis=1).drop('tba', axis=1).drop('added_by_status', axis=1).drop('ratings_count', axis=1).drop(
        'suggestions_count', axis=1).drop('tags', axis=1).drop('playtime', axis=1).drop('score', axis=1).drop('clip',
                                                                                                              axis=1).drop(
        'parent_platforms', axis=1)
    input_games.head()

    userGames = games_with_genres[games_with_genres['id'].isin(input_games['id'].tolist())]

    userGames = userGames.reset_index(drop=True)
    userGenreTable = userGames.drop('id', axis=1).drop('name', axis=1).drop('rating', axis=1).drop('metacritic',
                                                                                                   axis=1).drop(
        'genres', axis=1)

    userProfile = userGenreTable.transpose().dot(input_games['rating_user'])
    # userProfile

    genreTable = games_with_genres.set_index(games_with_genres['id'])
    genreTable = genreTable.drop('id', axis=1).drop('name', axis=1).drop('rating', axis=1).drop('metacritic',
                                                                                                axis=1).drop('genres',
                                                                                                             axis=1)
    # genreTable.head()

    # genreTable.shape

    recommendation_table_df = ((genreTable * userProfile).sum(axis=1)) / (userProfile.sum())
    recommendation_table_df.head()

    recommendation_table_df = recommendation_table_df.sort_values(ascending=False)
    recommendation_table_df = recommendation_table_df.drop(userGames['id'].tolist(), axis=0)
    recommendation_table_df.head()

    final_recommendation = games_df.loc[games_df['id'].isin(recommendation_table_df.head(5).keys())]
    final_recommendation = final_recommendation.drop('stores', axis=1).drop('reviews_count', axis=1).drop('platforms',
                                                                                                          axis=1).drop('ratings', axis=1).drop('slug', axis=1).drop('added', axis=1).drop(
        'saturated_color', axis=1).drop('rating_top', axis=1).drop('user_game', axis=1).drop('short_screenshots',
                                                                                             axis=1).drop(
        'dominant_color', axis=1).drop('updated', axis=1).drop('reviews_text_count', axis=1).drop('esrb_rating',
                                                                                                  axis=1).drop(
        'released', axis=1).drop('tba', axis=1).drop('added_by_status', axis=1).drop('ratings_count', axis=1).drop(
        'suggestions_count', axis=1).drop('tags', axis=1).drop('playtime', axis=1).drop('score', axis=1).drop('clip',
                                                                                                              axis=1).drop(
        'parent_platforms', axis=1)
    result = final_recommendation.to_json(orient="records")
    parsed = json.loads(result)
    return parsed