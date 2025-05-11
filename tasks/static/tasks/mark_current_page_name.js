const url = window.location.href;
const root = document.documentElement;
const primaryColor = getComputedStyle(root).getPropertyValue('--primary-color').trim();

const element = document.getElementById(
    url.includes('periodic') ? 'periodic' :
    url.includes('completed') ? 'completed' :
    url.includes('settings') ? 'settings' : 'main'
);

if (element) {
    element.style.color = 'white';
    element.style.backgroundColor = primaryColor;
}