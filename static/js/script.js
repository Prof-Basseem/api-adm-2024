// create button move to top and hidden in top  of page when scroll down
var btn = document.createElement("button");
btn.innerHTML = "&#x25B2";
btn.style.position = "fixed";
btn.style.bottom = "20px";
btn.style.right = "20px";
btn.style.fontSize = "14px";
btn.style.border = "2px solid #ffffff";
btn.style.zIndex = "2";
btn.style.backgroundColor = "#007BFF";
btn.style.color = "white";
btn.style.padding = "5px";
btn.style.borderRadius = "50%";
btn.style.cursor = "pointer";
btn.style.fontFamily = "tahoma";
// create event click for button dissaper if in top and appear if scroll down
btn.onclick = function() {
    window.scrollTo(0, 0);
    }
document.body.appendChild(btn);
window.onscroll = function() {
    if (window.pageYOffset > 70) {
        btn.style.display = "block";
    } else {
        btn.style.display = "none";
    }
}