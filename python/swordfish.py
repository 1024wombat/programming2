while True:
    print('あなたはだれ？')
    name =input()
    if name != 'joe':
        continue
    print('こんにちはjoe。パスワードは何？')
    password = input()
    if password == 'swordfish':
        break
print('認証しました')
