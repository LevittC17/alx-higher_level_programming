#!/usr/bin/node
function printMessage(){
    const noArgv = arguments.length;
    
    if (noArgv === 0){
        console.log("No argument");
    }
    else if (noArgv == 1){
        console.log("Argument found");
    }
    else
        console.log("Arguments found");
}
