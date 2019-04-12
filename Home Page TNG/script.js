function changePicture(source){
    // Changes the profile_pic image to the new input source (2 buttons underneath my picture)
    document.getElementById("profile_pic").src = source;
}

function changeFlair(newColor){
    // Changes the flair color of the site (3 Buttons at the top of the screen)
    document.getElementsByClassName("posts-section")[0].style.borderColor = newColor;
    document.getElementsByClassName("pic")[0].style.borderColor = newColor;
    document.getElementsByClassName("transcript")[0].style.borderColor = newColor;
    var postTitle = document.getElementsByClassName("post_title");
    var dates = document.getElementsByClassName("date");
    for (var i = 0; i < postTitle.length && i < dates.length; i++) {
        postTitle[i].style.color = newColor;
        dates[i].style.color = newColor;
    }
}

function highlightTable(highlightColor){
    // Highlights the table for easier reading (Mouseover the table)
    document.getElementsByTagName("table")[0].style.backgroundColor = highlightColor;
}

function mostRecent(){
    // Scrolls to the most recent post ('Most Recent Post' button at bottom of page)
   var first = document.querySelector(".post");
   var first_top = first.top + "px";
   var first_left = first.left + "px";
   window.scrollTo(first_top, first_left);
}
