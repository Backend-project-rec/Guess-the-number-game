import random

def get_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("無効な入力です。もう一度整数を入力してください。")

# 最小値と最大値を取得
n = get_input("最小値を入力してください: ")
m = get_input("最大値を入力してください: ")

# 最小値が最大値以下であることを確認
while n > m:
    print("最小値は最大値以下でなければなりません。")
    n = get_input("最小値を入力してください: ")
    m = get_input("最大値を入力してください: ")

# nからmの範囲で乱数を生成
random_number = random.randint(n, m)

# 最大試行回数は10回
max_tries = 10

for i in range(max_tries):
    guess = get_input(f"推測する数値を入力してください ({n} から {m} まで): ")

    if guess == random_number:
        print(f"おめでとう！正解は {random_number} でした。{i + 1} 回目で当たりました！")
        break
    elif guess < random_number:
        print("もっと大きい数です。")
    else:
        print("もっと小さい数です。")

    remaining_tries = max_tries - (i + 1)
    if remaining_tries > 0:
        print(f"残り試行回数は {remaining_tries} 回です。")
else:
    print(f"ゲームオーバーです。正解は {random_number} でした。")