function validate() {    
    var fname = document.reg_form.fname;    
    var section = document.reg_form.section;    
    var branch = document.reg_form.branch;      
    var email = document.reg_form.email;    
    var StudentID = document.reg_form.StudentID;    
     

    if (StudentID.value.length <= 0) {    
        alert("Student ID is required");    
        StudentID.focus();    
        return false;    
    }  
    if (fname.value.length <= 0) {    
        alert("Name is required");    
        fname.focus();    
        return false;    
    }    
    if (section.value.length <= 0) {    
        alert("Section is required");    
        section.focus();    
        return false;    
    }    
    if (branch.value.length <= 0) {    
        alert("Branch is required");    
        branch.focus();    
        return false;    
    }    
    
    if (email.value.length <= 0) {    
        alert("Email Id is required");    
        email.focus();    
        return false;    
    }    
      
    return false;    
}  