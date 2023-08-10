var subjectObject = {
   Departments:{
   "Technical": ["BTech","B.arch","MTec","m.arch","civil","electronics"]


"science":["Bsc","Msc","Bfarm","Mfarm"]

"commerce":["B.com","M.com","BBA","MBA"]
}
}


window.onload = function(){
   var Departments=document.getElementById('Departments')
   var Courses=document.getElementById('Courses')

   for(var x in subjectObject){
   //console.log(x);
   first.options[first.options.length] = new Option(x)
   }

   first.onchange = function(){
   second.length = 1
   for (var y in subjectObject[this.value]){
   //console.log(y);
   second.options[second.options.length] = new Option(y)
   }
   }
}
}































