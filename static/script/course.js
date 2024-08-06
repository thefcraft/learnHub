var pathname = window.location.pathname;
if (pathname.endsWith('index.html')) {
    var modifiedPathname = pathname.substring(0, pathname.length - 'index.html'.length);
    if (modifiedPathname.endsWith('/')) {
        modifiedPathname = modifiedPathname.slice(0, -1);
    }
    pathname = modifiedPathname;
} else {
    var modifiedPathname = pathname;
    if (modifiedPathname.endsWith('/')) {
        modifiedPathname = modifiedPathname.slice(0, -1);
    }
    pathname = modifiedPathname;
}
const key = pathname;

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

function getState(){
    const state = localStorage.getItem(key);
    if(state === null){
        return {};
    }
    else{
        return JSON.parse(state);
    }
}

function redirect(url, id){
    let elem = document.getElementById(`checkbox-${id}`);
    if (elem !== null){
        elem.checked = true;
    }
    saveState(true, id);
    // window.location.href = url;
    window.open(url, '_blank').focus();
}

function saveState(value, id){
    const newState = {
        ...getState(),
        [id]: value,
    };
    localStorage.setItem(key, JSON.stringify(newState));
    console.log(getState());
}

onload = () => {
    const state = getState();
    for (const k in state) {
        let elem = document.getElementById(`checkbox-${k}`);
        if (elem !== null){
            elem.checked = state[k];
        }
    }
};


// function handleImageError(elem){
//     console.log('Changing image src');
//     elem.onerror=null;
//     let newUrl = elem.src.replace('/maxresdefault.jpg', '/hqdefault.jpg');
//     elem.src=newUrl;
// }