burger = document.querySelector(".burger")
navBar = document.querySelector(".navBar")
rightNav = document.querySelector(".rightNav")
logo = document.querySelector(".logo")


burger.addEventListener("click", ()=>{
    logo.classList.toggle("v-class-resp")
    rightNav.classList.toggle("v-class-resp")
    navBar.classList.toggle("h-nav-resp")
})