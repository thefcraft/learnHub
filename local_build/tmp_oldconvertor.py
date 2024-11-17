from bs4 import BeautifulSoup
import json

html_content = """
<div class="course-grid" id="chill-baby-courses">
                <!-- Additional course items... -->
                <div class="course-item"  onclick="redirect(this)">
                    <div class="image">  
                        <img src="https://i.ytimg.com/vi/hBQS0gZATiY/maxresdefault.jpg" alt="Video Thumbnail">
                        <div class="videosCount">66 videos</div>
                    </div>
                    
                    <div class="course-info">
                        <h3><a href="https://www.youtube.com/@LOFIandCHILL_YT/videos">LOFI and CHILL Youtube</a></h3>
                        <p>Smooth Lofi-Beats and dope Visuals. Leave a sub to join the Community.</p>
                        <section class="tag">
                            <span class="channel">channel</span>
                            <span class="author"><b><i>Author: </i></b>LOFI & CHILL</span>
                        </section>
                    </div>
                </div>
                <div class="course-item"  onclick="redirect(this)">
                    <div class="image">
                        <img src="https://i.ytimg.com/vi/xgwYRUxp2TI/hqdefault.jpg" alt="Hindi Songs Covers">
                        <div class="videosCount">43 videos</div>
                    </div>
                    
                    <div class="course-info">
                        <h3><a href="https://www.youtube.com/playlist?list=PLEWeMUL-7fcO01nReXH___ruc-Xji2d9j">Hindi Songs Covers</a></h3>
                        <p>Hindi Songs Covers By Zendria 🕊</p>
                        <section class="tag">
                            <span class="playlist">playlist</span>
                            <span class="author"><b><i>Author: </i></b>Zendria 🕊</span>
                        </section>
                    </div>
                </div>
                <div class="course-item"  onclick="redirect(this)">
                    <div class="image">  
                        <img src="https://i.ytimg.com/vi/JdnEw7slVpk/maxresdefault.jpg" alt="Video Thumbnail">
                        <div class="videosCount">66 videos</div>
                    </div>
                    
                    <div class="course-info">
                        <h3><a href="https://youtube.com/@PhonkDemonMusic/videos">Phonk Demon Youtube</a></h3>
                        <p>Songs by Phonk Demon</p>
                        <section class="tag">
                            <span class="channel">channel</span>
                            <span class="author"><b><i>Author: </i></b>Phonk Demon</span>
                        </section>
                    </div>
                </div>
                <div class="course-item"  onclick="redirect(this)">
                    <div class="image">  
                        <img src="https://i.ytimg.com/vi/Vm799ekPdc8/maxresdefault.jpg" alt="Video Thumbnail">
                        <div class="videosCount">192 videos</div>
                    </div>
                    
                    <div class="course-info">
                        <h3><a href="https://www.youtube.com/@TheSoulofWindArtist/videos">The Soul of Wind Artist Youtube</a></h3>
                        <p>The Soul of Wind Artist - Part of the music label The Soul of Wind We specialize in gentle, relaxing music as well as fantasy, magical, RPG game music. . .</p>
                        <section class="tag">
                            <span class="channel">channel</span>
                            <span class="author"><b><i>Author: </i></b>The Soul of Wind Artist</span>
                        </section>
                    </div>
                </div>
                <div class="course-item"  onclick="redirect(this)">
                    <div class="image">  
                        <img src="https://i.ytimg.com/vi/sXolSIrZjdw/maxresdefault.jpg" alt="Video Thumbnail">
                        <div class="videosCount">428 videos</div>
                    </div>
                    
                    <div class="course-info">
                        <h3><a href="https://www.youtube.com/@sunsetmoodz/videos">Sunset Mood Youtube</a></h3>
                        <p>Sunset Mood © Magic Music Group LLC 2022. We own rights to all content uploaded. Any reproduction of this content will result in a Content ID claim.</p>
                        <section class="tag">
                            <span class="channel">channel</span>
                            <span class="author"><b><i>Author: </i></b>Sunset Mood</span>
                        </section>
                    </div>
                </div>
                <div class="course-item"  onclick="redirect(this)">
                    <div class="image">
                        <img src="https://i.ytimg.com/vi/C237b1fh_Ic/maxresdefault.jpg" alt="bütün coverlar / all covers">
                        <div class="videosCount">142 videos</div>
                    </div>
                    
                    <div class="course-info">
                        <h3><a href="https://www.youtube.com/playlist?list=PLkTt3JK3b61QgirOVj1ou0tYCiDXlxMFl">bütün coverlar / all covers</a></h3>
                        <p>bütün coverlar / all covers By Nursena Yener</p>
                        <section class="tag">
                            <span class="playlist">playlist</span>
                            <span class="author"><b><i>Author: </i></b>Nursena Yener</span>
                        </section>
                    </div>
                </div>
            </div>
"""


soup = BeautifulSoup(html_content, 'html.parser')


course_items = soup.find_all('div', class_='course-item')
for course_item in course_items:
    name = course_item.find('h3').find('a').text.strip()
    desc = course_item.find('p').text.strip()
    
    # Extract the dynamic class name for the tag
    tag_section = course_item.find('section', class_='tag')
    tag_spans = tag_section.find_all('span')
    tag_class = [tag_span for tag_span in tag_spans if tag_span.get('class')[0] != 'author'][0]  # Extract the class name dynamically


    # Extract the number of videos (image_text)
    image_text = course_item.find('div', class_='videosCount').text.strip()
    
    # Extract the tag (playlist)
    tag = tag_class.text.strip()

    # Extract the author
    author = course_item.find('span', class_='author').text.strip().replace('Author: ', '')

    # Extract the href (course URL)
    href = course_item.find('h3').find('a')['href']

    # Extract the image URL (icon)
    icon = course_item.find('img')['src']

    course_data = {
        "name": name,
        "desc": desc,
        "tag": tag,
        "image_text": image_text,
        "author": author,
        "href": href,
        "icon": icon
    }
    # Print the result
    print(json.dumps(course_data))
    # print('--------------------------------------------------------')
