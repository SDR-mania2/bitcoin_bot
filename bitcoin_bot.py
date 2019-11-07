import pybitflyer
import json

def main():

  #板情報を取得。本来API keyが必要だが、板情報取得だけなら不要。
  api = pybitflyer.API()
  
  #本来は以下のように指定する。
  #api = pybitflyer.API(api_key="...", api_secret="...")

  #BTC_JPYを指定して取得。
  board = api.board(product_code="BTC_JPY")

  #JSONに変換して表示する。
  print("{}".format(json.dumps(board,sort_keys=True,indent=4)))

if __name__=='__main__':
    main()

#今後チャート作成や取引部分も実装予定。
#というか動くのかこれ…
