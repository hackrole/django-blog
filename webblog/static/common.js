function alter(vars){
  if(typeof(vars) == "Obejct"){
    alter(var);
    alter("object");
  }else{
    alter(vars);
  }
}
