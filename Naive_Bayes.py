import pandas as pd

tennis_dataset = pd.read_csv("PlayTennis.csv")

# experiment = tennis_dataset[tennis_dataset["Outlook"] == "Sunny"]

# (tennis_dataset["Outlook"] == "Sunny") & (tennis_dataset["Play Tennis"] == "Yes")


def create_probability_tables():
    all_tables = []
    for column in tennis_dataset.columns:
        if column == "Play Tennis":
            continue
        unique_status = set(tennis_dataset[column])
        table = pd.DataFrame(columns=[column, "Play Tennis", "Don't Play Tennis"])
        for status in unique_status:
            p_yes = len(tennis_dataset[(tennis_dataset[column] == status) & (tennis_dataset["Play Tennis"] == "Yes")]) / 9
            p_no = len(tennis_dataset[(tennis_dataset[column] == status) & (tennis_dataset["Play Tennis"] == "No")]) / 5

            table.loc[len(table.index)] = [status, p_yes, p_no]
        all_tables.append(table)

    return all_tables


all_tables = create_probability_tables()
for table in all_tables:
    print(table, '\n')

test_sample = {
    "Outlook": "Sunny",
    "Temperature": "Cool",
    "Humidity": "Normal",
    "Wind": "Weak"
}


def predict_given_test_sample(test_sample):
    p_dash_yes = 9 / 14
    p_dash_no = 1 - p_dash_yes

    for table in all_tables:
        table_name = table.columns[0]
        status = test_sample[table_name]

        p_dash_yes *= table[table[table_name] == status].iloc[0,  1]
        p_dash_no *= table[table[table_name] == status].iloc[0, 2]

    return p_dash_yes >= p_dash_no


print("For the test case:\n", test_sample, "\nThe result is", predict_given_test_sample(test_sample))

