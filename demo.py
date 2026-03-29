
import os
from src.bilibili_client.ws import BiliClient

import dotenv
dotenv.load_dotenv()  # 加载环境变量

cli = BiliClient(
    idCode=os.getenv("ID_CODE"),  # 主播身份码
    appId=int(os.getenv("APP_ID")),  # 应用id
    key=os.getenv("ACCESS_KEY_ID"),  # access_key
    secret=os.getenv("ACCESS_KEY_SECRET"),  # access_key_secret
    host="https://live-open.biliapi.com") # 开放平台 (线上环境)
with cli:
    cli.run()