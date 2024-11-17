from dataclasses import dataclass
from typing import List, NewType, Literal
import os
import json
from constants import Tag

ImgLink = NewType('ImgLink', str)  
IconLink = NewType('IconLink', str)  
Link = NewType('Link', str)  


@dataclass
class Course: 
    name: str
    desc: str
    tag: Tag
    image_text: str
    author: str
    href: Link
    icon: ImgLink
    
@dataclass
class Category:
    key: str
    name: str
    icon: IconLink
    courses: List[Course]
    index: int # for sorting


def initialize()->List[Category]:
    categories = []
    for filename in os.listdir("categories"):
        filepath = os.path.join("categories", filename)
        with open(filepath, 'r') as f: data = json.load(f)
        categories.append(Category(
            data['key'], data['name'], data['icon'],
            [
             Course(
                 course['name'], course['desc'], course['tag'], course['image_text'], course['author'], course['href'], course['icon']
             )
             for course in data['courses']],
            index=data['index']
        ))
        
   
    return categories

data: List[Category] = initialize()


if __name__ == "__main__":
    Course('10 Videos', 
           'Neural Networks: Zero to Hero', 
           'A comprehensive course on building neural networks from scratch. Learn about backpropagation and modern deep learning techniques.',
           'playlist',
           'Andrej Karpathy'
           'https://i.ytimg.com/vi/VMj-3S1tku0/maxresdefault.jpg'
        )