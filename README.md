## dbot-dice
### なにこれ？
Discordでダイス振るやつ  

### Requirements
- Python 3
- Discord Bot Token

### Deploy
HerokuのFree Dynoに環境変数 `DISCORD_ACCESS_TOKEN` をセットしてデプロイ(手動)  

### Usage
#### ダイスを振る
!roll {振るダイスの個数}d{振るダイスの面数}  
command example : `!roll 1d6` (6面ダイスを1個振る)  
response example :  
```
dicebot : @{実行したアカウント}
実行：1d6
結果：4 # 合計値
[4] # すべてのダイスの結果
```

#### 対戦
!match  
実行したアカウントがいるボイスチャンネルのメンバーで対戦表を作る
