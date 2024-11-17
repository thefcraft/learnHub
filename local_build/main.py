import os; os.chdir(os.path.dirname(__file__))

from data import data, Course, List
from constants import DEBUG, TagColors, MINIFY_HTML
import htmlmin


from jinja2 import Environment, FileSystemLoader



def make_courses(courses: List[Course])->List[dict]:
    return [{
             'icon': course.icon,
             'name': course.name,
             'image_text': course.image_text,
             'href': course.href,
             'author': course.author,
             'tag': course.tag,
             'desc': course.desc,
            } for course in courses]

def make_categories()->List[dict]:
    return sorted([{
             'key': category.key,
             'name': category.name,
             'icon': category.icon,
             'n': len(category.courses),
             'courses': make_courses(category.courses),
             'index': category.index
            }
            for category in data], key=lambda x: x['index'])
 
def minify_html(html):
    return htmlmin.minify(html, remove_comments=True, remove_empty_space=True)
   
# Setup Jinja2 environment
template_dir = os.path.join(os.getcwd(), 'templates')
env = Environment(loader=FileSystemLoader(template_dir))

# Get the template for the homepage
template = env.get_template('index.html')


# Prepare the output directory
output_dir = os.path.join(os.getcwd(), 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Render the index.html template
output_content = template.render(
    categories=make_categories(),
    TagColors=TagColors.items()
)
if MINIFY_HTML: output_content = minify_html(output_content)
# Save the generated HTML file
if DEBUG: 
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf') as f:
        f.write(output_content)
else:
    with open(os.path.join('..', 'index.html'), 'w',  encoding='utf') as f:
        f.write(output_content)
    

print("Site generated in the 'output' directory.")


