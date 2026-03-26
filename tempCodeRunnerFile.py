        data = r.json()
        print(data)
        articles = data.get('articles', [])
        for article in articles[:6]:  # optional: limit to top 5
            title = article.get('title')