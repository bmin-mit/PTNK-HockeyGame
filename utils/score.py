import json
def read_data():
    with open("score.txt", "r") as f:
        data = f.readlines()
    return [json.loads(line) for line in data]

def write_data(score1, score2):
    data = [f"{score1},{score2}"]
    data.extend(read_data())
    with open("score.txt", "w") as f:
        f.writelines(data[:min(5, len(data))])
