window.addEventListener('DOMContentLoaded', ()=>{

    // declaring vars
    var downScroller = document.querySelector('#down_scroller')
    


    // declaring functions
    function scrollPageDown(){
            window.scrollBy(0,4000)
       

    }
 

    // adding event listeners
    downScroller.addEventListener('click',scrollPageDown)

    
    



})