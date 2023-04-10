import random
import matplotlib.pyplot as plt

def main():
    # ドアを変更して当たった回数、ドアを変更せずに当たった回数
    C_wins_changed, C_wins_unchanged = 0, 0

    # ドアを変更して当たった確率、ドアを変更せずに当たった確率
    P_wins_changed, P_wins_unchanged = [], []

    # 試行回数の入力
    n = int(input())

    for i in range(n):
        # phase1
        truth = random.randrange(3) # 当たりのドアの選択（0番からランダムに1つ選択）
        player_selected = random.randrange(3) # 挑戦者が選んだドアの番号（0番からランダムに1つ選択）
        doors_unselected = [r for r in range(3) if r != player_selected] # 挑戦者が選ばなかったドアの一覧

        # phase2
        # 司会者がドアを選択
        if player_selected == truth:
            mc_selected = random.choice(doors_unselected) # 挑戦者が選んだドアが正解の場合、司会者は選ばれなかったドアから1つを除いて開ける
        elif doors_unselected[0] == truth:
            mc_selected = doors_unselected[1] # 挑戦者が選ばなかったドアAが正解の場合、司会者は選ばれなかったドアBを開ける
        elif doors_unselected[1] == truth:
            mc_selected = doors_unselected[0] # 挑戦者が選ばなかったドアBが正解の場合、司会者は選ばれなかったドアAを開ける
        
        # phase3
        # 残されたドアを決める
        doors_unselected.remove(mc_selected) # 挑戦者が選ばなかったドアから、司会者が選んだドアを削除
        another_door = doors_unselected[0] # 残されたドア

        # phase4
        # 当たりの回数のカウント
        if another_door == truth:
            C_wins_changed += 1         # 残されたドアが正解の場合、「変更してあたり」をカウント
        elif player_selected == truth:
            C_wins_unchanged += 1       # 挑戦者が選んだドアが正解の場合、「変更しないであたり」をカウント
        
        # 確率推移表示用リストのデータ追加
        P_wins_changed.append(C_wins_changed / (C_wins_changed + C_wins_unchanged))
        P_wins_unchanged.append(C_wins_unchanged / (C_wins_changed + C_wins_unchanged))

    print('ドアを変更して当たった数', C_wins_changed, '確率：', P_wins_changed)
    print('ドアを変更せず当たった数', C_wins_unchanged, '確率：', P_wins_unchanged)

    # グラフ化
    plt.plot(P_wins_changed, label = 'P_wins_changed')
    plt.plot(P_wins_unchanged, label = 'P_wins_unchanged')
    plt.legend()
    plt.show()
    return

if __name__ == '__main__':
    main()