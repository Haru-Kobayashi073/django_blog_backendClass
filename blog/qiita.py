import requests

class QiitaApiClient:
    """Qiita の API を叩く役割を持つクラス"""

    def get_django_articles(self):
        # get リクエストを送る
        response = requests.get(
            "https://qiita.com/api/v2/tags/django/items",
            headers={"Authorization": "Bearer 51ab5758e906067b2a5ef6e7824b7fb969544e81"},
        )
        
        # アクセストークンがない場合はこう
        # response = requests.get("https://qiita.com/api/v2/tags/django/items")
        
        # とりあえず print してみる
        # response.json() で json 形式のレスポンスの中身が見られる
        json = response.json()
        print(json[0]['title'])
        qiita_articles = []
        json = response.json()
        for json_article in json:
            qiita_article = QiitaArticle(
                json_article["title"],
                json_article["url"],
            )
            qiita_articles.append(qiita_article)
        return qiita_articles
      
class QiitaArticle:

    def __init__(self, title, url):
        self.title = title
        self.url = url