const modal=document.querySelector('.modal-body')
const modal1=document.querySelector('.modal-body1')
const modal2=document.querySelector('.modal-title')
const m=document.querySelector('.mandatory')
function display(){
    m.style.display="none"
}
const RequestLogic = {
    url: `${location.origin}/api/request/`,

    addRequest(name, email,checkList) {
        return fetch(this.url, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({
                name: name,
                email: email,
                services:checkList
            }),
        })
            .then((response) => {
                return response.json();
            }
            )
    },
};


var isCaptchaValid = false
var verifyCallback = function (response) {
    isCaptchaValid = true;
    console.log(response)
}


const addToRequest = document.getElementById('contact-form-button');
const MyForm=document.getElementById('myform');
MyForm.addEventListener("submit", (e)=>{

    e.preventDefault()
    var name=MyForm.name.value
    var email=MyForm.email.value
    
    const check=document.querySelectorAll(".check")
    
    
    var checkList=''
    for(i=0;i<check.length;i++) {
       if(check[i].checked){
        checkList+=check[i].parentNode.children[1].innerText
        checkList+=","
       }
    }
    if(isCaptchaValid==true){
        RequestLogic.addRequest(name, email,checkList);
        MyForm.reset()
        modal.style.display="none"
    modal1.classList.add('modal1-active')
    modal2.style.display="none"
    }
    else{
        alert("Please veriy that you are human")
    }
    

   
});


function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
       var c = ca[i];
       while (c.charAt(0)==' ') c = c.substring(1);
       if(c.indexOf(name) == 0)
          return c.substring(name.length,c.length);
    }
    return "";
}


const emailForm=document.getElementsByClassName("subscribe")[0];
emailForm.addEventListener("submit", async (event)=>{
    event.preventDefault()
    var data=emailForm.email.value
    
    url="/subscribe/"
      
    
    fetch(url, {
        method: "POST",
        headers: {
            "Content_Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),

        },
        body: JSON.stringify({
            "email":data
        })

    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log("data", data);
        document.getElementById('subscribeFormInput').innerHTML="Thank you for subscribing!"
        document.getElementById('subscribeFormInput').style.height="40px"

    })
    emailForm.reset()
})

