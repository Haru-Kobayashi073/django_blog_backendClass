import requests

class QiitaApiClient:
    """Qiita の API を叩く役割を持つクラス"""

    def get_django_articles(self):
        # get リクエストを送る
        response = requests.get(
            "https://qiita.com/api/v2/tags/django/items",
            headers={"Authorization": "Bearer "},
        )
        
        # アクセストークンがない場合はこう
        # response = requests.get("https://qiita.com/api/v2/tags/django/items")
        
        # とりあえず print してみる
        # response.json() で json 形式のレスポンスの中身が見られる
        json = response.json()
        print(json[0]['title'])