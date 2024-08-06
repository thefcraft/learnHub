document.getElementById('menu-toggle').addEventListener('click', function() {
    const navMenu = document.getElementById('nav-menu');
    navMenu.classList.toggle('active');
});

window.onclick = (event) => {
    const navMenu = document.getElementById('nav-menu');
    const menuToggle = document.getElementById('menu-toggle');
    if (!menuToggle.contains(event.target) && !navMenu.contains(event.target)) {
        if (navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
        }
    }
}

function redirect(elem){
    window.location.href = elem.getElementsByTagName('a')[0].getAttribute('href');
}
function updateCourseCount() {
    document.querySelectorAll('.category').forEach(function(category) {
        // const count = category.querySelectorAll('.course-item').length;
        let courses = category.querySelectorAll('.course-item');
        let count = 0;
        courses.forEach(function(course) {
            count += course.style.display === 'flex';
        });
        category.querySelector('.total-count span').textContent = count;
        const viewMoreButton = category.querySelector('.view-more button');
        viewMoreButton.disabled = count <= 4;
    });
}

function toggleViewMore(categoryId) {
    const courses = document.querySelector(`#${categoryId}`);
    const viewMoreButton = document.querySelector(`#${categoryId}-view-more`);
    
    const visibleCourses = 4;
    const allCourses = courses.querySelectorAll('.course-item');
    allCourses.forEach((course, index) => {
        course.style.display = index < visibleCourses ? 'flex' : 'none';
    });

    viewMoreButton.addEventListener('click', () => {
        allCourses.forEach(course => course.style.display = 'flex');
        viewMoreButton.style.display = 'none';
    });
}

document.getElementById('search').addEventListener('input', function() {
    let searchTerm = this.value.toLowerCase();
    let categories = document.querySelectorAll('.category');

    categories.forEach(function(category) {
        let courses = category.querySelectorAll('.course-item');
        let hasVisibleCourse = false;

        courses.forEach(function(course) {
            let title = course.querySelector('.course-info h3').textContent.toLowerCase();
            if (title.includes(searchTerm)) {
                course.style.display = 'flex';
                hasVisibleCourse = true;
            } else {
                course.style.display = 'none';
            }
        });

        if (hasVisibleCourse) {
            category.style.display = 'block';
        } else {
            category.style.display = 'none';
        }
    });

    updateCourseCount();
});

document.getElementById('category-filter').addEventListener('change', function() {
    let selectedCategory = this.value;
    document.querySelectorAll('.category').forEach(function(category) {
        if (selectedCategory === "" || category.getAttribute('data-category') === selectedCategory) {
            category.style.display = 'block';
        } else {
            category.style.display = 'none';
        }
    });

    updateCourseCount();
});

// Initialize view more functionality
toggleViewMore('dl-courses');
toggleViewMore('ml-courses');
toggleViewMore('web-dev-courses');
toggleViewMore('data-science-courses');
document.querySelectorAll('.category').forEach(function(category) {
    const count = category.querySelectorAll('.course-item').length;
    category.querySelector('.total-count span').textContent = count;
    const viewMoreButton = category.querySelector('.view-more button');
    viewMoreButton.disabled = count <= 4;
});