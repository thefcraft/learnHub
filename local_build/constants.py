from typing import Literal, Dict

DEBUG: bool = True
MINIFY_HTML: bool = False

Tag = Literal['author', 'playlist', 'blog', 'github', 'channel', 'video']
TagColors: Dict[Tag, str] = {
    'author': '#e314b3',
    'playlist': '#ff5722',
    'blog': '#4caf50',
    'github': '#333',
    'channel': '#4d0cd0',
    'video': '#d3ab08',
}
