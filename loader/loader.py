from flask import Blueprint, request, render_template

import logging
# logging.basicConfig(encoding="utf-8", level=logging.INFO)
logging.basicConfig(filename="basic.log", level=logging.INFO)

from functions import load_posts, upload_posts

loader_blueprint = Blueprint("loader", __name__, url_prefix="/post", static_folder="static", template_folder="templates")


# Вьюшка формы
@loader_blueprint.route("/form/")
def form():
    return render_template("post_form.html")


# Вьюшка загрузки поста
@loader_blueprint.route("/upload/", methods=["GET", "POST"])
def upload():
    try:
        file = request.files["picture"]
        filename = file.filename
        content = request.values["content"]
        posts = load_posts()
        posts.append({
            "pic": f"uploads/images/{filename}",
            "content": content
        })
        upload_posts(posts)
        file.save(f"uploads/images/{filename}")
        # Проверка расширения файла
        if filename.split(".")[-1] not in ["png", "jpeg", "jpg"]:
            logging.info("Это не картинка")
    except FileNotFoundError:
        logging.error("Ошибка загрузки файла")
        return "<h1> Файл не найден </h1>"
    else:
        return render_template("post_uploaded.html", pic=f"/uploads/images/{filename}", content="content")
