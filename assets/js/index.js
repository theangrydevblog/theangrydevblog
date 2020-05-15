import "./prism"
import "../css/prism.css"
import "../css/main.css";

var AllCodeTags = Array.from(document.querySelectorAll('code'));
AllCodeTags.forEach(function(tag){
    tag.innerHTML = tag.innerHTML.trim();
    tag.parentNode.innerHTML = tag.parentNode.innerHTML.trim();
});