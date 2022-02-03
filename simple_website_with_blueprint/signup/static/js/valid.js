function Signup(){


    var q=document.getElementById("uname");
    var w=document.getElementById("pass");
    var e=document.getElementById("cpass");
    var r=document.getElementById("emai");
    var t=document.getElementById("phno");
    var numlen = w.value.replace(/[^0-9]/g,"").length;
    var spelen = w.value.replace(/[a-zA-Z0-9 ]/gi,"").length;

    if(q.value==""){
    window.alert("please enter your username");
    q.focus();
    return false;
}

if(w.value.length != 8){
    window.alert("The password length should be 8 characters");
    w.focus();
    return false;
}

if(numlen != 1){
    window.alert("The password must contain only one number, please check the password");
    w.focus();
    return false;
}

if(spelen != 1){
    window.alert("The password must contain only one special character, please check the password");
    w.focus();
    return false;
}
    if(w.value==""){
    window.alert("please enter the password");
    w.focus();
    return false;
}
    
    if(e.value==""){
    window.alert("please re-enter the password");
    e.focus();
    return false;
}

    if(w.value!=e.value){
    window.alert("the password did not match with the confirm password");
    return false;
}
    if(r.value==""){
    window.alert("please enter your email");
    r.focus();
    return false;
}
    if(t.value==""){
    window.alert("please enter your phone number");
    t.focus();
    return false;
}

    return true;
};
    
