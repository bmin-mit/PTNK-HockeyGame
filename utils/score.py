def read_data():
    with open("score.txt", "r", encoding="utf-8-sig") as f:
        data = f.readlines()
    return data

def write_data(score1, score2):
    data = [f"{score1},{score2}\n"]
    data.extend(read_data())
    with open("score.txt", "w") as f:
        f.writelines(data[:min(5, len(data))])
