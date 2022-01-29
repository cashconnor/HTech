// in data, I like to store a view object with all 
// the values I need for a component to manage 
// it's 'view' state - ie loading, 
// or in this case, if the user is at the top of the page or not
function data () {
    return {
        view: {
            atTopOfPage: true
        }
    }
}

// a beforeMount call to add a listener to the window
function beforeMount () {
    window.addEventListener('scroll', this.handleScroll);
}

methods: {
    // the function to call when the user scrolls, added as a method
    function handleScroll(){
        // when the user scrolls, check the pageYOffset
        if(window.pageYOffset>0){
            // user is scrolled
            if(this.view.atTopOfPage) this.view.atTopOfPage = false
        }else{
            // user is at top of page
            if(!this.view.atTopOfPage) this.view.atTopOfPage = true
        }
    }
}

//Get the button:
mybutton = document.getElementById("scrollbtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}