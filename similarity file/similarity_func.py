def show_similarity(series):
    # Convert both input and the 'name' column to lowercase for case-insensitive comparison
    new_df['name_lower'] = new_df['name'].str.lower() 
    
    if series in new_df['name_lower'].values:
        series_index = new_df[new_df['name_lower'] == series].index[0]
        similarity = similarity_score[series_index]
        five_similar = sorted(list(enumerate(similarity)), reverse=True, key=lambda x: x[1])[1:6]
    else:
        print("No TV show with this name. Try searching for more.")
        return None

    for i in five_similar:
        name = new_df.loc[i[0], 'name']  # Fetch the original name
        print(name)
    
    # drop temporary column
    new_df.drop(columns=['name_lower'], inplace=True)