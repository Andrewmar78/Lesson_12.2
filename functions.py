import json

POST_PATH = "posts.json"


# Загрузка постов из json-файла
def load_posts():
    with open(POST_PATH, "r", encoding="utf-8") as file:
        posts = json.load(file)
    return posts


# Запись поста в json-файл
def upload_posts(posts):
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4, ensure_ascii=False)
