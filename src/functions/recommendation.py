import pandas as pd

def recomendar_musicas(input_dict, df_features, df_with_id, model, preprocessor, features, top_n=20):
    """
    Recomenda músicas baseado nas features de entrada
    
    Args:
        input_dict: Dicionário com as features de entrada
        df_features: DataFrame apenas com features (para o modelo)
        df_with_id: DataFrame com features + ID (para retornar ao frontend)
        model: Modelo KNN treinado
        preprocessor: Pipeline de normalização
        features: Lista de features numéricas
        top_n: Número de recomendações (padrão: 20)
    
    Returns:
        DataFrame com as top_n músicas recomendadas + ID + distância
    """
    # Criar DataFrame do input
    input_df = pd.DataFrame([input_dict])[features]
    
    # Normalizar com o preprocessor
    input_scaled = preprocessor.transform(input_df)
    
    # Encontrar vizinhos mais próximos
    distances, indices = model.kneighbors(input_scaled, n_neighbors=top_n)
    
    # Obter resultados do dataframe com ID
    resultados = df_with_id.iloc[indices[0]].copy()
    resultados['distancia'] = distances[0]
    resultados = resultados.sort_values('distancia').reset_index(drop=True)
    
    return resultados