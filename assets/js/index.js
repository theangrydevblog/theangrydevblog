import "./prism"
import "../css/prism.css"
import "../css/main.css";

var AllCodeTags = Array.from(document.querySelectorAll('code'));
AllCodeTags.forEach(function(tag){
    tag.innerHTML = tag.innerHTML.trim();
    tag.parentNode.innerHTML = tag.parentNode.innerHTML.trim();
});

var navButton = document.querySelector(".navbar-toggler-icon");
window.addEventListener("click", function(e){
   navbar.style.backgroundColor = "whitesmoke";
});

var navbar = document.querySelector("nav");
window.addEventListener("scroll", function(e){
    if (window.scrollY !== 0){
        navbar.style.backgroundColor = "whitesmoke";
    }else{
        navbar.style.backgroundColor = "transparent";
    }
});

