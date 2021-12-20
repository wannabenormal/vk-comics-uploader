# Programming vacancies compare

This script will fetch random comic from [xkcd.com](https://xkcd.com/) and publish it at your [VK](https://vk.com) group wall.

### How to install

1. You may want to isolate your envrironment with [venv](https://docs.python.org/3/library/venv.html).
2. Install requirements with `pip` or `pip3`.
```
pip install -r requirements.txt
```
3. Create group at [VK](https://vk.com).
4. Create a standalone app at [VK Dev](https://vk.com/dev).
5. Get an access token with [Implicit Flow](https://vk.com/dev/implicit_flow_user). You need to set in `scope`: `groups`, `photos`, `wall` and `offline`.
6. Create a `.env` file with structure:
```
VK_APP_ID=YOUR_APP_ID
VK_ACCESS_TOKEN=YOUR_ACCESS_TOKEN
VK_GROUP_ID=YOUR_GROUP_ID
```
7. Run the script with `python` or `python3`:
```
python main.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).