import df
df['Rating'] = df['Humidity'].apply(lambda x:
    '🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜'if x > -0.01 else(
    '🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜'if x > -0.11 else(
    '🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜'if x > -0.21 else(
    '🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜'if x > -0.31 else(
    '🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜'if x > -0.41 else(
    '🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜'if x > -0.51 else(
    '🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜'if x > -0.61 else(
    '🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜'if x > -0.71 else(
    '🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜'if x > -0.81 else(
    '🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥'if x > -0.91 else(
    '🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜ 'if x > 0 else(
    '🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜' if x >= 0.11 else(
    '🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜' if x >= 0.21 else(
    '🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜' if x >= 0.31 else(
    '🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜' if x >= 0.41 else(
    '🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜'if x >= 0.51 else(
    '🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜'if x >= 0.61 else(
    '🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜'if x >= 0.71 else(
    '🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜'if x >= 0.81 else(
    '🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩'if x >= 0.91 else " "
    
    
    ))))))))))))))))))))