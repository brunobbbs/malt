#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import random
import functools
from md5 import md5

def GET_AVATAR(autor, membros):
    if autor in membros:
        if 'github' in membros[autor]:
            formatter = "https://avatars.githubusercontent.com/{}?size=250"
            username = membros[autor]['github']
        elif 'email' in membros[autor]:
            formatter = "http://www.gravatar.com/avatar/{}?s=250"
            username = md5(membros[autor]['email'].strip().lower()).hexdigest()
        elif 'twitter' in membros[autor]:
            formatter = "http://avatars.io/twitter/{}"
            username = membros[autor]['twitter']
            if username.startswith("@"):
                username = username[1:]
        else:
            formatter = "/theme/img/{}"
            username = "default_avatar.png"
    else:
        formatter = "/theme/img/{}"
        username = "default_avatar.gif"
    return formatter.format(username)

def GET_ARTICLE_IMAGE(article, root):
    if hasattr(article, 'image'):
        img = article.image
        if img.startswith('/'):
            img = img[1:]
        return img

    if not root:
        return ""

    base = os.path.join('content', root)
    banners = map(functools.partial(os.path.join, root), os.walk(base).next()[2])
    random.seed(article.date)
    return random.choice(banners)

def GET_ARTICLE_AT_GITHUB(article, repo, branch):
    base = os.path.relpath(article.source_path, os.getcwd())
    url = "{}/tree/{}/{}"
    return url.format(repo, branch, base)
