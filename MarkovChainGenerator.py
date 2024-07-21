import random

def Main():
    InputText = "ぶぶんぶんすうぶんかい"
    NumOfAttempts = 10000

    # 前処理
    ListedText = list(InputText)
    
    # 後継文字を分析
    FollowCounts = FollowCharCount(ListedText)

    # 遷移確率を計算
    FollowProps = FollowCharProps(FollowCounts)

    for i in range(NumOfAttempts):

        # 遷移確率に基づき文字列を生成
        OutputText = GenerateText(ListedText, FollowProps)
        print(OutputText)

        # 同一なら終了
        if OutputText == InputText:
            print("Number of attempts: " + (i + 1))
            break


def GenerateText(ListedText, FollowProps):

    # 最初の文字を設定
    currentChar = random.choice(ListedText)
    OutputText = currentChar
    
    # 各文字について
    for _ in range(len(ListedText) - 1):      
        if currentChar in FollowProps:
            nextChars = list(FollowProps[currentChar].keys())
            props = list(FollowProps[currentChar].values())
            
            # random.chicesで入れ子構造によりリストが返ってくるのでその最初の要素[0]を指定
            # 現在の文字を更新して文字列追加
            currentChar = random.choices(nextChars, props)[0]
            OutputText += currentChar  
        else:
            # 最初の文字続きがない(InputTextの最後の文字で固有の場合)とき
            break
        
    return OutputText


def FollowCharCount(ListedText):
    """
    次の文字が何かを総当たりで計算しカウント
    今の文字 * 次の文字 の表に代入
    """
    FollowCounts = {}

    for i in range(len(ListedText) - 1):
        currentChar = ListedText[i]
        nextChar = ListedText[i + 1]

        # 今の文字が新規ならその文字のカウント枠を作成(初期化)
        if currentChar not in FollowCounts:
            FollowCounts[currentChar] = {}

        # 次の文字が今の文字に対して初の遷移先ならその文字のマスを作成(初期化)
        if nextChar not in FollowCounts[currentChar]:
            FollowCounts[currentChar][nextChar] = 0

        # 対応するマスに1追加
        FollowCounts[currentChar][nextChar] += 1

    return FollowCounts


def FollowCharProps(FollowCounts):
    """各文字に遷移する割合を計算
    """

    FollowProps = {}

    for char, nextChars in FollowCounts.items():

        # 今の文字からの遷移先を同文字ありで足し合わせ
        totalCount = sum(nextChars.values())

        # 割合記入枠を作成
        FollowProps[char] = {}
        for nextChars, count in nextChars.items():
            # 対応するマスに割合を記入
            FollowProps[char][nextChars] = count / totalCount
    
    return FollowProps


if __name__ == "__main__":
    Main()