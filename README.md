
# 🌍 Location - IP 定位工具

## ✨ 用途

Location 是一款强大的 IP 定位工具，旨在帮助用户快速、准确地获取访问者的地理IP位置。

## ⚙️ 安装使用

   1.**下载 docker 镜像**

   ~~~bash
   docker pull jiujiuyao/location:latest 
   ~~~

   2.**通过 git 下载配置文件(或者直接手动下载)**

   ~~~bash
   sudo apt update
   sudo apt install git
   git clone https://github.com/Jiujiuwhoami/location.git
   cd location
   mkdir locations
   ~~~

   3.**启动 docker**

   ~~~bash
   docker network create --subnet=172.66.66.0/24 hacker
   docker-compose up -d
   ~~~

   4.**配置 ngrok 代理**

   * 官网下载安装 [ngrok](https://dashboard.ngrok.com/get-started/setup)
   * 配置密钥
   ```bash
   ngrok config add-authtoken
   ```
   * 开启代理（获取到访问链接）
   ```bash
   ngrok http http://localhost:5005
   ```

   5.**访问**

   * 例`https://******.ngrok-free.app`

   * 访问 `docker` 日志

   ~~~bash
   docker logs hack_location
   ~~~

   * 所有访客记录会保留在 `locations` 文件夹下

   ~~~bash
   cd locations
   ls
   ~~~


## 💡 自定义网页与配置

   * 当需要使用自定义前端页面时，只需将项目文件放在 `templates` 目录下，入口文件默认为 `index.html`.

   * 修改 `docker-compose.yml` 文件

   ~~~yml
   services:
     location:
       image: jiujiuyao/location:latest 
       container_name: hack_location        
       restart: unless-stopped               
       networks:
         hacker:
           ipv4_address: 172.66.66.2        
       environment:
         - PORT=5005                
         - GO_URL=https://baidu.com # 修改成当请求成功时候的跳转链接
         - ERROR_URL=https://bing.cn # 修改成当请求失败时候的跳转链接
       volumes:
         - ./routes.py:/app/routes.py        
         - ./templates/:/app/templates/     
         - ./locations/:/app/locations/ 
       working_dir: /app                    
       command: ['uvicorn', 'app:app', '--host', '0.0.0.0', '--port', '5005'] 
       ports:
         - "5005:5005"                      
   networks:
     hacker:
       external: true                        
   ~~~
   *GO_URL=https://baidu.com # 修改成当请求成功时候的跳转链接*

   *ERROR_URL=https://bing.cn # 修改成当请求失败时候的跳转链接*

   * 如需替换前端路由或入口文件，则修改 `routes.py`

   ~~~py
   # routes.py
   from fastapi import APIRouter, Request
   from fastapi.responses import HTMLResponse
   from fastapi.templating import Jinja2Templates
   import os

   router = APIRouter()
   templates = Jinja2Templates(directory="templates")
   GO_URL = os.getenv('GO_URL', '/static/js/coffee.html')  
   ERROR_URL = os.getenv('ERROR_URL', '/static/js/coffee2.html')  

   @router.get("/location", response_class=HTMLResponse)
   async def index(request: Request):
       return templates.TemplateResponse("index.html", {"request": request, "go_url": GO_URL, "error_url": ERROR_URL})
   ~~~
   *修改 `@router.get("/location", response_class=HTMLResponse)` 路由 `"/location"`*

   *修改 `return templates.TemplateResponse("index.html", {"request": request, "go_url": GO_URL, "error_url": ERROR_URL})` 入口文件 `"index.html"`*

   * 重新启动 `docker`

## 🤝 贡献

欢迎任何人参与贡献！如果您有改进建议或发现错误，请提交 issue 或 pull request。

## 📄 许可证

此项目采用 MIT 许可证，详情请查看 [LICENSE](LICENSE) 文件。

## 📬 联系我们

如有问题，请通过以下方式联系：

- **Wechat**: `jiujiuwhoami`


## 开源软件免责声明

本开源软件由 Jiujiuwhoami 开发和维护，旨在帮助用户快速、准确地获取访问者的地理IP位置。使用本软件即表示您同意以下条款：

1. **使用风险**：
   本软件按“现状”提供，不保证其适用性、可靠性或安全性。用户在使用本软件时需自行承担所有风险，包括但不限于因使用本软件而导致的任何损失或损害。

2. **责任限制**：
   在法律允许的范围内，开发者不对因使用本软件或无法使用本软件而导致的任何直接、间接、偶然、特殊或后果性损害承担责任。开发者不对用户在使用本软件过程中进行的任何活动负责。

3. **用户责任**：
   用户承认并同意，使用本软件进行的任何活动（包括但不限于合法性、合规性等）均由用户自行负责。开发者不对用户的任何行为承担责任。

4. **第三方内容**：
   本软件可能包含第三方链接或内容。我们对这些第三方内容的准确性或合法性不作任何保证，并不承担任何责任。

5. **法律适用**：
   本免责声明受世界各国法律的管辖，并根据相关法律进行解释。

使用本软件即表示您接受本免责声明。如果您不同意以上条款，请勿使用本软件。

