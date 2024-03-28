function check_me(input_id){
    var checked_input = document.querySelector("input[id=" + input_id + "]");
    var checked_label = document.querySelector("label[name=" + input_id + "]");

    if (checked_input.checked){
        checked_label.style.textDecoration = "line-through";
    }
    else {
         checked_label.style.textDecoration = "";
    }

    var btn = document.getElementById("remove_btn");

    btn.value = "REMOVE ITEMS";
    btn.style.color = "#FFFFFF";
    btn.style.backgroundColor = "#FE7575";
    btn.style.cursor = "pointer";
}
function func(){
    window.location.href="/add_client";
}
function viewclient(id) {
    
    window.location.href=`/view_client?id=${id}`;
}
function delFunction(id){
    window.location.href=`/del_client?id=${id}`;
}