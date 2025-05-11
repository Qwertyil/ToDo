const theme_name = document.getElementById('theme').innerHTML;

const theme = document.getElementById(theme_name);

if (theme) {
    theme.style.color = 'white';
    theme.style.backgroundColor = primaryColor;
}